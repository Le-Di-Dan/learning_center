# Certified Kubernetes Administrator (CKA) — Tóm tắt exam guide

> Nguồn chính hãng: [Trang CKA – Linux Foundation](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/) · [CKA Curriculum v1.37 (PDF, CNCF)](https://github.com/cncf/curriculum/blob/master/CKA_Curriculum_v1.37.pdf) · [FAQ CKA/CKAD/CKS](https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks) · [Important Instructions CKA & CKAD](https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad) · [Resources Allowed](https://docs.linuxfoundation.org/tc-docs/certification/certification-resources-allowed) · Kiểm tra ngày: 2026-11-05
>
> Lưu ý: phí, chính sách và phiên bản Kubernetes thay đổi thường xuyên. **Kiểm tra lại trang chính hãng trước khi đăng ký thi.**

## Thông tin kỳ thi
| Mục | Giá trị |
|---|---|
| Mã đề / phiên bản hiện hành | CKA (không có mã đề dạng số). Môi trường thi chạy **Kubernetes v1.37**; curriculum hiện hành **CKA_Curriculum_v1.37** |
| Phiên bản mới sắp áp dụng | Có khả năng. Kubernetes v1.38 dự kiến phát hành **16/12/2026** (lịch SIG Release). Linux Foundation ghi: môi trường thi được cập nhật lên minor version mới nhất trong khoảng **4–8 tuần** sau khi phát hành → đề có thể chuyển sang v1.38 khoảng cuối 01/2027 – 02/2027 (suy luận, chưa có thông báo chính thức). Domain/tỷ trọng thường không đổi theo minor version, nhưng cần xem lại curriculum PDF khi có bản mới |
| Format | **Performance-based** (thực hành trên dòng lệnh, làm task trên cluster Kubernetes thật), không phải trắc nghiệm |
| Số câu | **15–20 task** |
| Thời lượng | **120 phút** (2 giờ) |
| Điểm đạt | **66%** trở lên |
| Phí thi | **$445** (chỉ thi). Combo: thi + THRIVE-ONE Annual Subscription $625; thi + khoá Kubernetes Fundamentals (LFS258) $645 |
| Lần thi lại | **1 lần thi lại miễn phí** mỗi lần mua (không áp dụng cho bản "-SINGLE"). Có **12 tháng** kể từ ngày đăng ký/mua để thi (kể cả lần thi lại) |
| Simulator đi kèm | **killer.sh: 2 lượt**, mỗi lượt truy cập **36 giờ** kể từ lúc kích hoạt; mỗi lượt 17 câu (theo trang CKA). Không áp dụng cho CKA-SINGLE. Truy cập qua My Portal → Exam Preparation Checklist |
| Ngôn ngữ đề | Tiếng Anh, tiếng Trung giản thể, tiếng Nhật (task mặc định theo ngôn ngữ trình duyệt, đổi được trong lúc thi bằng Language Control) |
| Hình thức | Online proctored (giám thị từ xa qua PSI Secure Browser, có ghi hình/âm thanh/màn hình) |
| Hiệu lực | **2 năm** (chứng chỉ đạt trước 01/04/2024 là 3 năm). Gia hạn bằng cách thi đạt lại trước khi hết hạn. Chương trình CARE: đạt/gia hạn CKS từ 18/06/2026 trở đi sẽ tự kéo dài hạn CKA cho khớp |
| Hỗ trợ người không nói tiếng Anh bản xứ | **Không có** chính sách cộng giờ cho người không nói tiếng Anh bản xứ (không tìm thấy trên trang chính hãng). Chỉ có: (1) chọn đề tiếng Trung/Nhật; (2) tài liệu kubernetes.io được phép mở ở **mọi bản dịch** có sẵn (việc có bản tiếng Việt và mức độ đầy đủ: chưa xác minh). Cộng giờ chỉ dành cho test accommodation vì khuyết tật, cần form + xác nhận chuyên môn, nộp trước ≥ 2 tuần |
| Điều kiện tiên quyết | Không có. Mức độ: Intermediate |
| Kết quả | Gửi email trong vòng 24 giờ sau khi thi |

**Ghi chú về killer.sh:** FAQ chính hãng ghi "two attempts", 36 giờ/lượt, câu hỏi "similar to those on the real exam". Trang CKA (bản tóm tắt khi đọc) có nhắc lượt 2 dùng bộ câu khác, nhưng FAQ không nói điều này → coi là **chưa xác minh**. Mức độ khó của killer.sh so với đề thật: **chưa xác minh** từ nguồn chính hãng.

## Môi trường thi & tài liệu được phép mở

**Tài liệu được mở trong lúc thi** (chỉ qua trình duyệt trong VM thi):
- Kubernetes Documentation: https://kubernetes.io/docs (được dùng ô search của trang, nhưng **không được mở kết quả tìm kiếm bên ngoài**)
- Kubernetes Blog: https://kubernetes.io/blog/
- Helm Documentation: https://helm.sh/docs
- Gateway API Documentation: https://gateway-api.sigs.k8s.io
- Hộp "Quick Reference" trong từng task (link tài liệu cho tool cần dùng)
- Mọi bản dịch của kubernetes.io (khuyến nghị dùng bản tiếng Anh)
- Tài liệu cài sẵn trong distro (`/usr/share/...`), man pages

**Môi trường:**
- Máy gốc tên `base`, **không có** kubectl. Mỗi task ghi rõ host cần `ssh <nodename>`; làm xong thì `exit` về `base`. Không hỗ trợ SSH lồng nhau.
- Trên các host: `kubectl` có sẵn alias `k` + Bash autocompletion, `yq`, `curl`, `wget`, `man`. Dùng `sudo -i` khi cần quyền root.
- Copy/paste trong terminal: `Ctrl+Shift+C` / `Ctrl+Shift+V`. `Ctrl+W` sẽ đóng tab Chrome → dùng `Ctrl+Alt+W`. Phím Insert bị tắt.
- Một màn hình duy nhất, không dùng máy ảo, giấy tờ tuỳ thân có ảnh, tên khớp chính xác với tên đã khai.

## Domain & tỷ trọng
| # | Domain | Tỷ trọng | Số câu ước tính (đề thi thử đầy đủ 17 task) |
|---|---|---|---|
| 1 | Troubleshooting | 30% | 5 |
| 2 | Cluster Architecture, Installation and Configuration | 25% | 4 |
| 3 | Services and Networking (PDF ghi "Servicing and Networking") | 20% | 4 |
| 4 | Workloads and Scheduling | 15% | 3 |
| 5 | Storage | 10% | 1–2 |

> Số câu ước tính là do mentor tự phân bổ theo tỷ trọng, không phải số chính thức.

## Objective chi tiết (dịch & giải thích)

### Domain 1 — Troubleshooting (Xử lý sự cố) — 30%
- **1.1 Troubleshoot clusters and nodes** — Tìm nguyên nhân node `NotReady`, cluster không hoạt động: kiểm tra `kubectl get nodes`/`describe node`, trạng thái `kubelet` (`systemctl status kubelet`, `journalctl -u kubelet`), container runtime, chứng chỉ, tài nguyên đĩa/bộ nhớ.
- **1.2 Troubleshoot cluster components** — Sửa lỗi các thành phần control plane (kube-apiserver, etcd, kube-scheduler, kube-controller-manager) thường chạy dạng static Pod trong `/etc/kubernetes/manifests/`; đọc log, sửa manifest sai (sai cờ, sai đường dẫn cert...).
- **1.3 Monitor cluster and application resource usage** — Theo dõi CPU/RAM của node và Pod (`kubectl top node/pod`, cần metrics-server), tìm Pod tiêu thụ nhiều tài nguyên nhất.
- **1.4 Manage and evaluate container output streams** — Đọc và phân tích log container (stdout/stderr): `kubectl logs` (kể cả `-c`, `--previous`, `-f`), hiểu cơ chế logging của Kubernetes.
- **1.5 Troubleshoot services and networking** — Debug Service không có endpoint (sai selector/port), DNS không phân giải, NetworkPolicy chặn traffic, kube-proxy/CNI lỗi.

### Domain 2 — Cluster Architecture, Installation and Configuration (Kiến trúc, cài đặt & cấu hình cluster) — 25%
- **2.1 Manage role based access control (RBAC)** — Tạo và gán quyền bằng Role/ClusterRole, RoleBinding/ClusterRoleBinding, ServiceAccount; kiểm tra quyền bằng `kubectl auth can-i`.
- **2.2 Prepare underlying infrastructure for installing a Kubernetes cluster** — Chuẩn bị máy trước khi cài: container runtime (containerd), tắt swap hoặc cấu hình phù hợp, kernel module/sysctl (vd `br_netfilter`, `ip_forward`), cài `kubeadm`/`kubelet`/`kubectl`.
- **2.3 Create and manage Kubernetes clusters using kubeadm** — Dựng cluster bằng `kubeadm init`, join worker bằng `kubeadm join`, tạo lại token join.
- **2.4 Manage the lifecycle of Kubernetes clusters** — Nâng cấp version cluster (`kubeadm upgrade plan/apply`, drain/uncordon node), backup và restore etcd (`etcdctl snapshot save/restore`), gia hạn certificate.
- **2.5 Implement and configure a highly-available control plane** — Hiểu và cấu hình control plane nhiều node (HA): stacked etcd vs external etcd, load balancer phía trước API server, `--control-plane-endpoint`.
- **2.6 Use Helm and Kustomize to install cluster components** — Cài thành phần vào cluster bằng Helm chart (`helm repo add`, `helm install/upgrade`, values) và Kustomize (`kubectl apply -k`, overlay/patch).
- **2.7 Understand extension interfaces (CNI, CSI, CRI, etc.)** — Hiểu các "giao diện mở rộng": CNI (Container Network Interface – plugin mạng), CSI (Container Storage Interface – plugin lưu trữ), CRI (Container Runtime Interface – runtime như containerd); biết cài/kiểm tra plugin.
- **2.8 Understand CRDs, install and configure operators** — Hiểu CustomResourceDefinition (tự định nghĩa loại resource mới) và operator (controller tự động hoá vận hành dựa trên CRD); cài và cấu hình một operator.

### Domain 3 — Services and Networking (Service & mạng) — 20%
- **3.1 Understand connectivity between Pods** — Mô hình mạng Kubernetes: mọi Pod có IP riêng, giao tiếp trực tiếp với nhau không cần NAT; vai trò của CNI.
- **3.2 Define and enforce Network Policies** — Viết NetworkPolicy (firewall cấp Pod) cho ingress/egress theo podSelector, namespaceSelector, ipBlock, port.
- **3.3 Use ClusterIP, NodePort, LoadBalancer service types and endpoints** — Tạo và phân biệt các loại Service; hiểu Endpoints/EndpointSlice; expose Deployment.
- **3.4 Use the Gateway API to manage Ingress traffic** — Dùng Gateway API (GatewayClass, Gateway, HTTPRoute) để định tuyến traffic từ ngoài vào — thế hệ kế tiếp của Ingress.
- **3.5 Know how to use Ingress controllers and Ingress resources** — Tạo Ingress resource (rule theo host/path, TLS) và hiểu rằng cần Ingress controller để Ingress hoạt động.
- **3.6 Understand and use CoreDNS** — DNS nội bộ cluster: tên `<service>.<namespace>.svc.cluster.local`, cấu hình CoreDNS qua ConfigMap, debug phân giải DNS.

### Domain 4 — Workloads and Scheduling (Workload & lập lịch) — 15%
- **4.1 Understand application deployments and how to perform rolling update and rollbacks** — Deployment, cập nhật image theo kiểu rolling update, xem lịch sử và rollback (`kubectl rollout status/history/undo`).
- **4.2 Use ConfigMaps and Secrets to configure applications** — Tạo ConfigMap/Secret và đưa vào Pod qua biến môi trường hoặc volume.
- **4.3 Configure workload autoscaling** — Tự động scale: HorizontalPodAutoscaler (HPA) theo CPU/RAM (`kubectl autoscale`), cần requests + metrics-server.
- **4.4 Understand the primitives used to create robust, self-healing, application deployments** — Các thành phần giúp ứng dụng tự phục hồi: ReplicaSet/Deployment, DaemonSet, StatefulSet, liveness/readiness/startup probe, restartPolicy.
- **4.5 Configure Pod admission and scheduling (limits, node affinity, etc.)** — Kiểm soát Pod chạy ở đâu và dùng bao nhiêu tài nguyên: requests/limits, LimitRange, ResourceQuota, nodeSelector, node affinity, taints/tolerations, PriorityClass.

### Domain 5 — Storage (Lưu trữ) — 10%
- **5.1 Implement storage classes and dynamic volume provisioning** — Tạo StorageClass và dùng dynamic provisioning (PVC tự sinh PV), StorageClass mặc định.
- **5.2 Configure volume types, access modes and reclaim policies** — Các loại volume (emptyDir, hostPath, PVC...), access mode (ReadWriteOnce, ReadOnlyMany, ReadWriteMany, ReadWriteOncePod), reclaim policy (Retain, Delete).
- **5.3 Manage persistent volumes and persistent volume claims** — Tạo PV/PVC, bind, mount vào Pod, mở rộng dung lượng PVC, debug PVC `Pending`.

## Phong cách câu hỏi
- **100% thực hành trên terminal**, không có câu trắc nghiệm. Mỗi task mô tả một yêu cầu (tạo/sửa/sửa lỗi resource) và chỉ định host cần `ssh` vào. Hệ thống chấm tự động bằng cách kiểm tra trạng thái cluster/file sau khi thi.
- 15–20 task trong 120 phút → trung bình **6–8 phút/task**. Áp lực thời gian rất lớn: cần gõ `kubectl` nhanh, dùng `--dry-run=client -o yaml` để sinh YAML, tra docs nhanh.
- Task có trọng số khác nhau (không công bố chi tiết — chưa xác minh). Nên làm task dễ trước, task khó để sau. Việc có chấm điểm từng phần (partial credit) hay không: **chưa xác minh** trên trang chính hãng.
- Đề được viết bằng tiếng Anh kỹ thuật ngắn gọn (hoặc tiếng Trung/Nhật). Phải đọc kỹ tên namespace, tên resource, đường dẫn file output được yêu cầu — sai tên là mất điểm.
- Phải đảm bảo đang ở đúng host trước mỗi task (kiểm tra prompt terminal).

## Tài liệu ôn chính hãng
- **CKA Curriculum v1.37** (CNCF): https://github.com/cncf/curriculum
- **Trang CKA** (Linux Foundation): https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/
- **FAQ CKA/CKAD/CKS**: https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks
- **Important Instructions: CKA and CKAD** (mô tả môi trường thi): https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad
- **Resources Allowed** (tài liệu được mở khi thi): https://docs.linuxfoundation.org/tc-docs/certification/certification-resources-allowed
- **killer.sh simulator** — 2 lượt đi kèm khi mua đề (dùng ở giai đoạn cuối, khi đã ôn xong).
- **Khoá miễn phí Introduction to Kubernetes (LFS158)**: https://training.linuxfoundation.org/training/introduction-to-kubernetes/ — miễn phí, tự học 15–20 giờ, tiếng Anh, truy cập 90 ngày.
- **Khoá trả phí Kubernetes Fundamentals (LFS258)** — có trong combo $645 (tuỳ chọn).
- **Tài liệu Kubernetes chính thức**: https://kubernetes.io/docs — đặc biệt mục *Tasks* (hướng dẫn từng bước, chính là tài liệu được phép mở khi thi; nên luyện tra cứu nhanh tại đây). Kèm Helm docs (https://helm.sh/docs) và Gateway API docs (https://gateway-api.sigs.k8s.io).

## Nguồn & ngày truy cập (2026-11-05)
- https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/ — phí, format, killer.sh, hiệu lực, domain, v1.37
- https://github.com/cncf/curriculum — file `CKA_Curriculum_v1.37.pdf` (đã đọc nội dung PDF)
- https://docs.linuxfoundation.org/tc-docs/certification/faq-cka-ckad-cks — điểm đạt 66%, thi lại, killer.sh, hiệu lực 2 năm, ngôn ngữ, CARE
- https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad — 15–20 task, môi trường thi, v1.37
- https://docs.linuxfoundation.org/tc-docs/certification/certification-resources-allowed — tài liệu được phép
- https://training.linuxfoundation.org/about/policies/ — 1 lần thi lại/lần mua, 12 tháng eligibility, hoàn tiền
- https://docs.linuxfoundation.org/tc-docs/certification/lf-handbook2/exam-preparation-checklist — test accommodation, killer.sh
- https://kubernetes.io/releases/ — v1.37.1 (15/09/2026) là minor mới nhất
- https://github.com/kubernetes/sig-release/tree/master/releases/release-1.38 — v1.38.0 dự kiến 16/12/2026
