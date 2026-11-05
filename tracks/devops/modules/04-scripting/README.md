# Module 04 — Scripting: Bash & Python

- **Tầng**: Cốt lõi · **Cấp độ đích**: L4
- **Giờ ước tính**: 40 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 01-linux, 03-git
- **Liên quan chứng chỉ**: Không
- **Tài liệu chính hãng gốc**: https://www.gnu.org/software/bash/manual/ · https://docs.python.org/3/ · https://www.shellcheck.net/
- **Vì sao cần**: Nhóm Scripting 76.5% tin J/M (Python 60.8%, Bash 52.9%). Tự động hoá là trái tim của DevOps.

## Sau module này bạn sẽ làm được
1. Viết Bash script an toàn (strict mode, trap, shellcheck sạch)
2. Xử lý text/log bằng grep/sed/awk/jq
3. Viết CLI tool Python có tham số, logging, gọi API, test bằng pytest
4. Chọn đúng công cụ (Bash/Python) cho từng bài toán

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | Bash cơ bản | Biến, quoting, exit code, $?, chuỗi lệnh | 1.5 | chưa viết |
| 02 | Bash: điều kiện, vòng lặp, hàm | if/case/for/while, function, tham số | 1.5 | chưa viết |
| 03 | Bash script an toàn | set -euo pipefail, trap, getopts, shellcheck | 1.5 | chưa viết |
| 04 | Xử lý text: grep, sed, awk, jq | Phân tích log & JSON từ dòng lệnh | 2 | chưa viết |
| 05 | cron & tác vụ định kỳ | crontab, systemd timer, log rotate | 1 | chưa viết |
| 06 | Python cho DevOps: môi trường & cấu trúc | venv/uv, cấu trúc script, argparse | 1.5 | chưa viết |
| 07 | Python: file, JSON/YAML, subprocess | Đọc/ghi cấu hình, gọi lệnh hệ thống an toàn | 1.5 | chưa viết |
| 08 | Python gọi HTTP API | requests, timeout, retry, xử lý lỗi | 1.5 | chưa viết |
| 09 | CLI tool chuẩn: logging & test | logging, pytest, exit code, đóng gói | 2 | chưa viết |
| 10 | Bash, Python hay Node.js? | Tiêu chí chọn công cụ; so sánh với Node.js bạn đã biết | 1 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-backup-script | Bash backup có rotate + cron + log | lab | ✅ | L2 |
| ex02-healthcheck-cli | Python CLI kiểm tra nhiều endpoint, xuất JSON, exit code chuẩn | lab | ✅ | L3 |
| ex03-broken-scripts | Sửa script lỗi (quoting, pipefail, race) | debug | ✅ | L3 |
| ex04-log-analyzer | Thiết kế & viết tool phân tích access log Nginx có test | project | ✅ | L4 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 04`)
- [ ] shellcheck không cảnh báo trên mọi script nộp
- [ ] ex04 có ≥ 5 test pytest pass, xử lý file 100MB < 30 giây
