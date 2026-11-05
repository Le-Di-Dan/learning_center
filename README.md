# Repo training của tôi 🎓

Repo này được tạo từ framework **Learning Center**. Mở `claude` ở đây, Claude là mentor của bạn.

## Bắt đầu

```bash
claude
```
> Tôi muốn trở thành DevOps engineer, hãy dạy tôi

## Một buổi học điển hình

1. Mở `claude` — mentor tự nhắc bạn đang ở đâu, có gì cần ôn.
2. `/on-tap` nếu có mục đến hạn (5–10 phút).
3. `/hoc` — học bài tiếp theo, tự chạy lệnh thực hành trên máy.
4. `/bai-tap` khi được gợi ý → làm bài trong thư mục `submissions/...` → `/nop-bai`.
5. Cuối buổi: commit để lưu lịch sử tiến bộ.

## Các lệnh

| Lệnh | Việc |
|---|---|
| `/bat-dau` | Onboarding hoặc thêm role mới |
| `/hoc [bài/chủ đề]` | Học bài tiếp theo hoặc chủ đề cụ thể |
| `/bai-tap` | Nhận bài tập |
| `/nop-bai` | Nộp bài để được chấm |
| `/on-tap [module NN]` | Ôn tập / quiz cuối module |
| `/luyen-thi <cert> [luyen\|thi-thu\|nop\|san-sang\|ket-qua]` | Luyện thi chứng chỉ |
| `/phong-van [mini <phase>\|full\|tieng-anh]` | Phỏng vấn thử |
| `/tien-do` | Xem tiến độ |
| `/nghien-cuu-thi-truong --refresh` | Làm mới dữ liệu thị trường |
| `/lap-roadmap --update` | Điều chỉnh lộ trình |

## Nộp bài thế nào?

```
submissions/<role>/<module>/<bài-tập>/
├── (code / cấu hình của bạn)
├── ANSWERS.md          ← trả lời câu hỏi "tại sao" bằng lời của bạn
└── feedback/
    └── attempt-1.md    ← nhận xét của giám khảo sau mỗi lần nộp
```

- Đề bài & rubric: `tracks/<role>/modules/<module>/exercises/<bài-tập>/`
- Tự kiểm tra trước khi nộp: `bash tracks/<role>/modules/<module>/exercises/<bài-tập>/checks/check.sh submissions/<role>/<module>/<bài-tập>`
- Đạt khi ≥ 80/100 **và** trả lời được vấn đáp.

## Luật chơi

- Mentor **không làm hộ**: khi bí, hỏi — bạn nhận gợi ý theo 3 mức (định hướng → khái niệm → gợi ý cụ thể). Lời giải chỉ được giảng sau khi bạn đạt, hoặc sau 3 lần trượt.
- **Tự giác**: không mở `plan.md` của phỏng vấn hay `key.md` của đề thi thử trước khi làm xong. Bạn chỉ tự lừa chính mình.
- **Không commit secret** (mật khẩu, access key, file `.pem`, kubeconfig...). `.gitignore` đã chặn sẵn các loại phổ biến.
- **Cloud**: luôn đặt budget alert trước khi tạo tài nguyên và dọn dẹp sau mỗi lab.

## Bạn tìm thấy gì ở đâu

| Đường dẫn | Nội dung |
|---|---|
| `learner/profile.md` | Hồ sơ của bạn |
| `tracks/<role>/research/` | Dữ liệu thị trường (mở `postings.jsonl` để tự kiểm tra từng tin tuyển dụng) |
| `tracks/<role>/roadmap.md` | Lộ trình |
| `tracks/<role>/progress.md` | Tiến độ, điểm, lịch ôn |
| `tracks/<role>/glossary.md` | Từ điển thuật ngữ Anh–Việt của bạn |
| `tracks/<role>/modules/` | Bài học & đề bài |
| `tracks/<role>/certifications/` | Exam guide, ngân hàng câu hỏi, đề thi thử |
| `interviews/` | Biên bản & báo cáo phỏng vấn thử |

## Cập nhật framework

Trong thư mục framework: `git pull && ./setup.sh --update <đường-dẫn-repo-này>`, rồi xem `git diff` ở đây và commit.
