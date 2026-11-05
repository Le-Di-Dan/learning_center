# Ma trận kỹ năng thị trường — DevOps Engineer

> Thị trường: Việt Nam + Remote quốc tế · Level: Junior / Middle (có bảng so sánh tất cả level) · Ngày thu thập: 2026-11-05 · Làm mới tiếp theo: 2027-02-05
> Dữ liệu gốc: `postings.jsonl` (72 tin, mở URL từng tin để tự kiểm chứng) · Bảng số liệu sinh bởi `.claude/scripts/skill-stats.py` với `taxonomy.json`
> Tên role được tính: DevOps Engineer, SRE, Platform Engineer, Cloud/DevOps Engineer.

## Kết luận nhanh

Phân tầng theo **mẫu Junior/Middle (51 tin)** — đúng level mục tiêu. Cột cuối là số liệu khi tính cả Senior/Lead (72 tin) để thấy "đích đến" của job lương cao.

| Tầng | Nhóm kỹ năng | % tin (J/M) | Tool chọn học sâu | % tin của tool (J/M) | % nhóm (mọi level) |
|---|---|---|---|---|---|
| **Cốt lõi → L4** | CI/CD | 84.3% | **GitLab CI** (+ Jenkins, GitHub Actions ở mức chuyển đổi) | 35.3% | 80.6% |
| | Scripting/Programming | 76.5% | **Python + Bash** | 60.8% / 52.9% | 72.2% |
| | Cloud | 74.5% | **AWS** | 68.6% | 76.4% |
| | Orchestration | 70.6% | **Kubernetes** (EKS khi lên cloud) | 66.7% | 76.4% |
| | OS | 68.6% | **Linux** | 68.6% | 68.1% |
| | Monitoring/Observability | 64.7% | **Prometheus + Grafana** | 39.2% / 33.3% | 62.5% |
| **Quan trọng → L3** | Container | 56.9% | **Docker** | 49.0% | 56.9% |
| | IaC | 54.9% | **Terraform** | 45.1% | 63.9% ⬆ Cốt lõi |
| | Networking | 51.0% | Networking nền tảng + AWS VPC | 43.1% | 61.1% ⬆ Cốt lõi |
| | Logging | 37.3% | **ELK/EFK** (Loki ở mức so sánh) | 19.6% | 31.9% |
| | Security/DevSecOps | 37.3% | IAM, secrets management, image scanning | 15.7% | 44.4% |
| **Nên biết → L2** | GitOps | 25.5% | **Argo CD** | 19.6% | 29.2% |
| | Config management | 21.6% | **Ansible** | 15.7% | 25.0% |
| | SRE practices | 21.6% | Incident response, SLI/SLO, HA/DR | 11.8% | 29.2% |
| | K8s packaging | 17.6% | **Helm** | 17.6% | 19.4% |
| | Database | 27.5% | PostgreSQL (vận hành cơ bản: backup, HA) | 11.8% | 29.2% |
| | Version control | 27.5% | Git — xem "Nền tảng bổ sung" | 25.5% | 23.6% |
| Bỏ qua (< 15%) | Messaging, Cost/FinOps, AI tooling, Service mesh | 5.9–11.8% | Chỉ nhắc qua trong bài liên quan | | |

**Khuyến nghị nâng cấp độ đích** (do người học nhắm job chất lượng cao, level Junior+ → Middle):
- **Docker → L4**: là tiền đề bắt buộc của Kubernetes + CI/CD; thực tế mọi tin có Kubernetes đều ngầm yêu cầu Docker thành thạo.
- **Terraform → L4** và **Networking → L4**: ở mẫu mọi level cả hai đã vượt 60% (Cốt lõi); tin Middle/Senior hỏi sâu (state, module, VPC design, troubleshooting DNS/TLS).

**Nền tảng bổ sung** (ít ghi trong tin nhưng bắt buộc phải có):
- **Git (L3)** — chỉ 25% tin ghi, vì nhà tuyển dụng mặc định ứng viên biết. Mọi CI/CD, IaC, GitOps đều xoay quanh Git (branch, merge request, tag, hook).
- **Networking nền tảng (TCP/IP, DNS, HTTP/TLS, subnet/CIDR)** — tiền đề cho Cloud VPC, Kubernetes networking, debug sự cố. Trong tin thường gộp chung "networking fundamentals".
- **HTTP & kiến trúc web app (frontend/backend/database)** — DevOps triển khai ứng dụng, cần hiểu app chạy thế nào. Người học có lợi thế ở phía frontend.
- **YAML/JSON** — ngôn ngữ cấu hình của Kubernetes, CI/CD, Ansible.

**Chứng chỉ**: không chứng chỉ cụ thể nào đạt ngưỡng 15% khi đếm riêng lẻ, vì tin thường ghi chung chung. Gộp theo họ:
- Tin có nhắc chứng chỉ **có tên AWS** (kể cả "AWS/Azure/GCP certified"): **19.6%** (J/M), 19.4% (mọi level) → **đạt ngưỡng** → chọn chứng chỉ AWS (cụ thể chọn mã nào: quyết định ở `certifications/plan.md`).
- Chứng chỉ Kubernetes (CKA/CKAD/CKS): 5.9% (J/M), 8.3% (mọi level) — **không đạt** ngưỡng 15%, nhưng Kubernetes là kỹ năng **Cốt lõi** và CKA là chuẩn de-facto (thi thực hành) → **đưa vào lộ trình**.
- Terraform Associate: 0 tin nhắc tới. IaC chỉ là Quan trọng ở J/M → không bắt buộc; cân nhắc làm chứng chỉ phụ.
- Chỉ 23.5% tin J/M nhắc tới bất kỳ chứng chỉ nào và chỉ 1 tin bắt buộc → chứng chỉ là **điểm cộng giúp lọc CV**, không thay được project thực tế.

## Cách lựa chọn tool trong mỗi nhóm

- **Cloud → AWS**: 68.6% tin J/M, gấp đôi Azure (31.4%) và GCP (27.5%); dẫn đầu ở cả VN (75%) và quốc tế (64%). Khái niệm (IAM, VPC, compute, storage) chuyển sang Azure/GCP khá dễ.
- **CI/CD → GitLab CI**: ba tool sát nhau (GitLab CI 35.3%, Jenkins 33.3%, GitHub Actions 27.5%). Chọn GitLab CI vì dẫn đầu và rất phổ biến ở công ty VN (tự host được). Module CI/CD sẽ có bài **Jenkins** (phổ biến ở ngân hàng/doanh nghiệp VN) và **GitHub Actions** (phổ biến ở tin quốc tế + tiện làm portfolio công khai). Tư duy pipeline giống nhau; chuyển đổi chủ yếu là cú pháp.
- **Orchestration → Kubernetes**: 66.7%, vượt xa ECS (9.8%). Học Kubernetes "thuần" (kind local) trước, rồi EKS khi lên cloud.
- **Scripting → Python + Bash**: Python 60.8%, Bash 52.9%; Bash là công cụ hằng ngày trên Linux, Python cho automation phức tạp. **Go** 19.6% J/M nhưng **39% ở tin quốc tế** → "Nên biết", để ở phần mở rộng cuối lộ trình nếu nhắm remote.
- **Monitoring → Prometheus + Grafana**: cặp đi cùng nhau, chuẩn của hệ sinh thái Kubernetes. CloudWatch (17.6%) học trong module AWS.
- **IaC → Terraform**: 45.1%, gấp ~5 lần CloudFormation (9.8%); dùng được cho mọi cloud.
- **Logging → ELK/EFK**: 19.6%, phổ biến nhất trong nhóm. Loki học ở mức so sánh vì hay đi cùng Grafana.
- **GitOps → Argo CD** (19.6%) hơn hẳn Flux (2.8%).

## Phát hiện đáng chú ý
- **VN và quốc tế khác nhau ở vài điểm**: VN chuộng Jenkins (41%), Terraform (61%), Kubernetes (80%); quốc tế chuộng Go (39%) và GitHub Actions (29%). Cả hai đều có AWS + Kubernetes + Linux + Python ở top.
- **AI đang vào JD**: ~10% tin (mọi level) nhắc dùng AI coding agent/AI tools trong vận hành (VNG, MB Life, Papaya...). Chưa đủ ngưỡng, nhưng nên tập dùng AI có kiểm chứng trong lúc học.
- **SRE practices** (incident response, SLO, postmortem) tăng rõ ở tin Middle/Senior (21.6% → 29.2%) — đây là thứ phân biệt Middle với Junior khi phỏng vấn.

---

# Số liệu chi tiết — mẫu Junior/Middle (output nguyên văn của script)

## Mẫu dữ liệu

- Số tin tuyển dụng phân tích: **51** (lọc level: intern, junior, middle, unknown)
- Theo nguồn: itviec: 18, himalayas: 9, workable: 8, greenhouse: 4, topdev: 4, remotive: 3, wellfound: 2, lever: 1, ashby: 1, topcv: 1
- Theo level: middle: 37, junior: 10, unknown: 3, intern: 1
- Bằng chứng: page: 50, snippet: 1 (page = đã đọc trang gốc, snippet = chỉ thấy qua kết quả tìm kiếm)

## Theo nhóm kỹ năng

| Nhóm | % tin nhắc tới | % bắt buộc | Tầng | Cấp độ đích | Tool phổ biến nhất trong nhóm |
|---|---|---|---|---|---|
| CI/CD | 84.3% | 74.5% | Cốt lõi | L4 | CI/CD (54.9%), GitLab CI (35.3%), Jenkins (33.3%) |
| Scripting/Programming | 76.5% | 72.5% | Cốt lõi | L4 | Python (60.8%), Bash (52.9%), Go (19.6%) |
| Cloud | 74.5% | 62.7% | Cốt lõi | L4 | AWS (68.6%), Azure (31.4%), GCP (27.5%) |
| Orchestration | 70.6% | 64.7% | Cốt lõi | L4 | Kubernetes (66.7%), EKS (15.7%), ECS (9.8%) |
| OS | 68.6% | 68.6% | Cốt lõi | L4 | Linux (68.6%), Windows Server (9.8%), Windows (2.0%) |
| Monitoring/Observability | 64.7% | 54.9% | Cốt lõi | L4 | Prometheus (39.2%), Grafana (33.3%), Monitoring (19.6%) |
| Container | 56.9% | 52.9% | Quan trọng | L3 | Docker (49.0%), Containers (7.8%), Podman (2.0%) |
| IaC | 54.9% | 47.1% | Quan trọng | L3 | Terraform (45.1%), IaC (chung chung) (11.8%), CloudFormation (9.8%) |
| Networking | 51.0% | 49.0% | Quan trọng | L3 | Networking (43.1%), VPC (11.8%), Load balancing (9.8%) |
| Logging | 37.3% | 27.5% | Quan trọng | L3 | ELK (19.6%), Logging (9.8%), Loki (5.9%) |
| Security/DevSecOps | 37.3% | 27.5% | Quan trọng | L3 | IAM (15.7%), Cloud security (7.8%), SonarQube (7.8%) |
| Version control | 27.5% | 25.5% | Nên biết | L2 | Git (25.5%), GitHub (3.9%) |
| Database | 27.5% | 19.6% | Nên biết | L2 | PostgreSQL (11.8%), MySQL (7.8%), Redis (7.8%) |
| GitOps | 25.5% | 17.6% | Nên biết | L2 | Argo CD (19.6%), GitOps (15.7%) |
| Config management | 21.6% | 15.7% | Nên biết | L2 | Ansible (15.7%), Chef (3.9%), Configuration management (3.9%) |
| SRE practices | 21.6% | 17.6% | Nên biết | L2 | Incident response (11.8%), High availability / DR (9.8%), SLI/SLO (5.9%) |
| K8s packaging | 17.6% | 11.8% | Nên biết | L2 | Helm (17.6%), Kustomize (2.0%) |
| Cost/FinOps | 11.8% | 7.8% | Bỏ qua | - | FinOps (7.8%), Cloud cost optimization (2.0%), AWS cost optimization (2.0%) |
| AI tooling | 7.8% | 3.9% | Bỏ qua | - | AI coding tools (7.8%) |
| Service mesh | 5.9% | 0.0% | Bỏ qua | - | Service mesh (5.9%), Istio (2.0%), Cilium (2.0%) |
| Messaging | 5.9% | 0.0% | Bỏ qua | - | Kafka (3.9%), AWS SQS (2.0%) |

## Theo từng kỹ năng / tool

| Kỹ năng | Nhóm | % tin nhắc tới | % bắt buộc | % ưu tiên | Tầng (nếu xét riêng) |
|---|---|---|---|---|---|
| AWS | Cloud | 68.6% | 62.7% | 5.9% | Cốt lõi |
| Linux | OS | 68.6% | 68.6% | 0.0% | Cốt lõi |
| Kubernetes | Orchestration | 66.7% | 56.9% | 9.8% | Cốt lõi |
| Python | Scripting/Programming | 60.8% | 58.8% | 2.0% | Cốt lõi |
| CI/CD | CI/CD | 54.9% | 52.9% | 2.0% | Quan trọng |
| Bash | Scripting/Programming | 52.9% | 49.0% | 3.9% | Quan trọng |
| Docker | Container | 49.0% | 45.1% | 3.9% | Quan trọng |
| Terraform | IaC | 45.1% | 39.2% | 5.9% | Quan trọng |
| Networking | Networking, Networking | 43.1% | 41.2% | 2.0% | Quan trọng |
| Prometheus | Monitoring/Observability | 39.2% | 31.4% | 7.8% | Quan trọng |
| GitLab CI | CI/CD | 35.3% | 31.4% | 3.9% | Quan trọng |
| Grafana | Monitoring/Observability | 33.3% | 25.5% | 7.8% | Quan trọng |
| Jenkins | CI/CD | 33.3% | 27.5% | 5.9% | Quan trọng |
| Azure | Cloud | 31.4% | 19.6% | 11.8% | Quan trọng |
| GCP | Cloud | 27.5% | 19.6% | 7.8% | Nên biết |
| GitHub Actions | CI/CD | 27.5% | 25.5% | 2.0% | Nên biết |
| Git | Version control | 25.5% | 23.5% | 2.0% | Nên biết |
| Argo CD | GitOps | 19.6% | 13.7% | 5.9% | Nên biết |
| ELK | Logging | 19.6% | 15.7% | 3.9% | Nên biết |
| Go | Scripting/Programming | 19.6% | 17.6% | 2.0% | Nên biết |
| Monitoring | Monitoring/Observability | 19.6% | 17.6% | 2.0% | Nên biết |
| CloudWatch | Monitoring/Observability | 17.6% | 15.7% | 2.0% | Nên biết |
| Helm | K8s packaging | 17.6% | 11.8% | 5.9% | Nên biết |
| Ansible | Config management | 15.7% | 11.8% | 3.9% | Nên biết |
| EKS | Orchestration | 15.7% | 13.7% | 2.0% | Nên biết |
| GitOps | GitOps | 15.7% | 9.8% | 5.9% | Nên biết |
| IAM | Security/DevSecOps | 15.7% | 13.7% | 2.0% | Nên biết |
| Azure DevOps | CI/CD | 11.8% | 7.8% | 3.9% | Bỏ qua |
| IaC (chung chung) | IaC | 11.8% | 9.8% | 2.0% | Bỏ qua |
| Incident response | SRE practices | 11.8% | 9.8% | 2.0% | Bỏ qua |
| Microservices | — | 11.8% | 5.9% | 5.9% | Bỏ qua |
| PostgreSQL | Database | 11.8% | 7.8% | 3.9% | Bỏ qua |
| VPC | Networking | 11.8% | 11.8% | 0.0% | Bỏ qua |
| CloudFormation | IaC | 9.8% | 7.8% | 2.0% | Bỏ qua |
| EC2 | — | 9.8% | 9.8% | 0.0% | Bỏ qua |
| ECS | Orchestration | 9.8% | 9.8% | 0.0% | Bỏ qua |
| High availability / DR | SRE practices | 9.8% | 7.8% | 2.0% | Bỏ qua |
| Lambda | — | 9.8% | 9.8% | 0.0% | Bỏ qua |
| Load balancing | Networking | 9.8% | 9.8% | 0.0% | Bỏ qua |
| Logging | Logging | 9.8% | 7.8% | 2.0% | Bỏ qua |
| PowerShell | Scripting/Programming | 9.8% | 7.8% | 2.0% | Bỏ qua |
| S3 | — | 9.8% | 9.8% | 0.0% | Bỏ qua |
| Windows Server | OS | 9.8% | 7.8% | 2.0% | Bỏ qua |
| AI coding tools | AI tooling | 7.8% | 3.9% | 3.9% | Bỏ qua |
| Cloud security | Security/DevSecOps | 7.8% | 7.8% | 0.0% | Bỏ qua |
| Containers | Container | 7.8% | 7.8% | 0.0% | Bỏ qua |
| FinOps | Cost/FinOps | 7.8% | 3.9% | 3.9% | Bỏ qua |
| Java | Scripting/Programming | 7.8% | 5.9% | 2.0% | Bỏ qua |
| MongoDB | Database | 7.8% | 3.9% | 3.9% | Bỏ qua |
| MySQL | Database | 7.8% | 5.9% | 2.0% | Bỏ qua |
| Nginx | Networking | 7.8% | 5.9% | 2.0% | Bỏ qua |
| OpenTelemetry | Monitoring/Observability | 7.8% | 5.9% | 2.0% | Bỏ qua |
| Redis | Database | 7.8% | 3.9% | 3.9% | Bỏ qua |
| SonarQube | Security/DevSecOps | 7.8% | 2.0% | 5.9% | Bỏ qua |
| AKS | Orchestration | 5.9% | 3.9% | 2.0% | Bỏ qua |
| AWS CodePipeline | CI/CD | 5.9% | 3.9% | 2.0% | Bỏ qua |
| Agile | — | 5.9% | 3.9% | 2.0% | Bỏ qua |
| Bitbucket | CI/CD | 5.9% | 5.9% | 0.0% | Bỏ qua |
| DNS | Networking | 5.9% | 5.9% | 0.0% | Bỏ qua |
| Databases | Database | 5.9% | 5.9% | 0.0% | Bỏ qua |
| Datadog | Monitoring/Observability | 5.9% | 3.9% | 2.0% | Bỏ qua |
| DevSecOps | Security/DevSecOps | 5.9% | 2.0% | 3.9% | Bỏ qua |
| Firewall | Networking | 5.9% | 5.9% | 0.0% | Bỏ qua |
| JavaScript | Scripting/Programming | 5.9% | 3.9% | 2.0% | Bỏ qua |
| Loki | Monitoring/Observability, Logging | 5.9% | 3.9% | 2.0% | Bỏ qua |
| Nexus | — | 5.9% | 3.9% | 2.0% | Bỏ qua |
| Node.js | Scripting/Programming | 5.9% | 2.0% | 3.9% | Bỏ qua |
| Pulumi | IaC | 5.9% | 3.9% | 2.0% | Bỏ qua |
| RDS | — | 5.9% | 5.9% | 0.0% | Bỏ qua |
| SLI/SLO | SRE practices | 5.9% | 5.9% | 0.0% | Bỏ qua |
| Secrets management | Security/DevSecOps | 5.9% | 3.9% | 2.0% | Bỏ qua |
| Security | Security/DevSecOps | 5.9% | 5.9% | 0.0% | Bỏ qua |
| Serverless | — | 5.9% | 3.9% | 2.0% | Bỏ qua |
| Service mesh | Service mesh | 5.9% | 0.0% | 5.9% | Bỏ qua |
| Supply chain security | Security/DevSecOps | 5.9% | 3.9% | 2.0% | Bỏ qua |
| TypeScript | Scripting/Programming | 5.9% | 3.9% | 2.0% | Bỏ qua |
| AWS CDK | IaC | 3.9% | 3.9% | 0.0% | Bỏ qua |
| AWS Landing Zone | — | 3.9% | 0.0% | 3.9% | Bỏ qua |
| Apache | — | 3.9% | 3.9% | 0.0% | Bỏ qua |
| Automation | — | 3.9% | 3.9% | 0.0% | Bỏ qua |
| Backup | — | 3.9% | 3.9% | 0.0% | Bỏ qua |
| Bicep | IaC | 3.9% | 2.0% | 2.0% | Bỏ qua |
| Caching | — | 3.9% | 2.0% | 2.0% | Bỏ qua |
| Checkov | Security/DevSecOps | 3.9% | 0.0% | 3.9% | Bỏ qua |
| Chef | Config management | 3.9% | 2.0% | 2.0% | Bỏ qua |
| ClickHouse | — | 3.9% | 2.0% | 2.0% | Bỏ qua |
| Cloud migration | — | 3.9% | 2.0% | 2.0% | Bỏ qua |
| Cloud migration (on-prem -> cloud) | — | 3.9% | 0.0% | 3.9% | Bỏ qua |
| Configuration management | Config management | 3.9% | 2.0% | 2.0% | Bỏ qua |
| Distributed systems | — | 3.9% | 3.9% | 0.0% | Bỏ qua |
| GPU workloads | — | 3.9% | 0.0% | 3.9% | Bỏ qua |
| GitHub | Version control | 3.9% | 3.9% | 0.0% | Bỏ qua |
| Harbor | — | 3.9% | 2.0% | 2.0% | Bỏ qua |
| HashiCorp Vault | Security/DevSecOps | 3.9% | 0.0% | 3.9% | Bỏ qua |
| IIS | — | 3.9% | 3.9% | 0.0% | Bỏ qua |
| Kafka | Messaging | 3.9% | 0.0% | 3.9% | Bỏ qua |
| Observability | Monitoring/Observability | 3.9% | 3.9% | 0.0% | Bỏ qua |
| Open source contributions | — | 3.9% | 0.0% | 3.9% | Bỏ qua |
| OpenShift | Orchestration | 3.9% | 3.9% | 0.0% | Bỏ qua |
| OpenStack | Cloud | 3.9% | 2.0% | 2.0% | Bỏ qua |
| Oracle | Database | 3.9% | 2.0% | 2.0% | Bỏ qua |
| RAG | — | 3.9% | 0.0% | 3.9% | Bỏ qua |
| React | — | 3.9% | 2.0% | 2.0% | Bỏ qua |
| SQL Server | Database | 3.9% | 2.0% | 2.0% | Bỏ qua |
| Snyk | Security/DevSecOps | 3.9% | 2.0% | 2.0% | Bỏ qua |
| TLS | Networking | 3.9% | 3.9% | 0.0% | Bỏ qua |
| Tomcat | — | 3.9% | 3.9% | 0.0% | Bỏ qua |
| Trivy | Security/DevSecOps | 3.9% | 2.0% | 2.0% | Bỏ qua |
| Troubleshooting | — | 3.9% | 3.9% | 0.0% | Bỏ qua |
| Unit testing | — | 3.9% | 2.0% | 2.0% | Bỏ qua |
| VMware | — | 3.9% | 3.9% | 0.0% | Bỏ qua |
| WebLogic | — | 3.9% | 2.0% | 2.0% | Bỏ qua |
| WireGuard | — | 3.9% | 3.9% | 0.0% | Bỏ qua |
| .NET | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| A/B testing | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| AI agent frameworks | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AI/Big Data platform | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AI/ML architecture | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AIOps | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| API integration | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| APIs | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| APM | Monitoring/Observability | 2.0% | 2.0% | 0.0% | Bỏ qua |
| ARM templates | IaC | 2.0% | 2.0% | 0.0% | Bỏ qua |
| AWS ALB | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| AWS Compute Optimizer | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AWS Control Tower | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AWS Cost Explorer | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AWS ELB | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AWS EventBridge | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AWS GuardDuty | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AWS SQS | Messaging | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AWS WAF | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| AWS cost optimization | Cost/FinOps | 2.0% | 2.0% | 0.0% | Bỏ qua |
| AWS multi-account | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Air-gapped environments | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Alertmanager | Monitoring/Observability | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Alibaba Cloud | Cloud | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Alibaba Cloud CloudMonitor | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Apache Airflow | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Apache HTTP Server | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| App Store Connect | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Application servers | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Automated testing | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Azure Container Apps | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Azure Monitor | Monitoring/Observability | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Banking/financial services | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Bare metal | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Benchmarking/Performance testing | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Blockchain/P2P | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Blue-green deployment | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Branching strategies | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| C# | Scripting/Programming | 2.0% | 2.0% | 0.0% | Bỏ qua |
| CDN | Networking | 2.0% | 2.0% | 0.0% | Bỏ qua |
| CIS Benchmarks | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Ceph | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Cilium | Service mesh | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Cloud | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Cloud Run | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Cloud computing | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Cloud cost optimization | Cost/FinOps | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Cloud fundamentals | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Cloud-native | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Cloudflare | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Cloudflare Pages/Workers | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Code review | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| CodeQL | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Container Registry | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Container registry | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Container scanning | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| DAST | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| DORA metrics | SRE practices | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Database tuning | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Debugging | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Docker Registry | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| DynamoDB | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| E2E/integration testing in CI/CD | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| EAS | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| ESB/API | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Ethereum/Blockchain | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Expo | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| FPT Cloud | Cloud | 2.0% | 2.0% | 0.0% | Bỏ qua |
| GCC (Government Commercial Cloud) | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| GKE | Orchestration | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Generative AI/LLM basics | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Gitleaks | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Google Play Console | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Grafana Alloy | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Grafana Faro | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Greenplum | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| GuardDuty | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| HPA/Autoscaling | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| HTTP | Networking | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Hadoop | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| High-scale systems | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Hybrid cloud | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| IBM Cloud Paks | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| IBM MQ | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| IM8 | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| ISO 27001 | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| IaC scanning | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Internal Developer Platform | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Istio | Service mesh | 2.0% | 0.0% | 2.0% | Bỏ qua |
| JVM tuning | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Kubernetes networking (CNI, Ingress, DNS) | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Kubernetes operators | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Kustomize | K8s packaging | 2.0% | 2.0% | 0.0% | Bỏ qua |
| LLM API integration | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| LLM infrastructure | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| LLMOps | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Log analysis | Logging | 2.0% | 0.0% | 2.0% | Bỏ qua |
| MCP servers | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| MLOps | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Machine images | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Memcached | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Metrics | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| NIST | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| NIST SSDF | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Network programming | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Network security | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| New Relic | Monitoring/Observability | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Next.js | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| NoSQL | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| OTA updates | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| OWASP | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| OWASP SAMM | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| OWASP Top 10 | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| OWASP ZAP | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Observability platform development | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| On-prem to AWS migration | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| PHP | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Patching | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Performance testing | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Podman | Container | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Pre-sales | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Private cloud | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| PromQL | Monitoring/Observability | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Public cloud | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Puppet | Config management | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Pyroscope | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| React Native | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Release management | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Rust | Scripting/Programming | 2.0% | 0.0% | 2.0% | Bỏ qua |
| SAST | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| SBOM | Security/DevSecOps | 2.0% | 0.0% | 2.0% | Bỏ qua |
| SC TRM / BNM RMiT compliance | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| SCA | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| SHIP-HATS | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| SOC 2 | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| SQL | Database | 2.0% | 0.0% | 2.0% | Bỏ qua |
| SQL/NoSQL | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| SQLite | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| SRE | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| SSH hardening | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| SSH key management | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| SSO/SAML | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Scrum | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Secret scanning | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Secure SDLC | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Security assessment / penetration testing | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Security scanning | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Self-hosting tools | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Semgrep | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Sentry | Monitoring/Observability | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Serverless Framework | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Site24x7 | Monitoring/Observability | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Software engineering background | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Splunk | Logging | 2.0% | 2.0% | 0.0% | Bỏ qua |
| StarRocks | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Supabase | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Temenos T24 | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Tempo | Monitoring/Observability | 2.0% | 2.0% | 0.0% | Bỏ qua |
| TensorRT-LLM | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Terragrunt | IaC | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Trino | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Triton | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| VPN | Networking | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Vector database | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Vector databases | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Vertica | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| VictoriaLogs | Logging | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Viettel Cloud | Cloud | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Virtual machines | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Virtualization | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Vue | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Vulnerability remediation | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Web servers | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| WebSphere | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Windows | OS | 2.0% | 0.0% | 2.0% | Bỏ qua |
| WordPress | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| Workflow orchestration | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| YAML | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Zabbix | Monitoring/Observability | 2.0% | 2.0% | 0.0% | Bỏ qua |
| Zipkin | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| commercetools Frontend (Frontastic) | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| eBPF | — | 2.0% | 2.0% | 0.0% | Bỏ qua |
| libp2p | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| tfsec | — | 2.0% | 0.0% | 2.0% | Bỏ qua |
| vLLM | — | 2.0% | 0.0% | 2.0% | Bỏ qua |

## Chứng chỉ

- Tin có nhắc tới ít nhất 1 chứng chỉ: **23.5%** (12/51)

| Chứng chỉ | % tin nhắc tới | % bắt buộc | Đạt ngưỡng 15%? |
|---|---|---|---|
| Cloud (bất kỳ nhà cung cấp) | 13.7% | 2.0% | — |
| AWS (bất kỳ chứng chỉ AWS) | 9.8% | 2.0% | — |
| CKA | 3.9% | 0.0% | — |
| CKAD | 3.9% | 0.0% | — |
| Azure (bất kỳ) | 2.0% | 0.0% | — |
| CKS | 2.0% | 0.0% | — |
| DevOps certification | 2.0% | 0.0% | — |
| Linux certification | 2.0% | 0.0% | — |
| Red Hat EX280 | 2.0% | 0.0% | — |
| Security+ | 2.0% | 0.0% | — |


---

# Số liệu so sánh — tất cả level (chỉ bảng theo nhóm và chứng chỉ)

## Mẫu dữ liệu

- Số tin tuyển dụng phân tích: **72**
- Theo nguồn: itviec: 22, himalayas: 15, workable: 11, greenhouse: 6, remotive: 4, wellfound: 4, topdev: 4, ashby: 2, topcv: 2, lever: 1, remoteok: 1
- Theo level: middle: 37, senior: 20, junior: 10, unknown: 3, intern: 1, lead: 1
- Bằng chứng: page: 70, snippet: 2 (page = đã đọc trang gốc, snippet = chỉ thấy qua kết quả tìm kiếm)

## Theo nhóm kỹ năng

| Nhóm | % tin nhắc tới | % bắt buộc | Tầng | Cấp độ đích | Tool phổ biến nhất trong nhóm |
|---|---|---|---|---|---|
| CI/CD | 80.6% | 73.6% | Cốt lõi | L4 | CI/CD (48.6%), GitLab CI (31.9%), Jenkins (29.2%) |
| Cloud | 76.4% | 66.7% | Cốt lõi | L4 | AWS (70.8%), Azure (33.3%), GCP (30.6%) |
| Orchestration | 76.4% | 72.2% | Cốt lõi | L4 | Kubernetes (73.6%), EKS (13.9%), ECS (6.9%) |
| Scripting/Programming | 72.2% | 66.7% | Cốt lõi | L4 | Python (59.7%), Bash (50.0%), Go (25.0%) |
| OS | 68.1% | 66.7% | Cốt lõi | L4 | Linux (68.1%), Windows Server (6.9%), Windows (1.4%) |
| IaC | 63.9% | 58.3% | Cốt lõi | L4 | Terraform (51.4%), IaC (chung chung) (15.3%), CloudFormation (8.3%) |
| Monitoring/Observability | 62.5% | 55.6% | Cốt lõi | L4 | Prometheus (37.5%), Grafana (30.6%), CloudWatch (16.7%) |
| Networking | 61.1% | 59.7% | Cốt lõi | L4 | Networking (47.2%), Load balancing (12.5%), VPC (12.5%) |
| Container | 56.9% | 52.8% | Quan trọng | L3 | Docker (50.0%), Containers (6.9%), Podman (1.4%) |
| Security/DevSecOps | 44.4% | 31.9% | Quan trọng | L3 | IAM (19.4%), Secrets management (15.3%), HashiCorp Vault (6.9%) |
| Logging | 31.9% | 25.0% | Quan trọng | L3 | ELK (19.4%), Logging (6.9%), Loki (4.2%) |
| GitOps | 29.2% | 23.6% | Nên biết | L2 | GitOps (20.8%), Argo CD (20.8%), Flux (2.8%) |
| Database | 29.2% | 23.6% | Nên biết | L2 | PostgreSQL (15.3%), Redis (9.7%), MySQL (6.9%) |
| SRE practices | 29.2% | 26.4% | Nên biết | L2 | Incident response (19.4%), High availability / DR (11.1%), SLI/SLO (6.9%) |
| Config management | 25.0% | 20.8% | Nên biết | L2 | Ansible (20.8%), Chef (4.2%), Configuration management (2.8%) |
| Version control | 23.6% | 22.2% | Nên biết | L2 | Git (22.2%), GitHub (2.8%) |
| K8s packaging | 19.4% | 13.9% | Nên biết | L2 | Helm (19.4%), Kustomize (4.2%), Helmfile (1.4%) |
| Messaging | 11.1% | 4.2% | Bỏ qua | - | Kafka (8.3%), RabbitMQ (2.8%), Redpanda (2.8%) |
| AI tooling | 9.7% | 5.6% | Bỏ qua | - | AI coding tools (9.7%) |
| Cost/FinOps | 9.7% | 5.6% | Bỏ qua | - | FinOps (6.9%), Cloud cost optimization (1.4%), AWS cost optimization (1.4%) |
| Service mesh | 6.9% | 1.4% | Bỏ qua | - | Service mesh (5.6%), Istio (2.8%), Linkerd (1.4%) |

## Chứng chỉ

- Tin có nhắc tới ít nhất 1 chứng chỉ: **22.2%** (16/72)

| Chứng chỉ | % tin nhắc tới | % bắt buộc | Đạt ngưỡng 15%? |
|---|---|---|---|
| AWS (bất kỳ chứng chỉ AWS) | 12.5% | 1.4% | — |
| Cloud (bất kỳ nhà cung cấp) | 9.7% | 1.4% | — |
| CKA | 5.6% | 0.0% | — |
| Azure (bất kỳ) | 4.2% | 0.0% | — |
| CKAD | 4.2% | 0.0% | — |
| CKS | 4.2% | 0.0% | — |
| Databricks certification (Data Engineer or Platform Administrator) | 1.4% | 0.0% | — |
| DevOps certification | 1.4% | 0.0% | — |
| Linux certification | 1.4% | 0.0% | — |
| Red Hat EX280 | 1.4% | 0.0% | — |
| Security+ | 1.4% | 0.0% | — |


---

## Đối chiếu nguồn khác

| Nguồn | Nội dung đã đọc (2026-11-05) | Khớp / lệch với dữ liệu tin tuyển dụng |
|---|---|---|
| [roadmap.sh/devops](https://roadmap.sh/devops) — "Step by step guide for DevOps, SRE or any other Operations Role in 2026" | Mục "How do you become a DevOps Engineer" nêu: Python hoặc JavaScript (scripting), AWS, Ansible, Terraform, Docker, Kubernetes, Jenkins, Git, monitoring & logging | **Khớp** gần như hoàn toàn với nhóm Cốt lõi/Quan trọng. Lệch: roadmap.sh nhấn Ansible và Jenkins mạnh hơn dữ liệu (Ansible chỉ 15.7% J/M). Sơ đồ chi tiết (dạng đồ hoạ) không đọc được bằng WebFetch → chưa đối chiếu thứ tự topic. |
| [CNCF Annual Cloud Native Survey 2025](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/) (công bố 2026-01-20) | Kubernetes dùng ở production: 82% người dùng container (2023: 66%). 98% tổ chức áp dụng cloud native. GitOps dùng nhiều ở nhóm "innovators" 58% vs "adopters" 23%. Trở ngại hàng đầu: văn hoá (47%), thiếu đào tạo & bảo mật (36% mỗi mục). | **Khớp**: Kubernetes là Cốt lõi (66.7–73.6% tin). GitOps ở mức "Nên biết" (25–29%) phù hợp việc nó còn tập trung ở công ty trưởng thành. |

## Hạn chế của dữ liệu
- **Cỡ mẫu**: 72 tin (mục tiêu ≥ 50 ✅); mẫu J/M là 51 tin. Một tool chênh 2–3 tin là đổi ~5 điểm %, nên chỉ so sánh chênh lệch lớn.
- **Nguồn bị chặn**: LinkedIn (chặn hoàn toàn), TopCV (HTTP 403 — chỉ 2 tin qua snippet), VietnamWorks (render JS — 0 tin), WeWorkRemotely (403 trang chi tiết), Indeed/Glassdoor (chỉ ra trang danh sách), CareerViet (trang quá lớn).
- **Thiên lệch nguồn**: VN chủ yếu từ ITviec (22 tin) → thiên về công ty IT/product tại HCM/HN; ít doanh nghiệp truyền thống đăng trên TopCV/VietnamWorks. Quốc tế nặng về Himalayas (15 tin, lọc theo tin cho phép Vietnam).
- **Ngày đăng**: 62/72 tin có ngày (2026-06-10 → 2026-11-05). 10 tin không có ngày (4 tin TopDev đã hết hạn, 2 TopCV, 4 Wellfound) — chưa xác minh được thuộc 6 tháng gần nhất.
- **Trích xuất**: một số trang ITviec bị WebFetch tóm tắt lại, tên tool đầy đủ nhưng câu chữ không nguyên văn. Tin "Energi" (remote) có dấu hiệu hết hạn, độ tin cậy thấp.
- **Chuẩn hoá**: "CI/CD" ghi chung (không nêu tool) chiếm 54.9% → % từng tool CI/CD thực tế có thể cao hơn số liệu.
