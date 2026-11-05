---
name: bat-dau
description: Bắt đầu hành trình học một role mới (onboarding). Dùng khi người học nói "Tôi muốn trở thành <role>", "dạy tôi <role>", "tôi muốn chuyển sang backend/devops/cloud...", "bắt đầu học", hoặc gõ /bat-dau. Tạo hồ sơ người học, rồi điều phối nghiên cứu thị trường và lập roadmap.
argument-hint: "[tên role, vd: devops engineer]"
---

# Onboarding người học

Mục tiêu: sau skill này có `learner/profile.md`, `tracks/<role>/research/skills-matrix.md`, `tracks/<role>/roadmap.md`, `tracks/<role>/progress.md`, và người học biết rõ việc cần làm tiếp theo.

## Bước 0 — Kiểm tra trạng thái
- Đọc `learner/profile.md` nếu có.
  - Đã có và `active_track` trùng role được yêu cầu → không onboard lại; chuyển sang skill `tien-do`.
  - Đã có nhưng role khác → hỏi người học: chuyển hẳn sang role mới hay học song song. Thêm slug mới vào `tracks`, đổi `active_track` theo lựa chọn, bỏ qua các câu hỏi hồ sơ đã có (chỉ hỏi những gì khác theo role mới).

## Bước 1 — Xác định role
- Chuẩn hoá thành slug tiếng Anh kebab-case: `devops`, `backend-nodejs`, `cloud-aws`, `data-engineer`...
- Role có nhiều nhánh khác biệt lớn (vd "backend" → Node.js / Java / Go / Python) → hỏi người học chọn, kèm khuyến nghị dựa trên nền tảng hiện có (vd frontend JS → Node.js chuyển đổi nhanh nhất) và ghi chú rằng nghiên cứu thị trường sẽ cho số liệu để quyết định lại nếu cần.

## Bước 2 — Phỏng vấn hồ sơ
Dùng AskUserQuestion (tối đa 4 câu mỗi lần, có khuyến nghị):
1. Thị trường mục tiêu: Việt Nam / Remote quốc tế / Cả hai.
2. Thời gian học mỗi tuần: ~5h / ~10h / ~15h / 20h+.
3. Thời hạn mong muốn: 3 / 6 / 9 / 12 tháng.
4. Level mục tiêu: Junior / Middle.

Lần hỏi thứ hai:
5. Ngân sách thi chứng chỉ: không có / có thể chi lệ phí thi.
6. Cloud: chỉ free tier / có thể chi ít (< 10 USD/tháng).
7. Đọc tiếng Anh kỹ thuật: Yếu / Trung bình / Khá.

Hỏi tự do (một tin nhắn): vị trí hiện tại, số năm kinh nghiệm, công nghệ thành thạo, đã từng học gì cho role mới.

Tự kiểm tra máy (không cần hỏi): `uname -sm`, RAM (`sysctl -n hw.memsize` trên macOS / `free -g` trên Linux), dung lượng trống (`df -h .`), đã có `docker`, `git`, `python3` chưa. Nếu thiếu công cụ cần cho role, ghi chú để hướng dẫn cài ở bài đầu tiên.

## Bước 3 — Ghi hồ sơ
Tạo `learner/profile.md` theo `templates/profile.md` (frontmatter `active_track`, `tracks`, `created`). Đọc lại cho người học xác nhận trong 3–5 dòng tóm tắt.

## Bước 4 — Nghiên cứu thị trường
Thực hiện skill `nghien-cuu-thi-truong`. Trước khi bắt đầu, báo người học: bước này mất vài phút vì phải đọc nhiều tin tuyển dụng thật.

Sau khi xong, trình bày kết quả gọn: bảng tầng kỹ năng + chứng chỉ đạt ngưỡng + 2–3 nhận xét đáng chú ý. Hỏi người học có muốn điều chỉnh gì không (vd đã có kinh nghiệm Azure ở công ty nên muốn chọn Azure thay AWS).

## Bước 5 — Lập roadmap
Thực hiện skill `lap-roadmap`.

## Bước 6 — Khởi tạo & hướng dẫn
- Đảm bảo đã có `tracks/<role>/progress.md` (theo `templates/progress.md`) và `tracks/<role>/glossary.md` (bảng Tiếng Anh | Tiếng Việt | Giải thích | Gặp ở bài).
- Giải thích ngắn cách học hằng ngày:
  1. Mở `claude` trong repo → mentor tự nhắc vị trí hiện tại.
  2. `/on-tap` nếu có mục đến hạn → `/hoc` → `/bai-tap` → làm bài trong `submissions/...` → `/nop-bai`.
  3. `/tien-do` khi muốn xem tổng quan.
- Đề nghị commit: `git add -A && git commit -m "Onboarding <role>: profile, research, roadmap"` (chỉ commit khi người học đồng ý).
- Kết thúc bằng một việc cụ thể: "Gõ `/hoc` để bắt đầu bài đầu tiên: <tên bài>".
