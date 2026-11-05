# Module 07 — AWS nền tảng

- **Tầng**: Cốt lõi · **Cấp độ đích**: L4
- **Giờ ước tính**: 45 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 02-networking, 05-docker
- **Liên quan chứng chỉ**: aws-saa (nhiều domain)
- **Tài liệu chính hãng gốc**: https://docs.aws.amazon.com/ · https://docs.aws.amazon.com/wellarchitected/
- **Vì sao cần**: AWS có trong 68.6% tin J/M (75% tin VN) — cloud phổ biến nhất ở cả hai thị trường.

## Sau module này bạn sẽ làm được
1. Thiết lập tài khoản an toàn (MFA, budget alert, IAM Identity Center)
2. Thiết kế VPC nhiều tầng, IAM least privilege
3. Triển khai web app HA: ALB + Auto Scaling + RDS + S3/CloudFront
4. Giám sát bằng CloudWatch, audit bằng CloudTrail

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | Cloud, AWS & tài khoản an toàn | Region/AZ, mô hình trách nhiệm chung; MFA, budget alert | 2 | chưa viết |
| 02 | IAM chuyên sâu | User, role, policy, least privilege, IAM Identity Center | 2 | chưa viết |
| 03 | VPC (1): subnet, route, gateway | Subnet public/private, IGW, NAT | 2 | chưa viết |
| 04 | VPC (2): bảo mật & kết nối | Security group vs NACL, endpoint, peering, flow logs | 2 | chưa viết |
| 05 | EC2 & EBS | Instance type, AMI, user data, SSM Session Manager | 2 | chưa viết |
| 06 | Load balancing & Auto Scaling | ALB, target group, ASG, scaling policy | 2 | chưa viết |
| 07 | S3 & CloudFront | Bucket policy, lifecycle; host frontend Vue qua CloudFront | 2 | chưa viết |
| 08 | Route 53 & ACM | DNS, routing policy, certificate TLS | 1.5 | chưa viết |
| 09 | RDS & ElastiCache | Database managed, Multi-AZ, backup, read replica | 2 | chưa viết |
| 10 | CloudWatch & CloudTrail | Metric, log, alarm, audit trail | 1.5 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-secure-account | Tài khoản an toàn + IAM least privilege + budget alert | lab | ✅ | L2 |
| ex02-three-tier-vpc | VPC 3 tầng, truy cập private bằng SSM | lab | ✅ | L3 |
| ex03-deploy-taskflow-aws | Triển khai TaskFlow HA trên AWS (ALB/ASG/RDS/CloudFront) | lab | ✅ | L3 |
| ex04-vpc-debug | Sửa lỗi kết nối trong VPC (SG, NACL, route, NAT) | debug | ✅ | L4 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 07`)
- [ ] TaskFlow sống sót khi terminate 1 instance (ALB vẫn trả 200)
- [ ] Dọn sạch tài nguyên sau mỗi lab (kiểm bằng script)
