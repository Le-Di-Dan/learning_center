# Module 10 — Configuration management với Ansible

- **Tầng**: Nên biết · **Cấp độ đích**: L2
- **Giờ ước tính**: 12 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 01-linux, 04-scripting
- **Liên quan chứng chỉ**: Không
- **Tài liệu chính hãng gốc**: https://docs.ansible.com/
- **Vì sao cần**: Ansible 15.7% tin J/M, 20.8% mọi level; phổ biến ở công ty có server on-premise (ngân hàng, viễn thông VN).

## Sau module này bạn sẽ làm được
1. Viết playbook idempotent, dùng template & handler
2. Đóng gói thành role, kết hợp với Terraform

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | Config management & Ansible | Inventory, ad-hoc command, SSH | 1.5 | chưa viết |
| 02 | Playbook & idempotency | Task, module, chạy lại an toàn | 1.5 | chưa viết |
| 03 | Variable, template, handler | Jinja2, facts, notify | 1.5 | chưa viết |
| 04 | Role & kết hợp Terraform | Cấu trúc role, Galaxy, Terraform → Ansible | 1.5 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-ansible-role | Chuyển script provisioning Phase 1 thành Ansible role | lab | ✅ | L2 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 10`)
- [ ] Chạy playbook 2 lần liên tiếp: lần 2 `changed=0`
