---
name: nghien-cuu-thi-truong
description: Nghiên cứu thị trường việc làm có kiểm chứng cho một role - thu thập tin tuyển dụng thật, thống kê % kỹ năng và chứng chỉ được yêu cầu, phân tầng kỹ năng. Dùng khi onboarding, khi người học hỏi "thị trường đang cần gì", "làm mới nghiên cứu", hoặc gõ /nghien-cuu-thi-truong. Nên làm mới mỗi 3–6 tháng.
argument-hint: "[role-slug] [--refresh]"
---

# Nghiên cứu thị trường

Đầu vào: role (mặc định `active_track`), thị trường + level mục tiêu trong `learner/profile.md`.
Đầu ra trong `tracks/<role>/research/`: `postings.jsonl`, `taxonomy.json`, `skills-matrix.md`, `sources.md`.

Nguyên tắc: **mọi con số phải truy được về tin tuyển dụng có URL**. Không bịa; thiếu dữ liệu thì nói thiếu.

## Bước 1 — Chuẩn bị
- `mkdir -p tracks/<role>/research/raw`
- `--refresh` hoặc dữ liệu cũ > 3 tháng: chuyển `postings.jsonl` cũ thành `postings-YYYY-MM-DD.jsonl` để so sánh xu hướng sau.
- Chọn nguồn theo thị trường:
  - **Việt Nam**: itviec.com, topcv.vn, vietnamworks.com, linkedin.com (location Vietnam), topdev.vn
  - **Remote quốc tế**: linkedin.com, indeed.com, weworkremotely.com, remoteok.com, wellfound.com
  - **Đối chiếu** (không tính vào %): roadmap.sh, Stack Overflow Developer Survey, khảo sát chuyên ngành (CNCF, State of DevOps, JetBrains...)

## Bước 2 — Thu thập song song
Chạy song song 2–3 subagent `market-researcher` (mode `postings`), mỗi agent một nhóm nguồn và **một file output riêng** để không ghi đè nhau:
- `research/raw/<nhom-nguon>.jsonl`
- Mục tiêu tổng ≥ 50 tin (chia đều), ưu tiên level mục tiêu và level kề dưới, đăng trong 6 tháng gần nhất.
- Prompt cho agent phải ghi rõ: mode, role (kèm các tên gọi tương đương, vd "DevOps Engineer", "Site Reliability Engineer", "Platform Engineer" — hỏi người học nếu không rõ có tính SRE/Platform không), thị trường, danh sách nguồn, số tin mục tiêu, đường dẫn output, ngày hôm nay.

Nếu tổng < 30 tin sau lượt đầu: chạy thêm một lượt với nguồn/truy vấn khác. Vẫn thiếu → chấp nhận, ghi rõ ở phần Hạn chế.

## Bước 3 — Gộp & chuẩn hoá
1. Gộp: `cat research/raw/*.jsonl > research/postings.jsonl` (script thống kê tự bỏ dòng trùng URL).
2. Tạo `research/taxonomy.json` dựa trên các tên kỹ năng thực tế xuất hiện:
```json
{
  "aliases": {"k8s": "Kubernetes", "amazon web services": "AWS", "github action": "GitHub Actions"},
  "groups": {
    "Cloud": ["AWS", "Azure", "GCP"],
    "Container": ["Docker", "Podman"],
    "Orchestration": ["Kubernetes", "OpenShift", "ECS"],
    "CI/CD": ["Jenkins", "GitLab CI", "GitHub Actions", "Azure DevOps", "ArgoCD"],
    "IaC": ["Terraform", "CloudFormation", "Pulumi", "Ansible"]
  },
  "cert_aliases": {"aws saa": "AWS Certified Solutions Architect – Associate"}
}
```
   (Ví dụ trên cho DevOps — với role khác hãy tự xây nhóm phù hợp: Language, Framework, Database, Message queue...)
3. Chạy thống kê:
```bash
python3 .claude/scripts/skill-stats.py tracks/<role>/research --levels junior,middle,unknown
```
   (Lọc level theo mục tiêu của người học; chạy thêm một lần không lọc để so sánh.) Nếu output có mục "Cần xem lại taxonomy" → bổ sung `taxonomy.json` rồi chạy lại.

## Bước 4 — Viết skills-matrix.md
Theo `templates/skills-matrix.md`:
- **Kết luận nhanh**: tầng Cốt lõi / Quan trọng / Nên biết theo **nhóm**, mỗi nhóm chọn tool phổ biến nhất (giải thích nếu chọn khác — vd chênh lệch nhỏ mà tool kia hợp hồ sơ người học hơn).
- **Nền tảng bổ sung**: kỹ năng tiên quyết hiếm khi ghi trong tin nhưng bắt buộc (vd DevOps: networking, Git, Bash scripting; Backend: HTTP, SQL cơ bản). Mỗi mục kèm lý do.
- Dán nguyên output của script.
- **Đối chiếu nguồn khác**: WebFetch roadmap.sh và 1–2 khảo sát uy tín; ghi chỗ khớp / lệch.
- **Hạn chế**: cỡ mẫu, nguồn bị chặn, tỷ lệ snippet, sai lệch có thể có.

## Bước 5 — sources.md
Liệt kê: nguồn đã dùng, truy vấn đã chạy, nguồn bị chặn, ngày thu thập, ngày nên làm mới (+3 tháng).

## Bước 6 — Khi làm mới (refresh)
So sánh với lần trước: kỹ năng tăng/giảm > 10 điểm %, kỹ năng mới xuất hiện. Nếu thay đổi ảnh hưởng tới roadmap → đề xuất cập nhật qua skill `lap-roadmap` (không tự sửa roadmap khi người học chưa đồng ý).

## Báo cáo cho người học
Ngắn gọn bằng tiếng Việt: cỡ mẫu, bảng tầng kỹ năng, chứng chỉ đạt ngưỡng 15%, 2–3 phát hiện đáng chú ý, nhắc họ có thể mở `postings.jsonl` để kiểm tra từng URL.
