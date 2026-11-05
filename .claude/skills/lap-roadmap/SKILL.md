---
name: lap-roadmap
description: Lập hoặc cập nhật lộ trình học chi tiết (phase, module, bài học, cấp độ đích, Definition of Done, giờ ước tính, mốc chứng chỉ, capstone) từ kết quả nghiên cứu thị trường và hồ sơ người học. Dùng sau nghiên cứu thị trường, khi người học muốn "điều chỉnh lộ trình", hoặc gõ /lap-roadmap.
argument-hint: "[role-slug] [--update]"
---

# Lập roadmap

Đầu vào: `learner/profile.md`, `tracks/<role>/research/skills-matrix.md`.
Đầu ra: `roadmap.md`, `certifications/plan.md`, `certifications/<cert-id>/{exam-guide.md, domain-map.md}`, `modules/NN-<skill>/README.md`, `progress.md`.

## Bước 1 — Danh sách kỹ năng
Từ `skills-matrix.md`: kỹ năng theo tầng (Cốt lõi L4, Quan trọng L3, Nên biết L2) + nền tảng bổ sung. Trong nhóm có nhiều lựa chọn chỉ chọn **1 tool chính** để học sâu; các tool khác cùng nhóm nhắc tới trong 1 bài "so sánh & chuyển đổi".

## Bước 2 — Chứng chỉ
1. Lấy danh sách chứng chỉ ≥ 15% trong `skills-matrix.md` + chứng chỉ de-facto của kỹ năng Cốt lõi.
2. Với mỗi ứng viên, chạy subagent `market-researcher` (mode `certification`, song song) ghi `certifications/<cert-id>/exam-guide.md`. Loại chứng chỉ đã ngừng/không còn tồn tại.
3. Chọn & xếp thứ tự theo: % tin nhắc tới → liên quan tới role → chi phí (đối chiếu ngân sách trong profile) → điều kiện tiên quyết (Associate trước Professional). Ghi `certifications/plan.md` theo `templates/cert-plan.md`, có cả mục "Đã cân nhắc nhưng không chọn".

## Bước 3 — Kiểm tra đầu vào (miễn học)
Với kỹ năng nền tảng mà hồ sơ cho thấy người học có thể đã biết (vd frontend → Git, HTTP, JavaScript): làm quiz nhanh 5 câu/kỹ năng trong chat, từng câu một, có câu thực hành nhỏ. ≥ 80% → đánh dấu **miễn** (vẫn giữ 1 bài tập xác nhận nếu kỹ năng đó có trong chứng chỉ). Ghi vào bảng "Miễn học" của roadmap.

## Bước 4 — Thiết kế lộ trình
- Sắp xếp module theo **phụ thuộc kiến thức** (cái gì cần trước thì học trước). Ví dụ DevOps: Linux → Networking → Git & Scripting → Docker → CI/CD → Cloud → IaC → Kubernetes → Observability → Security.
- Chia 3–5 **Phase**; cuối mỗi phase: 1 mini-project tích hợp + mini interview.
- Mỗi module: cấp độ đích, 4–10 bài học (mỗi bài 1–2 giờ), bài tập bắt buộc đủ để **chứng minh** cấp độ đích:
  - L2: lab có hướng dẫn · L3: thêm bài debug + bài không hướng dẫn từng bước · L4: thêm bài thiết kế/tình huống production
- **Definition of Done đo được** cho mỗi module (con số, lệnh kiểm tra, điều kiện pass).
- Module thuộc chứng chỉ: bài học phải phủ **100% objective** trong exam guide → viết `certifications/<cert-id>/domain-map.md` (bảng Objective | Module/Bài | Trạng thái) và thêm bài nếu thiếu. Đặt mốc "thi <cert>" ngay sau nhóm module tương ứng.
- **Dự án xuyên suốt**: chọn 1 app mẫu gần với người học (vd frontend Vue + API nhỏ) làm đối tượng triển khai qua các module, để cuối cùng thành capstone đưa vào CV.
- **Giờ & lịch**: cộng giờ ước tính (bài học + bài tập + ôn tập ~20%), chia theo giờ/tuần trong profile → tuần bắt đầu/kết thúc mỗi module. Nếu vượt thời hạn mong muốn: nói thẳng, đưa 2 phương án (tăng giờ/tuần hoặc giảm phạm vi tầng Nên biết).

## Bước 5 — Ghi file
- `roadmap.md` theo `templates/roadmap.md` (có sơ đồ Mermaid).
- `modules/NN-<skill>/README.md` theo `templates/module.md` — chỉ danh sách bài học (tên + mục tiêu 1 dòng), **chưa viết nội dung bài** (bài được viết khi học tới, qua skill `hoc`).
- `progress.md` theo `templates/progress.md`: liệt kê toàn bộ module, bài học (trạng thái "chưa học" hoặc "miễn"), chứng chỉ; điền mục Tóm tắt.

## Bước 6 — Trình bày & xác nhận
Tóm tắt cho người học: số phase/module, tổng giờ, ngày dự kiến xong, các mốc chứng chỉ, capstone. Hỏi có muốn điều chỉnh không. Mọi điều chỉnh sau này ghi vào bảng "Lịch sử điều chỉnh" của roadmap.

## Chế độ --update
Dùng khi có nghiên cứu mới, sau mock interview phát hiện lỗ hổng, hoặc người học muốn đổi. Không xoá module đã học; thêm module/bài bổ sung hoặc đổi thứ tự phần chưa học; cập nhật progress.md và Lịch sử điều chỉnh.
