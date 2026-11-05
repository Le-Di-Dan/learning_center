# Module 15 — DevSecOps

- **Tầng**: Quan trọng · **Cấp độ đích**: L3
- **Giờ ước tính**: 20 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 06-cicd, 11-kubernetes-core, 07-aws-foundations
- **Liên quan chứng chỉ**: cka (một phần RBAC/security)
- **Tài liệu chính hãng gốc**: https://owasp.org/ · https://kubernetes.io/docs/concepts/security/ · https://docs.aws.amazon.com/security/
- **Vì sao cần**: Security/DevSecOps 37.3% tin J/M, 44.4% mọi level (IAM, secrets management dẫn đầu).

## Sau module này bạn sẽ làm được
1. Quản lý secret đúng cách (không hardcode)
2. Thêm security gate vào pipeline (SAST, scan image, SBOM)
3. Hardening workload Kubernetes và tài khoản cloud

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | DevSecOps & shift-left | Threat model đơn giản, mô hình rủi ro | 1.5 | chưa viết |
| 02 | Quản lý secret | Vault / AWS Secrets Manager / External Secrets | 2 | chưa viết |
| 03 | Bảo mật chuỗi cung ứng phần mềm | SAST, dependency & image scan, SBOM, ký image | 2 | chưa viết |
| 04 | Bảo mật Kubernetes | Pod Security Standards, Kyverno, RBAC review | 1.5 | chưa viết |
| 05 | Bảo mật cloud | IAM review, CIS benchmark, GuardDuty | 1.5 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-security-gates | Thêm secret scan, SAST, Trivy, SBOM vào pipeline | lab | ✅ | L3 |
| ex02-harden-workload | Audit & sửa deployment Kubernetes không an toàn | debug | ✅ | L3 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 15`)
- [ ] Pipeline chặn merge khi có secret hoặc lỗ hổng CRITICAL
- [ ] Không còn secret dạng plain text trong repo/manifest
