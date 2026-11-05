# Nguồn nghiên cứu thị trường — DevOps

- Ngày thu thập: 2026-11-05 · Nên làm mới: **2027-02-05** (3 tháng)
- Tổng: 72 tin (`postings.jsonl`), gộp từ `raw/vn.jsonl` (28), `raw/remote.jsonl` (24), `raw/linkedin-ats.jsonl` (20)

## Nguồn đã dùng
| Nguồn | Số tin | Cách lấy | Ghi chú |
|---|---|---|---|
| itviec.com | 22 | WebFetch trang chi tiết | Ngày đăng tính từ "X days ago" |
| topdev.vn | 4 | WebFetch | Tin đã hết hạn, không có ngày đăng |
| topcv.vn | 2 | Snippet kết quả tìm kiếm | Trang chi tiết trả 403 |
| himalayas.app | 15 | WebFetch, trang lọc `/jobs/countries/vietnam/...` | |
| remotive.com | 4 | Trang chi tiết (JSON-LD JobPosting) | |
| wellfound.com | 4 | WebFetch | Ngày đăng tương đối → null |
| remoteok.com | 1 | API `/api` + trang chi tiết | |
| Workable | 11 | API công khai của ATS | Nhiều công ty VN dùng |
| Greenhouse | 6 | API công khai `boards-api` | |
| Ashby | 2 | API công khai | |
| Lever | 1 | API công khai | |

## Truy vấn đã chạy (chính)
- `site:itviec.com DevOps Engineer`, `site:topcv.vn tuyển dụng DevOps Engineer 2026`, `site:vietnamworks.com DevOps Engineer`
- Himalayas: `/jobs/countries/vietnam/{devops-engineer, site-reliability-engineer, platform-engineer}`
- `site:weworkremotely.com DevOps Engineer remote 2026`
- `site:linkedin.com/jobs/view "DevOps Engineer" Ho Chi Minh` / `Hanoi Vietnam`
- Quét API Greenhouse/Lever/Ashby/Workable theo từ khoá DevOps/SRE/Platform

## Nguồn bị chặn / không dùng được
- LinkedIn: WebFetch và endpoint guest đều bị chặn; tìm kiếm không trả trang `/jobs/view/`.
- TopCV: 403 mọi trang tin. VietnamWorks: nội dung render JS → rỗng. CareerViet: trang > 10MB.
- WeWorkRemotely: 403 trang chi tiết. Indeed/Glassdoor: chỉ trang danh sách.

## Nguồn đối chiếu (không tính vào %)
- https://roadmap.sh/devops — truy cập 2026-11-05
- https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/ — truy cập 2026-11-05
