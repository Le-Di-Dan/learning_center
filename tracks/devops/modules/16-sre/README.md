# Module 16 — SRE: độ tin cậy & vận hành

- **Tầng**: Nên biết (tăng ở Middle) · **Cấp độ đích**: L2
- **Giờ ước tính**: 20 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 14-observability
- **Liên quan chứng chỉ**: Không
- **Tài liệu chính hãng gốc**: https://sre.google/books/ · https://www.postgresql.org/docs/current/backup.html
- **Vì sao cần**: SRE practices 21.6% J/M → 29.2% mọi level; là thứ phân biệt Middle với Junior khi phỏng vấn. Gộp vận hành PostgreSQL (Database 27.5%).

## Sau module này bạn sẽ làm được
1. Định nghĩa SLI/SLO, error budget cho dịch vụ
2. Điều phối incident, viết postmortem blameless
3. Backup/restore & DR cho PostgreSQL có đo RTO/RPO

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | SRE, SLI, SLO & error budget | Đo độ tin cậy bằng con số | 1.5 | chưa viết |
| 02 | Incident response & on-call | Vai trò, quy trình, giao tiếp khi sự cố | 1.5 | chưa viết |
| 03 | Postmortem & RCA | Blameless, 5 Whys, action item | 1 | chưa viết |
| 04 | HA, backup & DR cho PostgreSQL | RTO/RPO, pg_dump vs PITR, replica | 2 | chưa viết |
| 05 | Load test & chaos engineering | k6, capacity planning, thử lỗi có kiểm soát | 1.5 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-slo-burn-rate | SLO + burn-rate alert cho TaskFlow | lab | ✅ | L2 |
| ex02-game-day | Game day: xử lý sự cố được dàn dựng + postmortem | tư duy | ✅ | L3 |
| ex03-dr-drill | Diễn tập DR PostgreSQL, đo RTO/RPO thực tế | lab | ✅ | L3 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 16`)
- [ ] DR drill: khôi phục DB trong RTO ≤ 30 phút, mất dữ liệu ≤ RPO đã cam kết
