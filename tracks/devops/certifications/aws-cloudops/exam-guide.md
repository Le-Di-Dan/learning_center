# AWS Certified CloudOps Engineer – Associate (SOA-C03) — Tóm tắt exam guide

> Tên cũ: **AWS Certified SysOps Administrator – Associate**. AWS đã đổi tên khi ra phiên bản SOA-C03.
>
> Nguồn chính hãng:
> - Trang chứng chỉ: https://aws.amazon.com/certification/certified-cloudops-engineer-associate/
> - Exam guide (HTML): https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03.html
> - Chính sách ESL +30: https://aws.amazon.com/certification/policies/before-testing/
>
> Kiểm tra ngày: 2026-11-05. **Trước khi đăng ký thi, hãy mở lại trang chính hãng để kiểm tra phí, ngôn ngữ và phiên bản đề.**

## Thông tin kỳ thi

| Mục | Giá trị |
|---|---|
| Mã đề / phiên bản hiện hành | **SOA-C03**. Dùng từ ngày 30/09/2025 (SOA-C02 chỉ dùng tới hết 29/09/2025). Exam guide hiện là bản **1.2**, đăng ngày 29/10/2026 |
| Phiên bản mới sắp áp dụng | Không có mã đề mới nào được công bố. Exam guide được sửa định kỳ: 1.0 (30/09/2025), 1.1 (01/06/2026), 1.2 (29/10/2026). AWS cam kết công bố bản sửa ít nhất 1 tháng trước khi đề thi thay đổi theo. Bảng thay đổi chỉ ghi rõ khác biệt 1.0 → 1.1. Nội dung thay đổi của bản 1.2: **chưa xác minh** |
| Format | Trắc nghiệm, gồm 2 loại: **multiple choice** (1 đáp án đúng, 3 đáp án nhiễu) và **multiple response** (từ 2 đáp án đúng trở lên, trong ít nhất 5 lựa chọn). **Không có exam lab** (bài thực hành trên console): exam guide SOA-C03 chỉ liệt kê 2 loại câu hỏi trên |
| Số câu | 65 câu. Trong đó **50 câu tính điểm** và **15 câu không tính điểm** (AWS dùng để thử câu hỏi mới, bạn không biết câu nào là câu thử). Câu bỏ trống bị tính là sai, đoán sai không bị trừ điểm |
| Thời lượng | 130 phút (+30 phút nếu đăng ký ESL +30, xem bên dưới) |
| Điểm đạt | **720/1000** (thang điểm quy đổi 100–1000). Chấm kiểu bù trừ (compensatory): chỉ cần đạt tổng, không cần đạt từng domain |
| Phí thi | 150 USD, có thể phát sinh thêm phí chênh lệch tỷ giá (xem trang Exam pricing của AWS) |
| Ngôn ngữ đề | English, Japanese, Korean, Simplified Chinese. **Lưu ý:** bản Simplified Chinese và Korean sẽ ngừng sau ngày 19/11/2026. Không có tiếng Việt |
| Hình thức | Thi tại trung tâm khảo thí Pearson VUE hoặc thi online có giám sát (online proctored) |
| Hiệu lực | 3 năm. Gia hạn bằng cách thi đạt phiên bản mới nhất của đề này, hoặc lấy chứng chỉ AWS Certified DevOps Engineer – Professional (cũng gia hạn luôn chứng chỉ Associate này) |
| Hỗ trợ người không nói tiếng Anh bản xứ | **Có: ESL +30**, cộng thêm 30 phút khi thi bằng tiếng Anh. Cách đăng ký: đăng nhập aws.training/Certification → Go to your Account → Request Exam Accommodations → Request Accommodation → chọn "ESL +30 MINUTES" → Create. Chỉ cần đăng ký **một lần, trước khi đăng ký thi**, áp dụng cho các lần đăng ký thi sau đó. Ngoài ra, đề dùng tên viết tắt chính thức của dịch vụ (vd Amazon SNS); nút Help trong đề có bảng tên đầy đủ |
| Điều kiện tiên quyết | Không bắt buộc. AWS khuyến nghị: khoảng 1 năm kinh nghiệm triển khai, quản lý, xử lý sự cố, networking và security trên AWS, cộng với ít nhất 1 năm ở vai trò vận hành (vd system administrator). Người chưa có kinh nghiệm IT nên thi Cloud Practitioner trước |

### Ghi chú cho người giữ chứng chỉ cũ
- Tên mới "CloudOps Engineer" chỉ áp dụng cho người thi đạt SOA-C03.
- Người đang có chứng chỉ SysOps Administrator vẫn còn hiệu lực đủ 3 năm kể từ ngày đạt, không phải thi lại ngay.

### So sánh nhanh với Solutions Architect – Associate (SAA-C03)
Thông tin SAA lấy từ https://aws.amazon.com/certification/certified-solutions-architect-associate/ (kiểm tra 2026-11-05).

| Mục | CloudOps Engineer – Associate (SOA-C03) | Solutions Architect – Associate |
|---|---|---|
| Trọng tâm | **Vận hành**: giám sát, tự động hoá, xử lý sự cố, backup/DR, triển khai bằng IaC | **Thiết kế** kiến trúc trên AWS |
| Số câu / thời lượng | 65 câu / 130 phút | 65 câu / 130 phút |
| Phí | 150 USD | 150 USD |
| Ngôn ngữ | 4 ngôn ngữ (2 ngôn ngữ ngừng sau 19/11/2026) | 10 ngôn ngữ (bản tiếng Ý ngừng sau 31/12/2026) |
| Kinh nghiệm khuyến nghị | ~1 năm vận hành workload trên AWS | ≥ 1 năm thiết kế giải pháp trên AWS |
| Mã đề | SOA-C03 (xác minh trên trang chính hãng) | Trang chứng chỉ không ghi trực tiếp; link ôn thi trên trang có chữ "SAA-C03" → **chưa xác minh trực tiếp** |
| Gia hạn qua chứng chỉ Professional | DevOps Engineer – Professional | Solutions Architect – Professional |

Điểm đạt của SAA chưa được kiểm tra trong lần nghiên cứu này (**chưa xác minh**).

## Domain & tỷ trọng

Số câu ước tính tính theo tỷ trọng. Đề thật có 50 câu tính điểm. Đề thi thử đầy đủ 65 câu thì chia theo cột cuối.

| # | Domain | Tỷ trọng | Ước tính /50 câu tính điểm | Số câu ước tính (đề thi thử đầy đủ 65 câu) |
|---|---|---|---|---|
| 1 | Monitoring, Logging, Analysis, Remediation, and Performance Optimization | 22% | 11 | 14 |
| 2 | Reliability and Business Continuity | 22% | 11 | 14 |
| 3 | Deployment, Provisioning, and Automation | 22% | 11 | 14 |
| 4 | Security and Compliance | 16% | 8 | 11 |
| 5 | Networking and Content Delivery | 18% | 9 | 12 |

### Khác biệt so với SOA-C02 (theo trang so sánh chính hãng)
- SOA-C02 có 6 domain. Domain 6 "Cost and Performance Optimization" (12%) bị bỏ; Task 6.1 và 6.2 chuyển vào **Task 1.3** của SOA-C03.
- Tỷ trọng thay đổi: Domain 1 từ 20% lên 22%, Domain 2 từ 16% lên 22%, Domain 3 từ 18% lên 22%. Domain 4 (16%) và Domain 5 (18%) giữ nguyên.
- Nội dung thêm: CloudWatch agent cho EC2/ECS/EKS (1.1), CloudFormation **và AWS CDK** (3.1), ép tuân thủ theo Region/dịch vụ (4.1), CloudWatch network monitoring (5.3).
- Nội dung bỏ: cấu hình S3 static website hosting.
- Chuyển chỗ: VPN chuyển từ Task 4.2 sang Task 5.1.

### Bản 1.1 (01/06/2026) thêm gì
- Dịch vụ thêm vào phạm vi thi: Amazon Bedrock, AWS DevOps Agent, AWS Health Dashboard, Kiro, AWS Security Agent.
- Một số objective được viết rõ hơn, kèm ví dụ cụ thể: 1.1.1, 1.2.1, 1.3.4 (thêm Amazon S3 Files), 2.3.4 (các chiến lược DR), 3.2.2, 4.1.3, 4.1.5, 4.2.5, 5.1.2.

## Objective chi tiết (dịch & giải thích)

> Lưu ý: dòng in đậm giữ nguyên văn tiếng Anh từ exam guide. Exam guide nói rõ danh sách này **không bao quát hết** nội dung đề thi.

### Domain 1 — Monitoring, Logging, Analysis, Remediation, and Performance Optimization (Giám sát, ghi log, phân tích, khắc phục sự cố và tối ưu hiệu năng) — 22%

#### Task 1.1: Implement metrics, alarms, and filters by using AWS monitoring and logging services.
*(Triển khai metric, cảnh báo và bộ lọc bằng các dịch vụ giám sát/ghi log của AWS)*

- **1.1.1 Use AWS services (for example, Amazon CloudWatch, AWS CloudTrail, Amazon Managed Service for Prometheus) to configure monitoring and logging for workloads (for example, serverless, compute, AI).** — Biết dùng CloudWatch (metric, log), CloudTrail (ghi lại ai gọi API nào) và Managed Prometheus để giám sát nhiều loại workload: serverless (Lambda), máy chủ (EC2), cả workload AI.
- **1.1.2 Configure and manage the CloudWatch agent to collect metrics and logs from EC2 instances, Amazon ECS clusters, or Amazon EKS clusters.** — Cài và cấu hình CloudWatch agent (chương trình chạy trên máy/cluster) để gửi thêm metric như RAM, disk và file log về CloudWatch. Mặc định EC2 không gửi metric RAM, nên phải có agent.
- **1.1.3 Configure, identify, and troubleshoot CloudWatch alarms that can invoke AWS services directly or through Amazon EventBridge (for example, by creating composite alarms and identifying their invokable actions).** — Tạo alarm (cảnh báo khi metric vượt ngưỡng), alarm gộp (composite alarm, kết hợp nhiều alarm bằng AND/OR). Biết alarm có thể kích hoạt hành động gì: gửi SNS, scale Auto Scaling, reboot/stop EC2, hoặc đi qua EventBridge. Biết sửa khi alarm không kêu.
- **1.1.4 Create, implement, and manage customizable and shareable CloudWatch dashboards that display metrics and alarms for AWS resources across multiple accounts and AWS Regions.** — Tạo dashboard CloudWatch, chia sẻ được, hiển thị dữ liệu từ nhiều account và nhiều Region trên cùng một màn hình.
- **1.1.5 Configure AWS services to send notifications to Amazon SNS and to invoke alarms that send notifications to Amazon SNS.** — Cấu hình gửi thông báo qua SNS (dịch vụ pub/sub gửi email/SMS/HTTP), trực tiếp từ dịch vụ hoặc thông qua alarm.

#### Task 1.2: Identify and remediate issues by using monitoring and availability metrics.
*(Phát hiện và khắc phục sự cố dựa trên metric giám sát và độ sẵn sàng)*

- **1.2.1 Analyze performance metrics and automate remediation strategies by using AWS services and functionality (for example, CloudWatch, Lambda, AWS Systems Manager, CloudTrail, Kiro, AWS DevOps Agent).** — Đọc metric để tìm nguyên nhân, rồi tự động khắc phục (auto-remediation): vd alarm → Lambda hoặc Systems Manager tự sửa. Bản mới có thêm công cụ AI là Kiro và AWS DevOps Agent.
- **1.2.2 Use EventBridge to route, enrich, and deliver events, and troubleshoot any issues with event bus rules.** — Dùng EventBridge (bộ định tuyến sự kiện) để lọc sự kiện, thêm dữ liệu vào sự kiện và chuyển tới đích. Biết sửa lỗi khi rule không khớp sự kiện (sai event pattern, thiếu quyền gọi target...).
- **1.2.3 Create or run custom and predefined Systems Manager Automation runbooks (for example, by using AWS SDKs or custom scripts) to automate tasks and streamline processes on AWS.** — Dùng runbook (kịch bản tự động hoá) của Systems Manager Automation, loại có sẵn của AWS hoặc tự viết, để tự động hoá việc vận hành (vd restart, tạo snapshot, vá lỗi).

#### Task 1.3: Implement performance optimization strategies for compute, storage, and database resources.
*(Tối ưu hiệu năng cho compute, storage và database)*

- **1.3.1 Optimize compute resources and remediate performance problems by using performance metrics, resource tags, and AWS tools.** — Chọn đúng loại/kích thước máy (right-sizing) dựa trên metric, dùng tag để quản lý, dùng công cụ như Compute Optimizer.
- **1.3.2 Analyze Amazon EBS performance metrics, troubleshoot issues, and optimize volume types to improve performance and reduce cost.** — Hiểu metric của ổ đĩa EBS (IOPS, throughput, độ trễ), các loại volume (gp3, io2, st1...) và chọn loại phù hợp để vừa nhanh vừa rẻ.
- **1.3.3 Implement and optimize S3 performance strategies (for example, AWS DataSync, S3 Transfer Acceleration, multipart uploads, S3 Lifecycle policies) to enhance data transfer, storage efficiency, and access patterns.** — Tăng tốc truyền dữ liệu S3 (multipart upload: chia file lớn thành nhiều phần; Transfer Acceleration; DataSync) và giảm chi phí lưu trữ (Lifecycle: tự chuyển dữ liệu cũ sang lớp lưu trữ rẻ hơn hoặc xoá).
- **1.3.4 Evaluate and select shared storage solutions (for example, Amazon EFS, Amazon FSx, Amazon S3 Files), and optimize the solutions (for example, EFS lifecycle policies) for specific use cases and requirements.** — Chọn hệ thống file dùng chung (nhiều máy cùng mount): EFS (NFS cho Linux), FSx (Windows, Lustre...), S3 Files. Tối ưu chi phí bằng lifecycle policy.
- **1.3.5 Monitor Amazon RDS metrics (for example, Amazon RDS Performance Insights, CloudWatch alarms) and modify configurations to increase performance efficiency (for example, Performance Insights proactive recommendations, RDS Proxy).** — Theo dõi database RDS bằng Performance Insights (xem câu SQL nào chậm) và alarm. Biết dùng RDS Proxy (gom connection, giảm tải cho DB, hay dùng với Lambda).
- **1.3.6 Implement, monitor, and optimize EC2 instances and their associated storage and networking capabilities (for example, EC2 placement groups).** — Tối ưu EC2 cùng storage và mạng đi kèm, vd placement group (cách xếp các máy: cluster gần nhau cho độ trễ thấp, spread để tránh hỏng cùng lúc, partition).

### Domain 2 — Reliability and Business Continuity (Độ tin cậy và duy trì hoạt động kinh doanh) — 22%

#### Task 2.1: Implement scalability and elasticity.
*(Triển khai khả năng mở rộng và co giãn)*

- **2.1.1 Configure and manage scaling mechanisms in compute environments.** — Cấu hình Auto Scaling (tự tăng/giảm số máy hoặc task theo tải): các kiểu scaling policy (target tracking, step, scheduled), cho EC2, ECS, Lambda.
- **2.1.2 Implement caching by using AWS services to enhance dynamic scalability (for example, Amazon CloudFront, Amazon ElastiCache).** — Dùng cache để giảm tải cho backend: CloudFront (CDN, cache ở gần người dùng), ElastiCache (Redis/Memcached, cache trong bộ nhớ).
- **2.1.3 Configure and manage scaling in AWS managed databases (for example, Amazon RDS, DynamoDB).** — Scale database: RDS read replica, tăng kích thước instance, storage autoscaling. DynamoDB: on-demand hay provisioned capacity, auto scaling.

#### Task 2.2: Implement highly available and resilient environments.
*(Triển khai môi trường có tính sẵn sàng cao và khả năng chịu lỗi)*

- **2.2.1 Configure and troubleshoot Elastic Load Balancing (ELB) and Amazon Route 53 health checks.** — Cấu hình health check (kiểm tra máy còn sống không) cho load balancer (bộ cân bằng tải) và Route 53. Biết sửa lỗi target bị đánh dấu unhealthy (sai port/path, security group chặn...).
- **2.2.2 Configure fault-tolerant systems (for example, Multi-AZ deployments).** — Thiết kế để một Availability Zone (AZ, cụm data center) hỏng vẫn chạy: RDS Multi-AZ, Auto Scaling group trải trên nhiều AZ.

#### Task 2.3: Implement backup and restore strategies.
*(Triển khai chiến lược sao lưu và khôi phục)*

- **2.3.1 Automate snapshots and backups for AWS resources (for example, EC2 instances, RDS DB instances, EBS volumes, S3 buckets, DynamoDB tables) by using AWS services (for example, AWS Backup).** — Tự động hoá backup bằng AWS Backup (backup plan, vault) và snapshot cho EC2, RDS, EBS, S3, DynamoDB.
- **2.3.2 Use various methods to restore databases (for example, point-in-time restore) to meet recovery time objective (RTO), recovery point objective (RPO), and cost requirements.** — Khôi phục database (vd point-in-time restore: khôi phục về một thời điểm bất kỳ). Chọn cách phù hợp với RTO (bao lâu phải chạy lại), RPO (chấp nhận mất dữ liệu bao nhiêu) và chi phí.
- **2.3.3 Implement versioning for storage services (for example, Amazon S3, Amazon FSx).** — Bật versioning (giữ nhiều phiên bản của file) để chống xoá/ghi đè nhầm.
- **2.3.4 Follow disaster recovery procedures and best practices (for example, backup and restore, pilot light, warm standby, active/active).** — Nắm 4 chiến lược DR (khôi phục sau thảm hoạ), từ rẻ/chậm đến đắt/nhanh: backup & restore → pilot light → warm standby → active/active (multi-site).

### Domain 3 — Deployment, Provisioning, and Automation (Triển khai, cấp phát tài nguyên và tự động hoá) — 22%

#### Task 3.1: Provision and maintain cloud resources.
*(Cấp phát và duy trì tài nguyên cloud)*

- **3.1.1 Create and manage AMIs and container images (for example, EC2 Image Builder).** — Tạo và quản lý AMI (image máy ảo EC2) và container image, tự động hoá bằng EC2 Image Builder.
- **3.1.2 Create and manage AWS resources by using CloudFormation and the AWS CDK.** — Viết infrastructure as code (IaC, hạ tầng dưới dạng code) bằng CloudFormation (YAML/JSON) và AWS CDK (viết bằng ngôn ngữ lập trình như TypeScript, Python).
- **3.1.3 Identify and remediate deployment issues (for example, subnet sizing issues, CloudFormation errors, permissions issues).** — Sửa lỗi triển khai: subnet hết IP, stack CloudFormation lỗi/rollback, thiếu quyền IAM.
- **3.1.4 Provision and share resources across multiple Regions and accounts (for example, AWS Resource Access Manager [AWS RAM], CloudFormation StackSets).** — Triển khai và chia sẻ tài nguyên ra nhiều account/Region: StackSets (một template, deploy nhiều nơi), RAM (chia sẻ subnet, Transit Gateway... giữa các account).
- **3.1.5 Implement deployment strategies and services.** — Hiểu các chiến lược deploy (rolling, blue/green, canary, immutable) và dịch vụ hỗ trợ.
- **3.1.6 Use and manage third-party tools to automate resource deployment (for example, Terraform, Git).** — Dùng công cụ bên thứ ba như Terraform và Git để tự động triển khai.

#### Task 3.2: Automate the management of existing resources.
*(Tự động hoá quản lý tài nguyên đang có)*

- **3.2.1 Use AWS services to automate operational processes (for example, Systems Manager).** — Dùng Systems Manager để vận hành hàng loạt máy: Run Command, Patch Manager, Session Manager, Parameter Store, State Manager...
- **3.2.2 Implement event-driven automation by using AWS services and features (for example, Lambda, S3 Event Notifications, EventBridge, AWS DevOps Agent).** — Tự động hoá theo sự kiện: vd có file mới vào S3 → gọi Lambda; EventBridge rule → hành động.

### Domain 4 — Security and Compliance (Bảo mật và tuân thủ) — 16%

#### Task 4.1: Implement and manage security and compliance tools and policies.
*(Triển khai và quản lý công cụ, chính sách bảo mật và tuân thủ)*

- **4.1.1 Implement IAM features (for example, password policies, multi-factor authentication [MFA], roles, federated identity, resource policies, policy conditions).** — Dùng các tính năng IAM (quản lý danh tính và quyền): chính sách mật khẩu, MFA (xác thực nhiều lớp), role, đăng nhập liên kết (federation), resource policy, điều kiện trong policy.
- **4.1.2 Troubleshoot and audit access issues by using AWS tools (for example, CloudTrail, IAM Access Analyzer, IAM policy simulator).** — Điều tra lỗi "Access Denied" và kiểm toán quyền: xem log CloudTrail, dùng Access Analyzer (tìm tài nguyên bị chia sẻ ra ngoài), policy simulator (thử policy).
- **4.1.3 Implement multi-account strategies securely (for example, AWS Organizations, service control policies, IAM Identity Center).** — Quản lý nhiều account an toàn: Organizations, SCP (giới hạn quyền tối đa cho account), IAM Identity Center (đăng nhập một lần vào nhiều account).
- **4.1.4 Implement remediation based on the results of AWS Trusted Advisor security checks.** — Đọc khuyến nghị bảo mật của Trusted Advisor và khắc phục.
- **4.1.5 Enforce compliance requirements and continuous monitoring (for example, Region and service selections, AWS Config conformance packs).** — Ép buộc tuân thủ (vd chỉ được dùng Region/dịch vụ cho phép) và giám sát liên tục bằng AWS Config conformance pack (bộ rule kiểm tra cấu hình).

#### Task 4.2: Implement strategies to protect data and infrastructure.
*(Bảo vệ dữ liệu và hạ tầng)*

- **4.2.1 Implement and enforce a data classification scheme.** — Phân loại dữ liệu (công khai, nội bộ, nhạy cảm...) và áp dụng, vd gắn tag, dùng Macie để tìm dữ liệu nhạy cảm trong S3.
- **4.2.2 Implement, configure, and troubleshoot encryption at rest (for example, AWS KMS).** — Mã hoá dữ liệu lưu trữ bằng KMS (dịch vụ quản lý khoá). Biết sửa lỗi liên quan đến key policy và quyền dùng khoá.
- **4.2.3 Implement, configure, and troubleshoot encryption in transit (for example, AWS Certificate Manager [ACM]).** — Mã hoá dữ liệu khi truyền (HTTPS/TLS), dùng ACM để cấp và gắn chứng chỉ TLS cho load balancer/CloudFront.
- **4.2.4 Securely store secrets by using AWS services.** — Lưu mật khẩu/API key an toàn: Secrets Manager (có tự xoay vòng), Systems Manager Parameter Store.
- **4.2.5 Configure reports and remediate findings from AWS services (for example, AWS Security Hub, Amazon GuardDuty, AWS Config, Amazon Inspector, AWS Security Agent).** — Đọc và xử lý cảnh báo từ các dịch vụ bảo mật: Security Hub (tổng hợp), GuardDuty (phát hiện mối đe doạ), Config, Inspector (quét lỗ hổng), Security Agent.

### Domain 5 — Networking and Content Delivery (Mạng và phân phối nội dung) — 18%

#### Task 5.1: Implement and optimize networking features and connectivity.
*(Triển khai và tối ưu tính năng mạng, kết nối)*

- **5.1.1 Configure a VPC (for example, subnets, route tables, network ACLs, security groups, NAT gateways, internet gateway, egress-only internet gateway).** — Dựng VPC (mạng riêng ảo) đầy đủ: subnet public/private, route table, NACL (tường lửa cấp subnet, stateless), security group (tường lửa cấp instance, stateful), NAT gateway, internet gateway, egress-only IGW (cho IPv6 đi ra).
- **5.1.2 Configure private networking connectivity (for example, VPC endpoints, AWS PrivateLink, VPC peering).** — Kết nối riêng không qua internet: VPC endpoint (gateway/interface), PrivateLink, VPC peering.
- **5.1.3 Audit AWS network protection services (for example, Route 53 Resolver DNS Firewall, AWS WAF, AWS Shield, AWS Network Firewall) in a single account.** — Kiểm tra cấu hình các dịch vụ bảo vệ mạng trong một account: DNS Firewall, WAF (tường lửa web), Shield (chống DDoS), Network Firewall.
- **5.1.4 Optimize the cost of network architectures.** — Giảm chi phí mạng: vd dùng gateway endpoint cho S3 thay vì đi qua NAT gateway, hạn chế truyền dữ liệu giữa AZ/Region.

#### Task 5.2: Configure domains, DNS services, and content delivery.
*(Cấu hình tên miền, DNS và phân phối nội dung)*

- **5.2.1 Configure DNS (for example, Route 53 Resolver).** — Cấu hình DNS, gồm Route 53 Resolver (phân giải DNS giữa VPC và mạng on-premises).
- **5.2.2 Implement Route 53 routing policies, configurations, and query logging.** — Dùng các routing policy của Route 53 (simple, weighted, latency, failover, geolocation...) và bật ghi log truy vấn DNS.
- **5.2.3 Configure content and service distribution (for example, CloudFront, AWS Global Accelerator).** — Phân phối nội dung/dịch vụ toàn cầu: CloudFront (CDN) và Global Accelerator (định tuyến qua mạng AWS, dùng IP tĩnh).

#### Task 5.3: Troubleshoot network connectivity issues.
*(Xử lý sự cố kết nối mạng)*

- **5.3.1 Troubleshoot VPC configurations (for example, subnets, route tables, network ACLs, security groups, transit gateways, NAT gateways).** — Tìm lỗi "không kết nối được" trong VPC: thiếu route, NACL chặn chiều về, security group sai, Transit Gateway, NAT.
- **5.3.2 Collect and interpret networking logs to troubleshoot issues (for example, VPC flow logs, ELB access logs, AWS WAF web ACL logs, CloudFront logs, container logs).** — Bật và đọc các loại log mạng để tìm lỗi (vd flow log có REJECT → bị chặn ở đâu).
- **5.3.3 Identify and remediate CloudFront caching issues.** — Sửa lỗi cache CloudFront: nội dung cũ (cần invalidation), cache key/TTL sai, tỷ lệ cache hit thấp.
- **5.3.4 Identify and troubleshoot hybrid connectivity issues and private connectivity issues.** — Sửa lỗi kết nối hybrid (giữa on-premises và AWS, vd Site-to-Site VPN) và kết nối riêng (endpoint, PrivateLink).
- **5.3.5 Configure and analyze CloudWatch network monitoring services.** — Dùng các tính năng giám sát mạng của CloudWatch để theo dõi và phân tích kết nối.

## Dịch vụ trong phạm vi thi (tóm tắt)

Danh sách đầy đủ (không bao quát hết, có thể thay đổi): https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/soa-03-in-scope-services.html

Nhóm quan trọng nhất theo objective: CloudWatch, CloudTrail, EventBridge, SNS, Systems Manager, EC2/EBS/Auto Scaling, ELB, S3, EFS/FSx, RDS/Aurora/DynamoDB/ElastiCache, AWS Backup, CloudFormation/CDK, StackSets/RAM, IAM/Organizations/SCP/Identity Center, KMS/ACM/Secrets Manager, Config/Security Hub/GuardDuty/Inspector, VPC (subnet, route, NACL, SG, NAT, endpoint, peering, Transit Gateway, Flow Logs, Reachability Analyzer), Route 53, CloudFront, Global Accelerator. Container: ECR, ECS, EKS.

## Phong cách câu hỏi

- **Câu tình huống vận hành**: mô tả một hệ thống đang chạy và một vấn đề (alarm không kêu, máy không kết nối được, backup không đạt RPO, Access Denied...). Bạn chọn cách xử lý đúng.
- Hay gặp các yêu cầu so sánh như **"MOST operationally efficient"** (ít công vận hành nhất, ưu tiên dịch vụ managed và tự động hoá), **"MOST cost-effective"**, **"LEAST amount of effort"**. Đọc kỹ cụm này, vì nhiều đáp án đều "chạy được" nhưng chỉ một đáp án thoả tiêu chí. *(Nhận xét về cách diễn đạt câu hỏi này dựa trên đặc điểm chung của đề AWS. Exam guide không liệt kê các cụm từ này — chưa xác minh trên nguồn chính hãng.)*
- **Multiple response**: đề ghi rõ số đáp án cần chọn (vd "Choose two"). Phải chọn đủ và đúng hết mới được tính điểm câu đó *(exam guide chỉ nói mỗi câu là một "scored opportunity"; quy tắc không có điểm từng phần chưa xác minh)*.
- Đáp án nhiễu (distractor) được viết "hợp lý", đúng chủ đề. Người nắm kiến thức chưa chắc rất dễ chọn nhầm.
- **Không có exam lab**: đề SOA-C03 chỉ có multiple choice và multiple response. Tuy vậy, objective vẫn dùng động từ "Configure / Troubleshoot / Implement" nên cần thực hành console và CLI thật để hiểu sâu.
- Không bị trừ điểm khi đoán. **Đừng bỏ trống câu nào.**
- Tên dịch vụ dùng dạng viết tắt chính thức (Amazon SNS, AWS KMS...). Nút Help có bảng tra tên đầy đủ.
- Thời gian: 130 phút cho 65 câu, khoảng 2 phút/câu. Có ESL +30 thì khoảng 2,5 phút/câu.

## Tài liệu ôn chính hãng

- **Exam guide SOA-C03** (HTML, gồm các trang domain, dịch vụ in-scope/out-of-scope, so sánh với C02, lịch sử sửa đổi): https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03.html
- **Trang chứng chỉ**: https://aws.amazon.com/certification/certified-cloudops-engineer-associate/
- **AWS Skill Builder — Exam prep plan 4 bước cho SOA-C03**: https://skillbuilder.aws/category/exam-prep/cloudops-engineer-associate-SOA-C03 . Theo trang chứng chỉ, gồm **Official Practice Question Set** và **Official Practice Exam**. Trang Skill Builder không đọc được bằng công cụ, nên danh sách khoá học cụ thể và mục nào miễn phí/trả phí **chưa xác minh**.
- **AWS Well-Architected Framework**: exam guide yêu cầu người thi nắm framework này (link tài liệu chưa fetch trong lần này).
- Tài liệu dịch vụ trên docs.aws.amazon.com cho từng dịch vụ in-scope. Bài học sẽ fetch khi học từng module.
- **Chính sách ESL +30 / đăng ký thi**: https://aws.amazon.com/certification/policies/before-testing/

> Nhắc nhở: chỉ dùng câu hỏi tự soạn theo objective và tài liệu chính hãng ở trên. Không dùng "exam dump" (vi phạm thoả thuận thi, có thể bị thu hồi chứng chỉ).

---
**Nguồn đã truy cập (2026-11-05):**
- https://aws.amazon.com/certification/certified-cloudops-engineer-associate/
- https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03.html (exam guide, bản 1.2)
- https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03-domain1.html … domain5.html
- https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03-comparison.html
- https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/soa-03-revisions.html
- https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/soa-03-in-scope-services.html
- https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/soa-03-service-mentions.html
- https://aws.amazon.com/certification/policies/before-testing/
- https://aws.amazon.com/certification/certified-solutions-architect-associate/ (để so sánh)
