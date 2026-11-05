# Module 09 — Infrastructure as Code với Terraform

- **Tầng**: Quan trọng → nâng L4 · **Cấp độ đích**: L4
- **Giờ ước tính**: 35 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 07-aws-foundations
- **Liên quan chứng chỉ**: terraform-associate (tuỳ chọn)
- **Tài liệu chính hãng gốc**: https://developer.hashicorp.com/terraform/docs · https://registry.terraform.io/
- **Vì sao cần**: IaC 54.9% tin J/M, 63.9% mọi level; Terraform 45.1%, gấp ~5 lần CloudFormation; 61% tin VN.

## Sau module này bạn sẽ làm được
1. Viết Terraform có module, biến, output, remote state + locking
2. Quản lý nhiều môi trường dev/staging/prod
3. Đưa Terraform vào CI/CD với plan review và policy check
4. Xử lý drift, import, refactor an toàn

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | IaC & Terraform workflow | init/plan/apply/destroy, HCL | 1.5 | chưa viết |
| 02 | Provider, resource, data source | Dependency graph, ngầm định vs tường minh | 1.5 | chưa viết |
| 03 | Variable, output, type & custom condition | Kiểu phức hợp, expression, function, validation/precondition/check | 1.5 | chưa viết |
| 04 | State, remote backend & dữ liệu nhạy cảm | S3 backend, locking, state command, sensitive/ephemeral, Vault provider | 2 | chưa viết |
| 05 | Module | Viết & dùng module, Registry, versioning | 2 | chưa viết |
| 06 | count, for_each, dynamic, lifecycle | Tạo tài nguyên lặp, điều khiển vòng đời | 1.5 | chưa viết |
| 07 | Nhiều môi trường & HCP Terraform | Workspace vs thư mục, HCP Terraform (project, variable set, run trigger), Terragrunt tổng quan | 1.5 | chưa viết |
| 08 | Terraform trong CI/CD | fmt, validate, tflint, checkov, plan trên MR | 1.5 | chưa viết |
| 09 | Import, moved, drift & troubleshooting | Đưa hạ tầng có sẵn vào code, refresh-only, moved/removed, TF_LOG | 1.5 | chưa viết |
| 10 | Terraform vs CloudFormation/CDK/Pulumi/OpenTofu | So sánh & chuyển đổi | 1 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-first-infra | VPC + EC2 bằng Terraform | lab | ✅ | L2 |
| ex02-modules-remote-state | Dựng lại hạ tầng TaskFlow bằng module + remote state | lab | ✅ | L3 |
| ex03-state-drift-debug | Sửa state hỏng & drift | debug | ✅ | L3 |
| ex04-terraform-pipeline | Pipeline Terraform: plan trên MR, apply có duyệt, policy check | project | ✅ | L4 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 09`)
- [ ] `terraform destroy` rồi `apply` lại → TaskFlow chạy, không thao tác tay trên console
- [ ] tflint + checkov không lỗi HIGH
