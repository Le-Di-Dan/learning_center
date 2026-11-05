---
name: phong-van
description: Phỏng vấn thử (mock interview) như nhà tuyển dụng thật - mini interview cuối mỗi phase, full interview loop cuối lộ trình (screening, hands-on troubleshooting, system design, project deep-dive, behavioral, vòng tiếng Anh), chấm độc lập và bổ sung lỗ hổng vào roadmap. Dùng khi người học nói "phỏng vấn thử tôi", "mock interview", hoặc gõ /phong-van.
argument-hint: "[mini <phase> | full | vong <screening|hands-on|system-design|deep-dive|behavioral> | tieng-anh]"
---

# Phỏng vấn thử

Thư mục: `interviews/<role>/<YYYY-MM-DD>-<loai>/` gồm `plan.md`, `transcript.md`, `report.md`, `lab/` (nếu có).

## Bước 1 — Chọn loại
- Không tham số: phase vừa hoàn thành chưa có mini interview → `mini <phase>`; đã xong roadmap → `full`; còn lại → hỏi người học.
- `full` khi roadmap chưa xong → cảnh báo kết quả sẽ phản ánh đúng việc còn thiếu, hỏi có muốn tiếp tục.
- Thời lượng: mini ~30 phút (6–8 câu); full ~2–3 giờ, có thể chia nhiều buổi theo vòng; một vòng ~30–45 phút.

## Bước 2 — Chuẩn bị (người học không thấy)
1. Chạy subagent `interviewer` mode `prepare` với: role, loại, đường dẫn `roadmap.md`, `progress.md`, `research/skills-matrix.md`, các report cũ, đường dẫn `plan.md` cần ghi. Nhắc người học **không mở `plan.md`** trước khi xong.
2. Có vòng hands-on: dựng môi trường lỗi trong `lab/` theo kịch bản của plan (local, tài nguyên tiền tố `lc-`), kiểm tra lỗi tái hiện được. Không để lộ lỗi qua comment hay tên file.

## Bước 3 — Phỏng vấn
Bạn đóng vai interviewer (giới thiệu tên giả, công ty giả, vị trí). Quy tắc:
- Mở đầu: giới thiệu format, thời lượng, mời người học giới thiệu bản thân (full/behavioral).
- **Hỏi từng câu một**, chờ trả lời. Không gợi ý, không dạy, không khen/chê trong lúc phỏng vấn (chỉ phản hồi trung tính như "OK, cảm ơn").
- Dùng follow-up trong plan để đào sâu; nếu người học trả lời hời hợt → hỏi "tại sao", "nếu ... thì sao".
- Người học nói "không biết" → ghi nhận, chuyển câu (như phỏng vấn thật), có thể hỏi "bạn sẽ tìm hiểu thế nào?".
- Hands-on: đưa đường dẫn `lab/`, nêu triệu chứng, giới hạn thời gian; người học tự chẩn đoán trên máy, mô tả suy nghĩ thành lời (think aloud). Kết thúc: chạy kiểm tra xem đã sửa đúng chưa.
- Vòng tiếng Anh: toàn bộ bằng tiếng Anh đơn giản, chuẩn phỏng vấn thật.
- **Sau mỗi câu trả lời**: append ngay vào `transcript.md` (câu hỏi, câu trả lời của người học — giữ nguyên ý, follow-up) để không mất dữ liệu nếu buổi dài.
- Kết thúc: mời người học đặt câu hỏi ngược cho nhà tuyển dụng (một phần đánh giá), rồi thoát vai.

## Bước 4 — Chấm độc lập
Chạy subagent `interviewer` mode `evaluate` với `plan.md`, `transcript.md`, kết quả lab, report cũ, đường dẫn `report.md`.

## Bước 5 — Phản hồi & hành động
1. Trình bày: điểm tổng, khuyến nghị, điểm mạnh, top 3 lỗ hổng, đường dẫn `report.md`. Giờ có thể thảo luận câu trả lời mẫu.
2. `progress.md`: thêm dòng vào bảng Phỏng vấn thử; lỗ hổng → "Điểm yếu cần theo dõi" + Lịch ôn tập.
3. Lỗ hổng lớn (điểm năng lực ≤ 2/5) → đề xuất thêm bài/module bổ sung qua `lap-roadmap --update` (khi người học đồng ý).
4. Dọn tài nguyên lab (`lc-*`).
5. **Job-ready**: 2 lần `full` liên tiếp ≥ 75% (bộ câu hỏi khác nhau) → chúc mừng, ghi vào Tóm tắt, gợi ý bước tiếp: hoàn thiện CV (dự án capstone, chứng chỉ), luyện phỏng vấn tiếng Anh thêm, bắt đầu ứng tuyển.
