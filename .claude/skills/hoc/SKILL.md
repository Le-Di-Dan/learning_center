---
name: hoc
description: Học bài tiếp theo trong lộ trình, hoặc một bài/chủ đề cụ thể. Nếu bài chưa có thì viết ngay bằng tiếng Việt dựa trên tài liệu chính hãng, rồi dạy tương tác và kiểm tra hiểu bài. Dùng khi người học nói "học tiếp", "bài tiếp theo", "dạy tôi về <chủ đề>", hoặc gõ /hoc.
argument-hint: "[mã bài vd 03-02 | tên chủ đề]"
---

# Học bài

## Bước 1 — Xác định bài
- Đọc `learner/profile.md`, `tracks/<role>/progress.md`, `roadmap.md`.
- Không có tham số → bài "chưa học"/"đang học" đầu tiên của module hiện tại.
- Có tham số → bài tương ứng. Nếu là chủ đề ngoài roadmap: dạy như bài bổ sung, lưu vào `modules/NN-<skill>/lessons/` của module gần nhất và ghi vào progress.
- Còn mục ôn tập đến hạn → nhắc làm `/on-tap` trước (người học có thể bỏ qua).
- Bài trước chưa học (tiên quyết) → cảnh báo, đề nghị học bài trước.
- Có bài tập đang "đã giao" chưa nộp của module → nhắc, nhưng vẫn cho học tiếp nếu người học muốn.

## Bước 2 — Viết bài (nếu file chưa có)
File: `tracks/<role>/modules/NN-<skill>/lessons/NN-<topic>.md`, theo đúng 10 mục của `templates/lesson.md`.

1. **Nghiên cứu nguồn chính hãng**: WebSearch giới hạn domain chính hãng (vd `site:docs.docker.com`, `site:kubernetes.io`, `site:docs.aws.amazon.com`, `site:developer.hashicorp.com`), WebFetch 2–5 trang liên quan. Ghi phiên bản công nghệ hiện hành.
2. **Viết cho người mới** (xem CLAUDE.md mục 1): đi từ tại sao → là gì → làm thế nào; ví dụ đời thường rồi ví dụ kỹ thuật; liên hệ kiến thức người học đã có; sơ đồ Mermaid khi có luồng/kiến trúc.
3. **Thực hành từng bước**: mọi lệnh có output mong đợi và giải thích tham số. Ưu tiên môi trường local miễn phí. Nếu có thể, **chạy thử** trong môi trường an toàn (container tạm `lc-...`, thư mục scratch) để xác minh output; xong thì dọn.
4. **Lỗi thường gặp**: lấy từ docs (troubleshooting) và kinh nghiệm phổ biến.
5. **Đọc tài liệu gốc**: chép nguyên văn 1 đoạn 3–6 câu từ trang docs đã đọc, giải thích từng câu. Độ khó theo mức tiếng Anh trong profile (Yếu: câu ngắn, giải thích từng cụm từ; Khá: đoạn dài hơn, chỉ giải thích cụm khó).
6. **Tự kiểm tra**: 3–5 câu, có câu tình huống; đáp án trong `<details>`.
7. **Nguồn**: bảng link + phiên bản + ngày truy cập.
8. Độ dài vừa 1 buổi (30–90 phút). Chủ đề quá lớn → tách thành nhiều bài, cập nhật module README.
9. Thêm thuật ngữ mới vào `tracks/<role>/glossary.md` (không trùng). Cập nhật cột "Trạng thái file" trong module README.

## Bước 3 — Dạy tương tác
Không chỉ đưa file rồi thôi:
1. Giới thiệu bài trong 3–5 câu: học gì, vì sao, mất bao lâu, đường dẫn file.
2. Đề nghị cách học: người học tự đọc rồi hỏi, **hoặc** mentor đi qua từng phần trong chat. Theo lựa chọn của họ.
3. Khi đi từng phần: giải thích ngắn → yêu cầu người học **tự chạy** lệnh thực hành trên máy họ và dán kết quả → nhận xét output.
4. Trả lời mọi câu hỏi; câu hỏi lạc đề nhưng có giá trị → trả lời ngắn và ghi chú để học sau.

## Bước 4 — Kiểm tra hiểu bài
- Hỏi 3 câu (một câu một lần) **khác** với câu trong mục Tự kiểm tra: 1 khái niệm, 1 tình huống, 1 "chuyện gì xảy ra nếu".
- ≥ 2/3 đúng → bài "đã học". Dưới → giải thích lại phần sai bằng cách khác (ví dụ khác, sơ đồ khác), hỏi lại 1 câu tương tự.

## Bước 5 — Cập nhật & bước tiếp
- `progress.md`: trạng thái bài "đã học", ngày học; thêm dòng vào **Lịch ôn tập** (Lần ôn = 0, Ngày ôn tiếp = hôm nay + 1); cập nhật **Tóm tắt**.
- Bài có bài tập gắn kèm (xem module README) hoặc đây là bài cuối module → gợi ý `/bai-tap`. Ngược lại → gợi ý bài tiếp theo.
- Kết thúc buổi bằng 2–3 dòng tóm tắt điều đã học.
