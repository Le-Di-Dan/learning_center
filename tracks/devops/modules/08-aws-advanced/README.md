# Module 08 — AWS nâng cao & kiến trúc

- **Tầng**: Cốt lõi · **Cấp độ đích**: L4
- **Giờ ước tính**: 30 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 07-aws-foundations
- **Liên quan chứng chỉ**: aws-saa (thiết kế kiến trúc)
- **Tài liệu chính hãng gốc**: https://docs.aws.amazon.com/ · https://aws.amazon.com/architecture/well-architected/
- **Vì sao cần**: Bổ sung phần kiến trúc, container & serverless mà tin Middle hỏi nhiều; phủ objective còn lại của chứng chỉ AWS.

## Sau module này bạn sẽ làm được
1. Triển khai container lên ECS Fargate từ CI bằng OIDC (không access key)
2. Thiết kế kiến trúc HA/DR theo Well-Architected, ước tính chi phí
3. Dùng các dịch vụ serverless & messaging cơ bản

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | ECR & ECS Fargate | Chạy container trên AWS không quản lý server | 2 | chưa viết |
| 02 | Serverless & messaging | Lambda, API Gateway, SQS/SNS, EventBridge | 2 | chưa viết |
| 03 | Well-Architected & HA/DR | 6 trụ cột, chiến lược DR, RTO/RPO | 2 | chưa viết |
| 04 | Bảo mật nâng cao | KMS, Secrets Manager, WAF, GuardDuty | 1.5 | chưa viết |
| 05 | Multi-account & governance | Organizations, SCP, Control Tower (tổng quan) | 1.5 | chưa viết |
| 06 | Tối ưu chi phí | Mô hình giá, Savings Plans, Spot, tagging, Cost Explorer, Budgets | 1.5 | chưa viết |
| 07 | Chọn database phù hợp | Aurora, DynamoDB, Redshift, ElastiCache — khi nào dùng gì | 2 | chưa viết |
| 08 | Storage nâng cao & di chuyển dữ liệu | EFS, FSx, Storage Gateway, AWS Backup, DataSync, Snow Family | 1.5 | chưa viết |
| 09 | Mạng quy mô lớn & hybrid | Transit Gateway, VPN, Direct Connect, PrivateLink, Global Accelerator | 1.5 | chưa viết |
| 10 | Thu nạp & phân tích dữ liệu | Kinesis, Glue, Athena, EMR, Lake Formation (mức kiến trúc) | 1.5 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-ecs-fargate-oidc | CI deploy TaskFlow lên ECS Fargate qua OIDC | lab | ✅ | L3 |
| ex02-architecture-doc | Viết tài liệu kiến trúc HA/DR + ước tính chi phí | tư duy | ✅ | L4 |
| ex03-serverless-worker | Worker serverless xử lý job qua SQS | lab | ✅ | L2 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 08`)
- [ ] Pipeline deploy ECS không dùng access key dài hạn
- [ ] Tài liệu kiến trúc được grader chấm ≥ 80 (có trade-off rõ ràng)
