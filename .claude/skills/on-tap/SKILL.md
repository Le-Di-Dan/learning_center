---
name: on-tap
description: Ôn tập theo lịch lặp lại ngắt quãng (spaced repetition) các bài đã học, hoặc làm quiz cuối module để hoàn thành module. Dùng khi người học nói "ôn bài", "ôn tập", "kiểm tra cuối module", khi hook báo có mục đến hạn ôn, hoặc gõ /on-tap.
argument-hint: "[module NN]"
---

# Ôn tập

## Chế độ mặc định — Ôn ngắt quãng

1. Đọc bảng **Lịch ôn tập** trong `progress.md`, lấy các dòng có Ngày ôn tiếp ≤ hôm nay. Không có → báo "không có mục đến hạn", đề nghị `/hoc`.
2. Giới hạn ~10 mục/buổi (ưu tiên quá hạn lâu nhất, chủ đề trong "Điểm yếu cần theo dõi").
3. Mỗi mục 1 câu hỏi (mục yếu: 2 câu), đọc lại bài học tương ứng để hỏi đúng nội dung. Đa dạng dạng câu:
   - Giải thích khái niệm bằng lời của mình
   - Viết lệnh/cấu hình cho một yêu cầu
   - Đọc output/log và chẩn đoán
   - Tình huống: "Bạn gặp X, bạn làm gì?"
   - Mục liên quan chứng chỉ: thỉnh thoảng hỏi bằng tiếng Anh theo phong cách đề thi
4. Hỏi **từng câu một**, chờ trả lời, chấm ngay: đúng / đúng một phần / sai + giải thích ngắn + link về bài học.
5. Cập nhật lịch (chuỗi khoảng cách: 1 → 3 → 7 → 14 → 30 → 60 ngày):
   - Đúng → Lần ôn +1, Ngày ôn tiếp = hôm nay + khoảng tiếp theo trong chuỗi
   - Đúng một phần → giữ Lần ôn, Ngày ôn tiếp = hôm nay + khoảng hiện tại
   - Sai → Lần ôn = 0, Ngày ôn tiếp = hôm nay + 1; thêm vào "Điểm yếu cần theo dõi"
   - Đã ôn đúng ở mốc 60 ngày → xoá khỏi lịch (đã nhớ lâu dài)
6. Ghi nhật ký `tracks/<role>/reviews/YYYY-MM-DD.md` (câu hỏi, câu trả lời tóm tắt, kết quả). Cập nhật Tóm tắt.

## Chế độ `module NN` — Quiz cuối module

1. Điều kiện: mọi bài tập bắt buộc của module đã đạt. Chưa → liệt kê bài còn thiếu, dừng.
2. 10 câu phủ toàn bộ bài của module, độ khó theo cấp độ đích (L3/L4: ≥ 4 câu tình huống/chẩn đoán). Module thuộc chứng chỉ: 3–4 câu bằng tiếng Anh theo phong cách đề thi.
3. Hỏi từng câu, **không giải thích ngay** — chấm và giải thích toàn bộ ở cuối (như thi thật).
4. ≥ 80% → module **hoàn thành**: cập nhật bảng Module (điểm quiz, ngày hoàn thành), kiểm tra DoD của module, Tóm tắt chuyển sang module tiếp theo. Chúc mừng!
5. < 80% → chỉ ra bài cần ôn lại, thêm vào Lịch ôn tập (hôm nay + 1), có thể làm lại sau ít nhất 1 ngày với bộ câu hỏi khác.
6. Lưu đề + kết quả vào `tracks/<role>/reviews/YYYY-MM-DD-module-NN.md`.
