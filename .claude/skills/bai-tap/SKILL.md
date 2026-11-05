---
name: bai-tap
description: Giao bài tập thực hành có cấu trúc (đề, rubric khoá, script kiểm tra tự động, thư mục nộp bài). Dùng khi người học nói "cho tôi bài tập", "giao bài", "luyện tập", sau khi học xong bài/module, hoặc gõ /bai-tap.
argument-hint: "[mã bài tập vd 04-ex02]"
---

# Giao bài tập

## Bước 1 — Chọn bài tập
- Đọc `progress.md` và module README hiện tại.
- Có bài tập "đã giao" chưa nộp → nhắc lại đề và đường dẫn, hỏi có muốn bài khác không.
- Không có tham số → bài tập bắt buộc tiếp theo chưa giao của module (theo bảng Bài tập trong module README).
- Kiểm tra người học đã học các bài cần thiết cho bài tập; thiếu thì đề nghị `/hoc` trước.

## Bước 2 — Thiết kế (nếu chưa có)
Thư mục: `tracks/<role>/modules/NN-<skill>/exercises/exNN-<ten>/`

1. **README.md** theo `templates/exercise.md`:
   - Bối cảnh giống công việc thật; nếu có dự án xuyên suốt thì dùng nó.
   - Yêu cầu **đo được**, ràng buộc rõ ràng, độ khó khớp cấp độ cần chứng minh (lab / debug / tư duy / project — xem CLAUDE.md).
   - Bài **debug**: tạo `starter/` chứa hệ thống có lỗi cố ý (2–4 lỗi, từ dễ tới khó). Không để comment lộ lỗi.
   - 2–4 câu hỏi cho `ANSWERS.md` nhắm vào "tại sao", không phải "là gì".
   - Nếu cần cloud: ước tính chi phí, yêu cầu đặt budget alert, mục dọn dẹp.
2. **rubric.md** theo `templates/rubric.md`: tiêu chí cụ thể cho bài này (không chung chung), có mục Lỗi nghiêm trọng.
3. **checks/check.sh** — hợp đồng bắt buộc:
   - Gọi: `bash checks/check.sh <submission_dir>`; exit 0 khi mọi kiểm tra pass, khác 0 khi có fail.
   - In mỗi kiểm tra một dòng `PASS: <mô tả>` hoặc `FAIL: <mô tả> — <gợi ý ngắn>`, cuối cùng `KẾT QUẢ: X/Y`.
   - Không sửa thư mục bài nộp (cần build thì copy sang thư mục tạm `mktemp -d`).
   - Tài nguyên tạo ra (container, network, image, cluster...) đặt tên tiền tố `lc-`, dọn bằng `trap ... EXIT`.
   - Không cần internet nếu tránh được; thiếu công cụ (docker...) → in `FAIL: thiếu <tool>` rõ ràng.
   - Tương thích bash 3.2 (macOS) và Linux.
   - Phần không tự động hoá được (thiết kế, giải thích) để rubric chấm.
4. **Xác minh bài tập giải được** (bắt buộc):
   - Chạy `check.sh` với `starter/` (hoặc thư mục rỗng) → phải FAIL.
   - Tự viết lời giải tham khảo trong thư mục scratch **ngoài repo** → chạy `check.sh` → phải PASS. Sửa check/đề nếu không như kỳ vọng. Xoá lời giải tham khảo sau khi xác minh — **không lưu vào repo**.

## Bước 3 — Khoá rubric & tạo chỗ nộp bài
```bash
shasum -a 256 tracks/<role>/modules/<module>/exercises/<exercise>/rubric.md
mkdir -p submissions/<role>/<module>/<exercise>/feedback
```
- Copy nội dung `starter/` (nếu có) vào `submissions/<role>/<module>/<exercise>/`.
- Tạo `ANSWERS.md` trong thư mục nộp với các câu hỏi đã soạn và chỗ trống để trả lời.
- `progress.md` → bảng Bài tập: trạng thái "đã giao", số lần nộp 0, 12 ký tự đầu SHA-256, ngày giao. Cập nhật Tóm tắt.

## Bước 4 — Hướng dẫn người học
Ngắn gọn:
- Đề ở đâu, làm bài ở đâu (đường dẫn đầy đủ), cần nộp những file gì.
- Lệnh tự kiểm tra (`check.sh`) trước khi nộp.
- Thời gian gợi ý; khi xong gõ `/nop-bai`.
- Nhắc luật gợi ý: hỏi khi bí, mentor sẽ gợi ý theo 3 mức, không đưa lời giải.
- Đọc rubric trước khi làm để biết được chấm thế nào.
