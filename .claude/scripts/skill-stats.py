#!/usr/bin/env python3
"""Thống kê kỹ năng & chứng chỉ từ tin tuyển dụng đã thu thập.

Dùng:
    python3 .claude/scripts/skill-stats.py tracks/<role>/research [--levels junior,middle]

Đọc trong thư mục research:
    postings.jsonl  mỗi dòng 1 tin tuyển dụng (schema: xem skill nghien-cuu-thi-truong)
    taxonomy.json   {"aliases": {...}, "groups": {...}, "cert_aliases": {...}} (không bắt buộc)

In bảng markdown ra stdout. Chỉ dùng thư viện chuẩn để chạy được ở mọi máy.
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

TIERS = [(60, "Cốt lõi", "L4"), (30, "Quan trọng", "L3"), (15, "Nên biết", "L2"), (0, "Bỏ qua", "-")]
CERT_THRESHOLD = 15


def tier(pct):
    for threshold, name, level in TIERS:
        if pct >= threshold:
            return name, level
    return TIERS[-1][1], TIERS[-1][2]


def pct(count, total):
    return round(100.0 * count / total, 1) if total else 0.0


def normalize(name, aliases):
    name = name.strip()
    return aliases.get(name.lower(), name)


def load_taxonomy(research_dir):
    path = research_dir / "taxonomy.json"
    if not path.exists():
        return {}, {}, {}
    data = json.loads(path.read_text(encoding="utf-8"))
    aliases = {k.lower(): v for k, v in data.get("aliases", {}).items()}
    cert_aliases = {k.lower(): v for k, v in data.get("cert_aliases", {}).items()}
    return aliases, data.get("groups", {}), cert_aliases


def load_postings(research_dir, levels, warnings):
    path = research_dir / "postings.jsonl"
    if not path.exists():
        sys.exit(f"Không tìm thấy {path}")
    postings, seen_urls = [], set()
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            p = json.loads(line)
        except json.JSONDecodeError as e:
            warnings.append(f"Dòng {lineno}: JSON lỗi ({e.msg}) — bỏ qua")
            continue
        url = p.get("url", "")
        if not url:
            warnings.append(f"Dòng {lineno}: thiếu url — bỏ qua (mọi tin phải kiểm chứng được)")
            continue
        if url in seen_urls:
            warnings.append(f"Dòng {lineno}: trùng url {url} — bỏ qua")
            continue
        seen_urls.add(url)
        if levels and p.get("level", "unknown") not in levels:
            continue
        postings.append(p)
    return postings


def analyze(postings, aliases, groups, cert_aliases):
    req, pref, any_ = Counter(), Counter(), Counter()
    group_req, group_any = Counter(), Counter()
    cert_req, cert_any = Counter(), Counter()
    skill_to_groups = {}
    for group, skills in groups.items():
        for s in skills:
            skill_to_groups.setdefault(normalize(s, aliases), []).append(group)

    for p in postings:
        r = {normalize(s, aliases) for s in p.get("required", [])}
        pr = {normalize(s, aliases) for s in p.get("preferred", [])} - r
        for s in r:
            req[s] += 1
            any_[s] += 1
        for s in pr:
            pref[s] += 1
            any_[s] += 1
        gr = {g for s in r for g in skill_to_groups.get(s, [])}
        ga = gr | {g for s in pr for g in skill_to_groups.get(s, [])}
        for g in gr:
            group_req[g] += 1
        for g in ga:
            group_any[g] += 1

        certs = p.get("certifications", {}) or {}
        cr = {normalize(c, cert_aliases) for c in certs.get("required", [])}
        cp = {normalize(c, cert_aliases) for c in certs.get("preferred", [])} - cr
        for c in cr:
            cert_req[c] += 1
        for c in cr | cp:
            cert_any[c] += 1
    return req, pref, any_, group_req, group_any, cert_req, cert_any, skill_to_groups


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("research_dir")
    ap.add_argument("--levels", default="", help="Lọc theo level, vd: junior,middle (mặc định: tất cả)")
    args = ap.parse_args()

    research_dir = Path(args.research_dir)
    levels = {lv.strip() for lv in args.levels.split(",") if lv.strip()}
    warnings = []
    aliases, groups, cert_aliases = load_taxonomy(research_dir)
    postings = load_postings(research_dir, levels, warnings)
    n = len(postings)
    if n == 0:
        sys.exit("Không có tin tuyển dụng nào phù hợp bộ lọc.")

    req, pref, any_, group_req, group_any, cert_req, cert_any, skill_to_groups = analyze(
        postings, aliases, groups, cert_aliases)

    evidence = Counter(p.get("evidence", "page") for p in postings)
    sources = Counter(p.get("source", "unknown") for p in postings)
    level_count = Counter(p.get("level", "unknown") for p in postings)

    out = []
    out.append("## Mẫu dữ liệu\n")
    out.append(f"- Số tin tuyển dụng phân tích: **{n}**" + (f" (lọc level: {', '.join(sorted(levels))})" if levels else ""))
    out.append("- Theo nguồn: " + ", ".join(f"{k}: {v}" for k, v in sources.most_common()))
    out.append("- Theo level: " + ", ".join(f"{k}: {v}" for k, v in level_count.most_common()))
    out.append("- Bằng chứng: " + ", ".join(f"{k}: {v}" for k, v in evidence.most_common())
               + " (page = đã đọc trang gốc, snippet = chỉ thấy qua kết quả tìm kiếm)")
    if n < 30:
        out.append(f"- ⚠️ Cỡ mẫu nhỏ ({n} < 30): tỷ lệ % chỉ mang tính tham khảo.")
    out.append("")

    if groups:
        out.append("## Theo nhóm kỹ năng\n")
        out.append("| Nhóm | % tin nhắc tới | % bắt buộc | Tầng | Cấp độ đích | Tool phổ biến nhất trong nhóm |")
        out.append("|---|---|---|---|---|---|")
        for g, c in sorted(group_any.items(), key=lambda x: -x[1]):
            p_any = pct(c, n)
            t, lv = tier(p_any)
            members = [s for s, gs in skill_to_groups.items() if g in gs]
            top = sorted(members, key=lambda s: -any_[s])
            top_str = ", ".join(f"{s} ({pct(any_[s], n)}%)" for s in top[:3] if any_[s])
            out.append(f"| {g} | {p_any}% | {pct(group_req[g], n)}% | {t} | {lv} | {top_str} |")
        out.append("")

    out.append("## Theo từng kỹ năng / tool\n")
    out.append("| Kỹ năng | Nhóm | % tin nhắc tới | % bắt buộc | % ưu tiên | Tầng (nếu xét riêng) |")
    out.append("|---|---|---|---|---|---|")
    for s, c in sorted(any_.items(), key=lambda x: (-x[1], x[0])):
        p_any = pct(c, n)
        out.append(f"| {s} | {', '.join(skill_to_groups.get(s, [])) or '—'} | {p_any}% | "
                   f"{pct(req[s], n)}% | {pct(pref[s], n)}% | {tier(p_any)[0]} |")
    out.append("")

    out.append("## Chứng chỉ\n")
    any_cert = sum(1 for p in postings if (p.get("certifications") or {}).get("required")
                   or (p.get("certifications") or {}).get("preferred"))
    out.append(f"- Tin có nhắc tới ít nhất 1 chứng chỉ: **{pct(any_cert, n)}%** ({any_cert}/{n})\n")
    if cert_any:
        out.append(f"| Chứng chỉ | % tin nhắc tới | % bắt buộc | Đạt ngưỡng {CERT_THRESHOLD}%? |")
        out.append("|---|---|---|---|")
        for c, cnt in sorted(cert_any.items(), key=lambda x: (-x[1], x[0])):
            p_any = pct(cnt, n)
            out.append(f"| {c} | {p_any}% | {pct(cert_req[c], n)}% | {'✅' if p_any >= CERT_THRESHOLD else '—'} |")
        out.append("")

    ungrouped = [s for s in any_ if s not in skill_to_groups and pct(any_[s], n) >= 15]
    if groups and ungrouped:
        out.append("## Cần xem lại taxonomy\n")
        out.append("Các kỹ năng ≥ 15% chưa thuộc nhóm nào: " + ", ".join(sorted(ungrouped)))
        out.append("")

    if warnings:
        out.append("## Cảnh báo dữ liệu\n")
        out.extend(f"- {w}" for w in warnings)
        out.append("")

    print("\n".join(out))


if __name__ == "__main__":
    main()
