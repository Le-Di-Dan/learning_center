# Module 12 — Kubernetes: quản trị cluster (CKA)

- **Tầng**: Cốt lõi · **Cấp độ đích**: L4
- **Giờ ước tính**: 32 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 11-kubernetes-core, 01-linux
- **Liên quan chứng chỉ**: cka (Cluster Architecture, Troubleshooting)
- **Tài liệu chính hãng gốc**: https://kubernetes.io/docs/ · https://github.com/cncf/curriculum
- **Vì sao cần**: Phần quản trị cluster là trọng tâm CKA và các câu hỏi phỏng vấn Middle (upgrade, backup, RBAC, troubleshooting).

## Sau module này bạn sẽ làm được
1. Dựng & nâng cấp cluster bằng kubeadm, backup/restore etcd
2. Cấu hình RBAC, NetworkPolicy
3. Troubleshoot node, control plane, mạng cluster
4. Dựng EKS bằng Terraform

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | Dựng cluster bằng kubeadm | Cài control plane + worker trên VM | 2 | chưa viết |
| 02 | Nâng cấp cluster & quản lý node | kubeadm upgrade, drain/cordon | 1.5 | chưa viết |
| 03 | Backup & restore etcd | etcdctl snapshot | 1.5 | chưa viết |
| 04 | RBAC & ServiceAccount | Role, ClusterRole, binding, authn/authz | 2 | chưa viết |
| 05 | Networking cluster | CNI, NetworkPolicy, CoreDNS | 2 | chưa viết |
| 06 | HA control plane, CRD & operator | Control plane nhiều node, CRD/operator, giao diện mở rộng CNI/CSI/CRI | 1.5 | chưa viết |
| 07 | Troubleshooting cluster | kubelet, static pod, control plane, log | 2 | chưa viết |
| 08 | Helm & Kustomize cho CKA | Cài ứng dụng bằng Helm, overlay bằng Kustomize | 1.5 | chưa viết |
| 09 | EKS & managed Kubernetes | EKS bằng Terraform; so sánh AKS/GKE | 2 | chưa viết |
| 10 | Chiến lược thi CKA | Tốc độ kubectl, lệnh imperative, killer.sh | 1 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-kubeadm-cluster | Dựng cluster kubeadm, upgrade 1 minor version, backup etcd | lab | ✅ | L3 |
| ex02-rbac-netpol | RBAC theo team + NetworkPolicy cô lập namespace | lab | ✅ | L3 |
| ex03-broken-cluster | Sửa cluster hỏng (kubelet, cert, DNS, scheduler) | debug | ✅ | L4 |
| ex04-eks-terraform | EKS bằng Terraform + deploy TaskFlow | project | ✅ | L3 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 12`)
- [ ] Restore etcd thành công từ snapshot
- [ ] Đạt ≥ 85% hai lần trên đề thi thử CKA tự soạn
