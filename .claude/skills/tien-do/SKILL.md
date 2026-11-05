---
name: tien-do
description: Báo cáo tiến độ học - vị trí hiện tại, % hoàn thành, điểm bài tập, tình trạng chứng chỉ, so với kế hoạch, điểm yếu và 3 việc nên làm tiếp. Dùng khi người học hỏi "tôi đang ở đâu", "tiến độ thế nào", "nên làm gì tiếp", hoặc gõ /tien-do.
argument-hint: "[role-slug]"
---

# Báo cáo tiến độ

1. Đọc `learner/profile.md`, `tracks/<role>/roadmap.md`, `progress.md`. Chưa có profile → đề nghị `/bat-dau`.
2. Tính:
   - Bài học: đã học / miễn / tổng; bài tập: đạt / tổng bắt buộc; module: hoàn thành / tổng; % theo phase.
   - Điểm bài tập trung bình, số lần nộp trung bình (> 2 lần ở module nào → module đó khó với người học).
   - Lịch ôn: số mục đến hạn, số mục quá hạn > 3 ngày.
   - Chứng chỉ: trạng thái, điểm 3 đề thi thử gần nhất, ngày dự kiến thi.
   - Phỏng vấn thử: lần gần nhất, điểm, khuyến nghị.
   - So với kế hoạch: vị trí hiện tại so với tuần dự kiến trong roadmap (dựa trên ngày bắt đầu) → nhanh / đúng / chậm bao nhiêu tuần.
3. Trình bày trong chat (ngắn gọn, có bảng):
   - Vị trí hiện tại & % tổng
   - Bảng phase/module với trạng thái
   - Điểm mạnh (2) và điểm yếu (2–3) có bằng chứng
   - Nếu chậm > 2 tuần: đề xuất điều chỉnh thực tế (tăng giờ, lùi hạn, hoặc giảm phạm vi tầng Nên biết) — không trách
   - **3 việc nên làm tiếp**, theo thứ tự ưu tiên: ôn đến hạn → bài tập đang chờ → bài học tiếp theo / thi thử / phỏng vấn
4. Làm mới mục `## Tóm tắt` trong `progress.md` cho khớp số liệu vừa tính.
5. Nghiên cứu thị trường cũ hơn 6 tháng → nhắc chạy `/nghien-cuu-thi-truong --refresh`.
