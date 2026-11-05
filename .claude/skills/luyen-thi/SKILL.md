---
name: luyen-thi
description: Luyện thi chứng chỉ quốc tế (AWS, Azure, CKA, RHCSA, CCNA, Terraform...) - luyện theo domain, thi thử đúng format và thời gian thật, đánh giá mức sẵn sàng đi thi, ghi kết quả thi thật. Dùng khi người học nói "luyện thi <chứng chỉ>", "thi thử", "tôi sẵn sàng thi chưa", hoặc gõ /luyen-thi.
argument-hint: "<cert-id> [luyen [domain] | thi-thu [mini|full] | nop | san-sang | ket-qua]"
---

# Luyện thi chứng chỉ

Thư mục: `tracks/<role>/certifications/<cert-id>/`. Không có tham số cert → liệt kê chứng chỉ trong `certifications/plan.md` kèm trạng thái, hỏi người học chọn.

**Luật** (CLAUDE.md 5.6): chỉ câu hỏi tự soạn theo objective chính thức; không dùng/tìm exam dump.

## Chuẩn bị (lần đầu với mỗi cert)
1. `exam-guide.md` chưa có hoặc kiểm tra > 3 tháng → chạy subagent `market-researcher` (mode `certification`) để tạo/cập nhật. Báo người học nếu có phiên bản đề mới.
2. `domain-map.md`: đối chiếu từng objective với bài học trong `progress.md`. Objective chưa học → cảnh báo; đề nghị học trước (hoặc vẫn luyện nhưng báo kết quả sẽ thấp ở domain đó).

## `luyen [domain]` — Luyện theo domain
1. Không chỉ định domain → chọn domain yếu nhất (từ thi thử gần nhất) hoặc domain có tỷ trọng cao chưa luyện.
2. 10 câu, **viết bằng tiếng Anh như đề thật** (format theo exam guide: single/multiple choice, scenario...). Thi thực hành (CKA, RHCSA...): thay bằng 2–3 task lab trên môi trường local có giới hạn thời gian và script kiểm tra.
3. Hỏi từng câu; sau mỗi câu giải thích **bằng tiếng Việt**: vì sao đáp án đúng, vì sao từng đáp án sai sai, từ khoá tiếng Anh cần chú ý trong câu hỏi.
4. Lưu câu hỏi vào `question-bank/<domain-slug>.md` (câu hỏi, đáp án, giải thích, objective, ngày dùng) để không lặp lại và để ôn.

## `thi-thu [mini|full]` — Tạo đề thi thử
- `mini` (mặc định): 20 câu, thời gian tỷ lệ theo đề thật. `full`: đúng số câu & thời gian đề thật.
- Phân bổ câu theo **tỷ trọng domain** trong exam guide. Không trùng câu trong `question-bank/` và các đề trước.
- Tạo `practice-exams/NN-YYYY-MM-DD/`:
  - `exam.md`: hướng dẫn, thời gian cho phép, câu hỏi tiếng Anh (đánh số, có domain ẩn — chỉ ghi trong key).
  - `answers.md`: phiếu trả lời trống (`1: `, `2: `...; nhiều đáp án ghi `A,C`).
  - `key.md`: đáp án + domain + giải thích tiếng Việt. Dòng đầu: "⚠️ KHÔNG MỞ FILE NÀY TRƯỚC KHI NỘP BÀI".
  - Thi thực hành: `tasks.md` + `checks/` thay cho trắc nghiệm.
- Khi người học nói "bắt đầu": ghi giờ bắt đầu vào đầu `exam.md`. Nhắc: điều kiện như thi thật — không tra cứu, không hỏi mentor, làm trong `answers.md`, xong gõ `/luyen-thi <cert-id> nop`.

## `nop` — Chấm đề thi thử
1. Ghi giờ nộp, tính thời gian đã dùng (vượt giờ → vẫn chấm nhưng ghi rõ).
2. So `answers.md` với `key.md` (câu nhiều đáp án: phải đúng hết mới tính điểm). Thi thực hành: chạy checks.
3. Viết `report.md` theo `templates/practice-exam-report.md`: điểm, theo domain, bảng câu sai, **mẫu sai lặp lại**, từ vựng tiếng Anh gây khó.
4. Từ vựng khó → thêm vào `glossary.md`. Câu sai → thêm chủ đề vào Lịch ôn tập; domain < 70% → đề nghị `luyen <domain>`.
5. Chuyển các câu của đề vào `question-bank/`. Cập nhật bảng Chứng chỉ trong `progress.md`.

## `san-sang` — Đánh giá sẵn sàng
- Điều kiện: **3 đề thi thử liên tiếp gần nhất (đều là đề khác nhau, ít nhất 1 đề full) ≥ 85%, không domain nào < 70%**, đã phủ 100% objective trong `domain-map.md`.
- Đạt → "SẴN SÀNG": hướng dẫn đăng ký trên trang chính hãng (link trong exam-guide), phí, hỗ trợ cho người không nói tiếng Anh bản xứ nếu đơn vị cấp có, checklist ngày thi (giấy tờ tuỳ thân, kiểm tra máy nếu thi online, giờ giấc), gợi ý thêm một bộ đề luyện thi thương mại uy tín để đối chiếu độc lập (tuỳ chọn).
- Chưa đạt → nói rõ còn thiếu điều kiện nào, kế hoạch 1–2 tuần cụ thể.

## `ket-qua` — Ghi kết quả thi thật
Hỏi kết quả (đạt/trượt, điểm, điểm theo domain nếu có). Ghi `progress.md` + `exam-result.md`.
- Đạt: chúc mừng; checklist cập nhật CV/LinkedIn (tên chứng chỉ chính xác, mã xác thực/badge); chuyển sang mốc tiếp theo trong plan.
- Trượt: phân tích domain yếu từ score report, lập kế hoạch thi lại (lưu ý chính sách thời gian chờ thi lại trên trang chính hãng).
