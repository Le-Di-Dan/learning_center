# Module 13 — Helm & GitOps với Argo CD

- **Tầng**: Nên biết · **Cấp độ đích**: L2
- **Giờ ước tính**: 16 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 11-kubernetes-core, 06-cicd
- **Liên quan chứng chỉ**: cka (Helm/Kustomize)
- **Tài liệu chính hãng gốc**: https://helm.sh/docs/ · https://argo-cd.readthedocs.io/
- **Vì sao cần**: GitOps 25.5% (Argo CD 19.6%), Helm 17.6% tin J/M; là cách deploy chuẩn ở công ty dùng Kubernetes trưởng thành.

## Sau module này bạn sẽ làm được
1. Đóng gói app thành Helm chart có values theo môi trường
2. Triển khai tự động theo Git bằng Argo CD

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | Helm cơ bản | Chart, values, release, upgrade/rollback | 1.5 | chưa viết |
| 02 | Viết Helm chart cho TaskFlow | Template, helper, values theo môi trường | 2 | chưa viết |
| 03 | GitOps & Argo CD | Nguyên lý pull-based, cài đặt, Application | 1.5 | chưa viết |
| 04 | Argo CD nâng cao & luồng CI→GitOps | Sync policy, multi-env, app-of-apps, image update | 1.5 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-helm-argocd | Helm chart TaskFlow + Argo CD tự đồng bộ dev/prod | lab | ✅ | L2 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 13`)
- [ ] Merge MR đổi image tag → Argo CD tự deploy trong ≤ 3 phút, không chạy kubectl tay
