# Module 11 — Kubernetes: triển khai ứng dụng

- **Tầng**: Cốt lõi · **Cấp độ đích**: L4
- **Giờ ước tính**: 35 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 05-docker, 02-networking
- **Liên quan chứng chỉ**: cka (Workloads & Scheduling, Services & Networking, Storage)
- **Tài liệu chính hãng gốc**: https://kubernetes.io/docs/
- **Vì sao cần**: Kubernetes 66.7% tin J/M (80% tin VN); CNCF 2025: 82% tổ chức dùng container chạy Kubernetes ở production.

## Sau module này bạn sẽ làm được
1. Deploy app nhiều thành phần lên Kubernetes bằng manifest YAML
2. Cấu hình Service, Ingress, ConfigMap/Secret, storage, probe, HPA
3. Debug CrashLoopBackOff, ImagePullBackOff, Pending một cách có hệ thống

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | Kubernetes là gì & kiến trúc | Control plane, node; dựng cluster kind | 1.5 | chưa viết |
| 02 | Pod & kubectl | Manifest YAML, kubectl get/describe/logs/exec | 1.5 | chưa viết |
| 03 | Deployment & rolling update | ReplicaSet, rollout, rollback | 1.5 | chưa viết |
| 04 | Service & DNS | ClusterIP, NodePort, LoadBalancer, CoreDNS | 1.5 | chưa viết |
| 05 | Ingress & Gateway API | Định tuyến HTTP vào cluster | 1.5 | chưa viết |
| 06 | ConfigMap & Secret | Tách cấu hình khỏi image | 1 | chưa viết |
| 07 | Storage & StatefulSet | Volume, PV, PVC, StorageClass, chạy Postgres | 2 | chưa viết |
| 08 | Resource, probe & autoscaling | requests/limits, liveness/readiness, HPA | 1.5 | chưa viết |
| 09 | Scheduling & workload khác | affinity, taint/toleration, DaemonSet, Job/CronJob | 1.5 | chưa viết |
| 10 | Debug ứng dụng trên Kubernetes | Quy trình chẩn đoán theo trạng thái pod | 2 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-taskflow-on-k8s | Deploy TaskFlow lên kind (Deployment, Service, Ingress, StatefulSet) | lab | ✅ | L2 |
| ex02-probes-hpa | Probe, resource, HPA chịu tải | lab | ✅ | L3 |
| ex03-broken-manifests | Sửa manifest lỗi (CrashLoop, ImagePull, Pending, Service sai selector) | debug | ✅ | L3 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 11`)
- [ ] Rolling update TaskFlow không mất request (đo bằng load test)
- [ ] ex03: sửa đủ 5 lỗi trong ≤ 40 phút
