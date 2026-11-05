---
name: nop-bai
description: Nộp và chấm bài tập - gọi giám khảo độc lập (subagent grader) chấm theo rubric đã khoá, rồi vấn đáp để xác nhận người học thật sự hiểu, cập nhật điểm và tiến độ. Dùng khi người học nói "nộp bài", "chấm bài cho tôi", "tôi làm xong rồi", hoặc gõ /nop-bai.
argument-hint: "[mã bài tập vd 04-ex02]"
---

# Nộp & chấm bài

## Bước 1 — Xác định bài & kiểm tra điều kiện
- Bài tập: tham số, hoặc bài "đã giao"/"cần làm lại" gần nhất trong `progress.md`.
- Thư mục `submissions/<role>/<module>/<exercise>/` tồn tại và có bài làm (không chỉ starter nguyên vẹn). `ANSWERS.md` đã trả lời đủ. Thiếu → nói rõ thiếu gì, dừng.
- Số lần nộp N = số file `feedback/attempt-*.md` hiện có + 1.
- Quét nhanh secret (`grep -rIiE "(aws_secret|password\s*=|BEGIN (RSA|OPENSSH) PRIVATE KEY|api[_-]?key)"`): nếu có → cảnh báo ngay, hướng dẫn gỡ và thu hồi, vẫn chấm (rubric sẽ xử lý theo mục Lỗi nghiêm trọng).

## Bước 2 — Chấm độc lập
Chạy subagent `grader` với prompt chứa:
- Đường dẫn thư mục bài tập (`tracks/<role>/modules/<module>/exercises/<exercise>/`)
- Đường dẫn thư mục bài nộp
- N, SHA-256 rubric đầy đủ (tính lại từ 12 ký tự trong progress để đối chiếu: chạy `shasum -a 256` và so tiền tố)
- Đường dẫn các feedback trước

**Không** gửi kèm ý kiến riêng của bạn về bài làm, không gợi ý điểm — để grader chấm độc lập.

## Bước 3 — Thông báo kết quả sơ bộ
Nói cho người học: điểm, check pass bao nhiêu, 2–3 điểm tốt, 2–3 điểm cần sửa quan trọng nhất, đường dẫn `feedback/attempt-N.md`.
- Kết luận sơ bộ `CHƯA ĐẠT` → bỏ qua vấn đáp, sang Bước 5.
- `CHỜ VẤN ĐÁP` → Bước 4.

## Bước 4 — Vấn đáp
- Hỏi lần lượt 3 câu grader đã soạn, **từng câu một**, chờ trả lời. Không gợi ý trong lúc hỏi. Người học trả lời bằng lời của mình, không cần hoàn hảo — so với "ý chính".
- Mỗi câu: đạt / chưa đạt + giải thích ngắn, bổ sung ý còn thiếu.
- ≥ 2/3 đạt → **ĐẠT**. Dưới → **CHƯA ĐẠT (vấn đáp)**: chỉ ra phần hiểu chưa chắc, gợi ý bài cần đọc lại; lần nộp sau chỉ cần vấn đáp lại (không cần sửa code nếu rubric đã ≥ 80).
- Ghi mục "## Vấn đáp" vào `feedback/attempt-N.md` (câu hỏi, tóm tắt câu trả lời, đánh giá) và sửa dòng Kết luận.

## Bước 5 — Cập nhật & bước tiếp
`progress.md` → bảng Bài tập: số lần nộp, điểm cao nhất, trạng thái (đạt / cần làm lại), ngày đạt. Thêm "CHỦ ĐỀ YẾU" từ grader vào "Điểm yếu cần theo dõi" và Lịch ôn tập (ngày ôn tiếp = hôm nay + 1). Cập nhật Tóm tắt.

- **ĐẠT**:
  - Khen cụ thể. Bây giờ được phép thảo luận lời giải tối ưu hơn nếu người học muốn.
  - Đề nghị commit: `git add submissions/<...> && git commit -m "<exercise> lần N: XX điểm - đạt"` (khi người học đồng ý).
  - Mọi bài bắt buộc của module đã đạt → gợi ý quiz cuối module `/on-tap module NN`. Hết phase → mini-project / `/phong-van mini <phase>`. Module thuộc chứng chỉ → nhắc `/luyen-thi`.
- **CHƯA ĐẠT**:
  - Động viên, nhắc rằng sửa theo feedback là cách học hiệu quả nhất.
  - Sau lần trượt thứ 3: giảng lời giải tham khảo từng bước (giải thích vì sao), sau đó giao **bài biến thể** (cùng kỹ năng, bối cảnh khác) qua skill `bai-tap` để xác nhận đã nắm.
