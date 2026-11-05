# Domain map — Certified Kubernetes Administrator (CKA, curriculum v1.37)

> Đối chiếu từng objective trong `exam-guide.md` với bài học. Mã bài `MM-LL`. CKA là thi thực hành → mỗi objective phải có **lab**, không chỉ đọc.

| Objective | Nội dung | Module/Bài | Trạng thái |
|---|---|---|---|
| 1.1 | Troubleshoot clusters and nodes | 12-07, 01-07 (systemd/journalctl) | đã phân bổ |
| 1.2 | Troubleshoot cluster components | 12-07 | đã phân bổ |
| 1.3 | Monitor cluster and application resource usage | 11-08 (metrics-server, kubectl top), 14-07 | đã phân bổ |
| 1.4 | Manage and evaluate container output streams | 11-02, 11-10 | đã phân bổ |
| 1.5 | Troubleshoot services and networking | 11-04, 11-10, 12-05 | đã phân bổ |
| 2.1 | Manage role based access control (RBAC) | 12-04 | đã phân bổ |
| 2.2 | Prepare underlying infrastructure for installing a Kubernetes cluster | 12-01 | đã phân bổ |
| 2.3 | Create and manage Kubernetes clusters using kubeadm | 12-01 | đã phân bổ |
| 2.4 | Manage the lifecycle of Kubernetes clusters (upgrade, etcd backup/restore, cert renewal) | 12-02, 12-03 | đã phân bổ |
| 2.5 | Implement and configure a highly-available control plane | 12-06 | đã phân bổ |
| 2.6 | Use Helm and Kustomize to install cluster components | 12-08, 13-01 | đã phân bổ |
| 2.7 | Understand extension interfaces (CNI, CSI, CRI, etc.) | 12-06, 05-10 (containerd) | đã phân bổ |
| 2.8 | Understand CRDs, install and configure operators | 12-06 | đã phân bổ |
| 3.1 | Understand connectivity between Pods | 12-05, 11-04 | đã phân bổ |
| 3.2 | Define and enforce Network Policies | 12-05 | đã phân bổ |
| 3.3 | Use ClusterIP, NodePort, LoadBalancer service types and endpoints | 11-04 | đã phân bổ |
| 3.4 | Use the Gateway API to manage Ingress traffic | 11-05 | đã phân bổ |
| 3.5 | Know how to use Ingress controllers and Ingress resources | 11-05 | đã phân bổ |
| 3.6 | Understand and use CoreDNS | 11-04, 12-05 | đã phân bổ |
| 4.1 | Application deployments, rolling update and rollbacks | 11-03 | đã phân bổ |
| 4.2 | Use ConfigMaps and Secrets to configure applications | 11-06 | đã phân bổ |
| 4.3 | Configure workload autoscaling | 11-08 | đã phân bổ |
| 4.4 | Primitives for robust, self-healing deployments | 11-03, 11-07, 11-08, 11-09 | đã phân bổ |
| 4.5 | Configure Pod admission and scheduling (limits, LimitRange, ResourceQuota, affinity, taints, PriorityClass) | 11-08, 11-09 | đã phân bổ |
| 5.1 | Storage classes and dynamic volume provisioning | 11-07 | đã phân bổ |
| 5.2 | Volume types, access modes and reclaim policies | 11-07 | đã phân bổ |
| 5.3 | Manage persistent volumes and persistent volume claims | 11-07 | đã phân bổ |

**Độ phủ**: 27/27 objective (100%). Đã bổ sung bài 12-06 (HA control plane, CRD/operator, CNI/CSI/CRI).

**Lưu ý môi trường lab**: máy 8 GB RAM chạy kind cho module 11 được; lab kubeadm (12-01 → 12-07) nên dựng 2–3 VM nhỏ trên AWS EC2 (dùng xong xoá) vì VM local sẽ thiếu RAM.
