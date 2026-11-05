# AWS Certified Solutions Architect – Associate (SAA-C03) — Tóm tắt exam guide

> Nguồn chính hãng:
> - Trang chứng chỉ: https://aws.amazon.com/certification/certified-solutions-architect-associate/
> - Exam guide (bản HTML chính thức): https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html
> - Exam guide (PDF): https://docs.aws.amazon.com/pdfs/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.pdf (chỉ thấy trong kết quả tìm kiếm, nội dung lấy từ bản HTML ở trên)
>
> Kiểm tra ngày: 2026-11-05 · Phiên bản exam guide: **1.1 (công bố 2026-10-29)**
>
> Nhắc người học: thông tin đề thi (phí, ngôn ngữ, phiên bản) có thể đổi. **Kiểm tra lại trang chính hãng ngay trước khi đăng ký thi.**

## Thông tin kỳ thi

| Mục | Giá trị |
|---|---|
| Mã đề / phiên bản hiện hành | **SAA-C03** (exam guide hiện hành, bản 1.1 ngày 2026-10-29) |
| Phiên bản mới sắp áp dụng | **Không có thông báo chính hãng nào về SAA-C04** (đã kiểm tra trang chứng chỉ, exam guide, trang Revisions, blog AWS Training & Certification tháng 9 và 10/2026 — ngày 2026-11-05). Các trang bên thứ ba có nhắc "SAA-C04" nhưng không được AWS xác nhận → coi là **chưa xác minh / không đáng tin**. Xem mục "Lưu ý phiên bản" bên dưới. |
| Format | Trắc nghiệm: **multiple choice** (1 đáp án đúng / 4 lựa chọn) và **multiple response** (≥ 2 đáp án đúng / ≥ 5 lựa chọn) |
| Số câu | **65 câu** = 50 câu tính điểm + 15 câu không tính điểm (không được đánh dấu, bạn không biết câu nào) |
| Thời lượng | **130 phút** (+30 phút nếu đăng ký ESL +30 → 160 phút) |
| Điểm đạt | **720 / 1000** (thang điểm quy đổi 100–1000, mô hình bù trừ: chỉ cần đạt tổng, không cần đạt từng domain) |
| Phí thi | **150 USD** (có thể cộng thuế; giá cho 1 lần thi). Trang pricing ghi các mức khác: €128, AUD 224, ¥20,000 (JPY)... |
| Ngôn ngữ đề | English, French (France), Italian, Japanese, Korean, Portuguese (Brazil), Spanish (Latin America), Spanish (Spain), Simplified Chinese, Traditional Chinese. **Không có tiếng Việt.** Lưu ý: bản tiếng Ý sẽ ngừng sau 2026-12-31. |
| Hình thức | Trung tâm khảo thí **Pearson VUE** hoặc **online proctored** (thi tại nhà, có giám thị online qua Pearson VUE) |
| Hiệu lực | **3 năm**. Gia hạn: thi đạt phiên bản mới nhất của đề này, hoặc đạt AWS Certified Solutions Architect – Professional (tự động gia hạn SAA). |
| Hỗ trợ người không nói tiếng Anh bản xứ | **Có — ESL +30** (cộng 30 phút khi thi bằng tiếng Anh). Cách đăng ký: đăng nhập `aws.training/Certification` → *Go to your Account* → *Request Exam Accommodations* → *Request Accommodation* → chọn **ESL +30 MINUTES** ở ô *Accommodation Type* → *Create*. Chỉ cần đăng ký **một lần, TRƯỚC khi đăng ký thi**; áp dụng cho mọi lần đăng ký sau với mọi đơn vị tổ chức thi. Ngoài ra, đề bản địa hoá có nút chuyển sang xem câu hỏi tiếng Anh. |
| Điều kiện tiên quyết | Không bắt buộc. AWS khuyến nghị **≥ 1 năm kinh nghiệm thực tế thiết kế giải pháp cloud trên AWS**. Người chưa có kinh nghiệm IT được khuyên thi AWS Certified Cloud Practitioner trước. |
| Thi lại | Trượt → chờ **14 ngày** mới được thi lại; không giới hạn số lần, mỗi lần trả đủ phí. Đã đạt → không thi lại cùng đề trong 2 năm. |
| Kết quả | Có trong tài khoản AWS Certification trong vòng **5 ngày làm việc**. |
| Giấy tờ | Giấy tờ tuỳ thân do nhà nước cấp; tên trong tài khoản AWS Certification phải khớp giấy tờ. Cần thêm giấy tờ phụ — xem chi tiết tại trang "Before Testing". |

### Lưu ý phiên bản (quan trọng)

- **SAA-C03 vẫn là đề hiện hành.** Không có thông báo SAA-C04 trên aws.amazon.com hay docs.aws.amazon.com tại ngày 2026-11-05.
- Exam guide SAA-C03 vừa có **bản sửa 1.1 (2026-10-29)**: bỏ *Amazon Elastic Transcoder* khỏi danh sách in-scope; bỏ AWS DeepComposer, Amazon DevOps Guru, Amazon Elastic Inference, Amazon Managed Blockchain, Amazon Sumerian khỏi danh sách out-of-scope. AWS ghi: *"Exam guide updates will be published approximately one month before updates will be reflected on your exam"* → thay đổi này dự kiến có hiệu lực trên đề thi khoảng **cuối tháng 11/2026**. Ảnh hưởng nhỏ, không đổi domain/tỷ trọng.
- Bối cảnh: AWS đang đổi phiên bản một số đề khác (theo blog AWS Training & Certification 9–10/2026): SAP-C02 → **SAP-C03** (SAP-C02 thi được tới 2026-11-16), DVA-C02 → **DVA-C03** (DVA-C02 thi được tới 2026-11-30), MLA-C01 → MLA-C02. Điều này cho thấy AWS có thể sẽ cập nhật SAA trong tương lai — **cần kiểm tra lại trước khi đăng ký thi**, nhất là nếu dự định thi sau vài tháng nữa.

## Domain & tỷ trọng

Tỷ trọng tính trên phần nội dung **có tính điểm** (50 câu). Cột cuối là số câu đề xuất khi soạn đề thi thử đầy đủ 65 câu.

| # | Domain | Tỷ trọng | Số câu ước tính (đề thi thử 65 câu) |
|---|---|---|---|
| 1 | Design Secure Architectures (Thiết kế kiến trúc bảo mật) | 30% | 20 |
| 2 | Design Resilient Architectures (Thiết kế kiến trúc bền vững, chịu lỗi) | 26% | 17 |
| 3 | Design High-Performing Architectures (Thiết kế kiến trúc hiệu năng cao) | 24% | 15 |
| 4 | Design Cost-Optimized Architectures (Thiết kế kiến trúc tối ưu chi phí) | 20% | 13 |
| | **Tổng** | 100% | 65 |

## Objective chi tiết (dịch & giải thích)

Exam guide chia mỗi domain thành các **Task** (nhiệm vụ). Mỗi task có phần *Knowledge of* (cần hiểu) và *Skills in* (cần làm được). Phần tiếng Anh giữ nguyên văn exam guide; phần tiếng Việt giải thích bạn cần biết gì. Exam guide nói rõ danh sách này **không đầy đủ tuyệt đối** — các ví dụ "for example" chỉ là ví dụ.

### Domain 1 — Design Secure Architectures (Thiết kế kiến trúc bảo mật) — 30%

#### 1.1 Design secure access to AWS resources (Thiết kế truy cập an toàn vào tài nguyên AWS)

Knowledge of:
- **Access controls and management across multiple accounts** — Quản lý quyền khi công ty có nhiều AWS account (AWS Organizations, cross-account role).
- **AWS federated access and identity services (for example, IAM, AWS IAM Identity Center)** — Đăng nhập tập trung (federation, tức dùng tài khoản công ty để vào AWS) thay vì tạo user riêng ở từng account.
- **AWS global infrastructure (for example, Availability Zones, AWS Regions)** — Hiểu Region (vùng địa lý) và AZ (trung tâm dữ liệu độc lập trong một Region).
- **AWS security best practices (for example, the principle of least privilege)** — Nguyên tắc "quyền tối thiểu": chỉ cấp đúng quyền cần dùng.
- **The AWS shared responsibility model** — Mô hình trách nhiệm chung: AWS lo bảo mật "của" cloud (phần cứng, hạ tầng), khách hàng lo bảo mật "trong" cloud (dữ liệu, cấu hình, IAM).

Skills in:
- **Applying AWS security best practices to IAM users and root users (for example, multi-factor authentication [MFA])** — Bật MFA, không dùng root user cho việc hằng ngày.
- **Designing a flexible authorization model that includes IAM users, groups, roles, and policies** — Biết khi nào dùng user, group, role, policy và kết hợp chúng.
- **Designing a role-based access control strategy (for example, AWS STS, role switching, cross-account access)** — Dùng role + STS (cấp credential tạm thời) để chuyển quyền, truy cập chéo account.
- **Designing a security strategy for multiple AWS accounts (for example, AWS Control Tower, service control policies [SCPs])** — Dùng SCP trong Organizations để "chặn trần" quyền của cả account; Control Tower để dựng landing zone nhiều account.
- **Determining the appropriate use of resource policies for AWS services** — Phân biệt identity-based policy (gắn vào user/role) và resource-based policy (gắn vào tài nguyên, vd S3 bucket policy).
- **Determining when to federate a directory service with IAM roles** — Khi nào nối Active Directory/IdP của công ty với IAM role.

#### 1.2 Design secure workloads and applications (Thiết kế workload và ứng dụng an toàn)

Knowledge of:
- **Application configuration and credentials security** — Không hard-code mật khẩu/key trong code; lưu ở Secrets Manager hoặc Parameter Store.
- **AWS service endpoints** — Địa chỉ API của dịch vụ AWS; liên quan VPC endpoint để gọi dịch vụ AWS mà không ra internet.
- **Control ports, protocols, and network traffic on AWS** — Kiểm soát port/protocol nào được mở (security group, NACL).
- **Secure application access** — Truy cập ứng dụng an toàn (xác thực người dùng, HTTPS...).
- **Security services with appropriate use cases (for example, Amazon Cognito, Amazon GuardDuty, Amazon Macie)** — Cognito: đăng nhập cho người dùng app; GuardDuty: phát hiện mối đe doạ; Macie: tìm dữ liệu nhạy cảm trong S3.
- **Threat vectors external to AWS (for example, DDoS, SQL injection)** — Các kiểu tấn công từ bên ngoài và dịch vụ chống lại chúng.

Skills in:
- **Designing VPC architectures with security components (for example, security groups, route tables, network ACLs, NAT gateways)** — Thiết kế VPC (mạng riêng ảo) với security group (firewall stateful ở mức instance), NACL (firewall stateless ở mức subnet), route table, NAT gateway.
- **Determining network segmentation strategies (for example, using public subnets and private subnets)** — Đặt web ở public subnet, app/DB ở private subnet.
- **Integrating AWS services to secure applications (for example, AWS Shield, AWS WAF, IAM Identity Center, AWS Secrets Manager)** — Shield chống DDoS, WAF (web application firewall) chặn SQL injection/XSS, Secrets Manager quản lý và xoay vòng secret.
- **Securing external network connections to and from the AWS Cloud (for example, VPN, AWS Direct Connect)** — Kết nối an toàn giữa văn phòng/data center và AWS: VPN qua internet hoặc Direct Connect (đường truyền riêng).

#### 1.3 Determine appropriate data security controls (Chọn biện pháp bảo vệ dữ liệu phù hợp)

Knowledge of:
- **Data access and governance** — Ai được truy cập dữ liệu nào, kiểm soát và audit.
- **Data recovery** — Khôi phục dữ liệu khi mất/hỏng.
- **Data retention and classification** — Thời gian lưu giữ và phân loại mức nhạy cảm của dữ liệu.
- **Encryption and appropriate key management** — Mã hoá và quản lý khoá (KMS, CloudHSM).

Skills in:
- **Aligning AWS technologies to meet compliance requirements** — Chọn dịch vụ đáp ứng yêu cầu tuân thủ (vd AWS Artifact để lấy báo cáo compliance, AWS Config để kiểm tra cấu hình).
- **Encrypting data at rest (for example, AWS KMS)** — Mã hoá dữ liệu khi lưu trữ (S3, EBS, RDS) bằng KMS key.
- **Encrypting data in transit (for example, AWS Certificate Manager [ACM] using TLS)** — Mã hoá dữ liệu khi truyền: HTTPS/TLS với certificate từ ACM.
- **Implementing access policies for encryption keys** — Viết key policy: ai được dùng/quản lý key.
- **Implementing data backups and replications** — Backup (AWS Backup, snapshot) và sao chép dữ liệu (vd S3 replication).
- **Implementing policies for data access, lifecycle, and protection** — Chính sách truy cập, vòng đời (lifecycle), bảo vệ dữ liệu (vd S3 Object Lock, versioning).
- **Rotating encryption keys and renewing certificates** — Xoay vòng key và gia hạn certificate.

### Domain 2 — Design Resilient Architectures (Thiết kế kiến trúc bền vững, chịu lỗi) — 26%

#### 2.1 Design scalable and loosely coupled architectures (Thiết kế kiến trúc dễ mở rộng và liên kết lỏng)

"Loosely coupled" (liên kết lỏng) = các thành phần không phụ thuộc trực tiếp vào nhau, một phần hỏng/chậm không kéo sập phần khác. Giống như trong frontend bạn dùng event bus thay vì gọi hàm trực tiếp giữa các component.

Knowledge of:
- **API creation and management (for example, Amazon API Gateway, REST API)** — Tạo và quản lý API bằng API Gateway.
- **AWS managed services with appropriate use cases (for example, AWS Transfer Family, Amazon SQS, AWS Secrets Manager)** — Dịch vụ managed (AWS vận hành hộ) và trường hợp dùng: Transfer Family (SFTP/FTP vào S3/EFS), SQS (hàng đợi message).
- **Caching strategies** — Chiến lược cache (bộ nhớ đệm) để giảm tải backend.
- **Design principles for microservices (for example, stateless workloads compared with stateful workloads)** — Stateless (không lưu trạng thái trong server, dễ scale) vs stateful.
- **Event-driven architectures** — Kiến trúc hướng sự kiện (EventBridge, SNS, S3 event → Lambda).
- **Horizontal scaling and vertical scaling** — Scale ngang (thêm máy) vs scale dọc (máy to hơn).
- **How to appropriately use edge accelerators (for example, content delivery network [CDN])** — Dùng CDN (CloudFront) để phân phối nội dung gần người dùng — bạn đã quen khi deploy frontend.
- **How to migrate applications into containers** — Đưa ứng dụng vào container.
- **Load balancing concepts (for example, Application Load Balancer [ALB])** — Cân bằng tải; ALB làm việc ở tầng HTTP (Layer 7).
- **Multi-tier architectures** — Kiến trúc nhiều tầng: web → app → database.
- **Queuing and messaging concepts (for example, publish/subscribe)** — Hàng đợi (SQS) và pub/sub (SNS: một message gửi tới nhiều subscriber).
- **Serverless technologies and patterns (for example, AWS Fargate, AWS Lambda)** — Serverless: không quản lý server (Lambda chạy hàm, Fargate chạy container).
- **Storage types with associated characteristics (for example, object, file, block)** — Object (S3), file (EFS/FSx), block (EBS) và đặc điểm của từng loại.
- **The orchestration of containers (for example, Amazon ECS, Amazon EKS)** — Điều phối container: ECS (của AWS) và EKS (Kubernetes managed).
- **When to use read replicas** — Dùng read replica (bản sao chỉ đọc) để chia tải đọc của database.
- **Workflow orchestration (for example, AWS Step Functions)** — Điều phối quy trình nhiều bước bằng Step Functions.

Skills in:
- **Designing event-driven, microservice, and/or multi-tier architectures based on requirements** — Chọn và thiết kế kiểu kiến trúc phù hợp yêu cầu đề bài.
- **Determining scaling strategies for components used in an architecture design** — Chọn cách scale cho từng thành phần.
- **Determining the AWS services required to achieve loose coupling based on requirements** — Chọn SQS/SNS/EventBridge/Kinesis... để tách rời thành phần.
- **Determining when to use containers** — Khi nào nên dùng container.
- **Determining when to use serverless technologies and patterns** — Khi nào nên dùng serverless.
- **Recommending appropriate compute, storage, networking, and database technologies based on requirements** — Đề xuất compute/storage/network/database đúng yêu cầu.
- **Using purpose-built AWS services for workloads** — Dùng dịch vụ "chuyên dụng" thay vì tự dựng (vd dùng DynamoDB thay vì tự cài DB trên EC2).

#### 2.2 Design highly available and/or fault-tolerant architectures (Thiết kế kiến trúc sẵn sàng cao và/hoặc chịu lỗi)

High availability (sẵn sàng cao) = hệ thống ít khi ngừng phục vụ. Fault tolerance (chịu lỗi) = một phần hỏng mà hệ thống vẫn chạy.

Knowledge of:
- **AWS global infrastructure (for example, Availability Zones, AWS Regions, Amazon Route 53)** — Triển khai nhiều AZ/Region; Route 53 (DNS) để chuyển hướng traffic khi lỗi.
- **AWS managed services with appropriate use cases (for example, Amazon Comprehend, Amazon Polly)** — Biết công dụng các dịch vụ AI managed: Comprehend (phân tích văn bản), Polly (chuyển văn bản thành giọng nói).
- **Basic networking concepts (for example, route tables)** — Khái niệm mạng cơ bản như bảng định tuyến.
- **Disaster recovery (DR) strategies (for example, backup and restore, pilot light, warm standby, active-active failover, recovery point objective [RPO], recovery time objective [RTO])** — 4 chiến lược DR từ rẻ/chậm đến đắt/nhanh; RPO = chấp nhận mất tối đa bao nhiêu dữ liệu (tính theo thời gian), RTO = phải khôi phục trong bao lâu.
- **Distributed design patterns** — Mẫu thiết kế hệ phân tán.
- **Failover strategies** — Chiến lược chuyển sang hệ thống dự phòng khi lỗi.
- **Immutable infrastructure** — Hạ tầng bất biến: không sửa server đang chạy, mà thay bằng bản mới (liên quan IaC, AMI, container).
- **Load balancing concepts (for example, ALB)** — Load balancer phân phối traffic qua nhiều AZ và bỏ qua instance lỗi (health check).
- **Proxy concepts (for example, Amazon RDS Proxy)** — RDS Proxy gom kết nối DB, hữu ích khi Lambda mở quá nhiều connection.
- **Service quotas and throttling (for example, how to configure the service quotas for a workload in a standby environment)** — Giới hạn dịch vụ (quota) và throttling; nhớ tăng quota ở Region dự phòng.
- **Storage options and characteristics (for example, durability, replication)** — Độ bền dữ liệu (durability) và sao chép của các loại storage.
- **Workload visibility (for example, AWS X-Ray)** — Quan sát hệ thống; X-Ray để trace request qua nhiều service.

Skills in:
- **Determining automation strategies to ensure infrastructure integrity** — Tự động hoá (CloudFormation, Auto Scaling...) để hạ tầng nhất quán.
- **Determining the AWS services required to provide a highly available and/or fault-tolerant architecture across AWS Regions or Availability Zones** — Chọn dịch vụ để chạy multi-AZ / multi-Region.
- **Identifying metrics based on business requirements to deliver a highly available solution** — Chọn metric (CloudWatch) phù hợp mục tiêu kinh doanh.
- **Implementing designs to mitigate single points of failure** — Loại bỏ "single point of failure" (điểm mà hỏng một chỗ là sập cả hệ thống).
- **Implementing strategies to ensure the durability and availability of data (for example, backups)** — Đảm bảo dữ liệu bền và luôn truy cập được.
- **Selecting an appropriate DR strategy to meet business requirements** — Chọn chiến lược DR theo RPO/RTO và ngân sách.
- **Using AWS services that improve the reliability of legacy applications and applications not built for the cloud (for example, when application changes are not possible)** — Tăng độ tin cậy cho ứng dụng cũ mà không sửa code (vd đặt sau ALB + Auto Scaling, dùng RDS Multi-AZ).
- **Using purpose-built AWS services for workloads** — Dùng dịch vụ chuyên dụng phù hợp workload.

### Domain 3 — Design High-Performing Architectures (Thiết kế kiến trúc hiệu năng cao) — 24%

#### 3.1 Determine high-performing and/or scalable storage solutions (Chọn giải pháp lưu trữ hiệu năng cao / dễ mở rộng)

Knowledge of:
- **Hybrid storage solutions to meet business requirements** — Lưu trữ lai (on-premises + cloud), vd Storage Gateway.
- **Storage services with appropriate use cases (for example, Amazon S3, Amazon EFS, Amazon EBS)** — S3 (object, không giới hạn dung lượng), EFS (file share nhiều instance cùng mount), EBS (ổ đĩa gắn vào một EC2).
- **Storage types with associated characteristics (for example, object, file, block)** — Đặc điểm hiệu năng của từng loại storage.

Skills in:
- **Determining storage services and configurations that meet performance demands** — Chọn storage + cấu hình (vd loại EBS gp3/io2) đáp ứng IOPS/throughput.
- **Determining storage services that can scale to accommodate future needs** — Chọn storage tự mở rộng theo nhu cầu tương lai.

#### 3.2 Design high-performing and elastic compute solutions (Thiết kế compute hiệu năng cao và co giãn)

Knowledge of:
- **AWS compute services with appropriate use cases (for example, AWS Batch, Amazon EMR, AWS Fargate)** — Batch (chạy job hàng loạt), EMR (Hadoop/Spark big data), Fargate (container serverless).
- **Distributed computing concepts supported by AWS global infrastructure and edge services** — Tính toán phân tán dùng hạ tầng toàn cầu và edge.
- **Queuing and messaging concepts (for example, publish/subscribe)** — Hàng đợi và pub/sub để tách tải.
- **Scalability capabilities with appropriate use cases (for example, Amazon EC2 Auto Scaling, AWS Auto Scaling)** — Tự động tăng/giảm số instance theo tải.
- **Serverless technologies and patterns (for example, AWS Lambda, Fargate)** — Mẫu thiết kế serverless.
- **The orchestration of containers (for example, Amazon ECS, Amazon EKS)** — Điều phối container.

Skills in:
- **Decoupling workloads so that components can scale independently** — Tách workload để từng phần scale độc lập (vd đặt SQS giữa web và worker).
- **Identifying metrics and conditions to perform scaling actions** — Chọn metric/điều kiện để kích hoạt scale (CPU, độ dài hàng đợi...).
- **Selecting the appropriate compute options and features (for example, EC2 instance types) to meet business requirements** — Chọn loại EC2 phù hợp.
- **Selecting the appropriate resource type and size (for example, the amount of Lambda memory) to meet business requirements** — Chọn kích thước tài nguyên (vd memory Lambda — tăng memory cũng tăng CPU).

#### 3.3 Determine high-performing database solutions (Chọn giải pháp database hiệu năng cao)

Knowledge of:
- **AWS global infrastructure (for example, Availability Zones, AWS Regions)** — Đặt DB ở AZ/Region phù hợp.
- **Caching strategies and services (for example, Amazon ElastiCache)** — Cache với ElastiCache (Redis/Memcached).
- **Data access patterns (for example, read-intensive compared with write-intensive)** — Nhận diện workload thiên về đọc hay ghi.
- **Database capacity planning (for example, capacity units, instance types, Provisioned IOPS)** — Lập kế hoạch dung lượng: capacity unit (DynamoDB), instance type, Provisioned IOPS.
- **Database connections and proxies** — Quản lý kết nối DB, dùng proxy.
- **Database engines with appropriate use cases (for example, heterogeneous migrations, homogeneous migrations)** — Chọn engine; migration cùng engine (homogeneous) hay khác engine (heterogeneous).
- **Database replication (for example, read replicas)** — Sao chép DB.
- **Database types and services (for example, serverless, relational compared with non-relational, in-memory)** — Các loại DB: serverless, quan hệ (SQL) vs phi quan hệ (NoSQL), in-memory.

Skills in:
- **Configuring read replicas to meet business requirements** — Cấu hình read replica.
- **Designing database architectures** — Thiết kế kiến trúc database.
- **Determining an appropriate database engine (for example, MySQL compared with PostgreSQL)** — Chọn engine phù hợp.
- **Determining an appropriate database type (for example, Amazon Aurora, Amazon DynamoDB)** — Chọn loại DB: Aurora (quan hệ, hiệu năng cao) hay DynamoDB (NoSQL key-value).
- **Integrating caching to meet business requirements** — Đưa cache vào kiến trúc.

#### 3.4 Determine high-performing and/or scalable network architectures (Chọn kiến trúc mạng hiệu năng cao / dễ mở rộng)

Knowledge of:
- **Edge networking services with appropriate use cases (for example, Amazon CloudFront, AWS Global Accelerator)** — CloudFront (CDN, cache nội dung HTTP) vs Global Accelerator (tăng tốc TCP/UDP qua mạng AWS, IP tĩnh).
- **How to design network architecture (for example, subnet tiers, routing, IP addressing)** — Thiết kế subnet, định tuyến, chia dải IP (CIDR).
- **Load balancing concepts (for example, Application Load Balancer [ALB])** — Cân bằng tải.
- **Network connection options (for example, AWS VPN, AWS Direct Connect, AWS PrivateLink)** — Các cách kết nối: VPN, Direct Connect, PrivateLink (truy cập dịch vụ qua mạng riêng).

Skills in:
- **Creating a network topology for various architectures (for example, global, hybrid, multi-tier)** — Vẽ topology mạng cho kiến trúc toàn cầu, lai, nhiều tầng.
- **Determining network configurations that can scale to accommodate future needs** — Cấu hình mạng đủ chỗ mở rộng (vd chừa dải IP).
- **Determining the appropriate placement of resources to meet business requirements** — Đặt tài nguyên đúng chỗ (subnet, AZ, Region).
- **Selecting the appropriate load balancing strategy** — Chọn ALB / NLB / GWLB phù hợp.

#### 3.5 Determine high-performing data ingestion and transformation solutions (Chọn giải pháp thu nạp và biến đổi dữ liệu hiệu năng cao)

Knowledge of:
- **Data analytics and visualization services with appropriate use cases (for example, Amazon Athena, AWS Lake Formation, Amazon Quick)** — Athena (truy vấn SQL trực tiếp trên S3), Lake Formation (dựng và phân quyền data lake), Amazon Quick (dịch vụ trực quan hoá/BI — tên này ghi đúng như exam guide).
- **Data ingestion patterns (for example, frequency)** — Mẫu thu nạp dữ liệu: theo lô hay liên tục, tần suất bao nhiêu.
- **Data transfer services with appropriate use cases (for example, AWS DataSync, AWS Storage Gateway)** — DataSync (chuyển dữ liệu online), Storage Gateway (nối storage on-prem với AWS).
- **Data transformation services with appropriate use cases (for example, AWS Glue)** — Glue: ETL (trích xuất – biến đổi – nạp) serverless.
- **Secure access to ingestion access points** — Bảo mật điểm nhận dữ liệu.
- **Sizes and speeds needed to meet business requirements** — Ước lượng dung lượng và tốc độ cần.
- **Streaming data services with appropriate use cases (for example, Amazon Kinesis)** — Dữ liệu streaming (luồng liên tục) với Kinesis.

Skills in:
- **Building and securing data lakes** — Dựng và bảo mật data lake (kho dữ liệu thô, thường trên S3).
- **Designing data streaming architectures** — Thiết kế kiến trúc streaming.
- **Designing data transfer solutions** — Thiết kế giải pháp chuyển dữ liệu.
- **Implementing visualization strategies** — Trực quan hoá dữ liệu.
- **Selecting appropriate compute options for data processing (for example, Amazon EMR)** — Chọn compute xử lý dữ liệu.
- **Selecting appropriate configurations for ingestion** — Cấu hình thu nạp phù hợp.
- **Transforming data between formats (for example, .csv to .parquet)** — Đổi định dạng dữ liệu (CSV → Parquet dạng cột, truy vấn nhanh và rẻ hơn).

### Domain 4 — Design Cost-Optimized Architectures (Thiết kế kiến trúc tối ưu chi phí) — 20%

Lưu ý: cả 4 task trong domain này đều lặp lại 2 mục kiến thức chung: **AWS cost management service features (for example, cost allocation tags, multi-account billing)** — tag phân bổ chi phí, gộp hoá đơn nhiều account; và **AWS cost management tools with appropriate use cases (for example, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report)** — Cost Explorer (xem/phân tích chi phí), Budgets (đặt ngân sách + cảnh báo), CUR (báo cáo chi tiết nhất).

#### 4.1 Design cost-optimized storage solutions (Thiết kế lưu trữ tối ưu chi phí)

Knowledge of:
- **Access options (for example, an S3 bucket with Requester Pays object storage)** — Requester Pays: người tải dữ liệu trả phí tải, không phải chủ bucket.
- **AWS cost management service features (for example, cost allocation tags, multi-account billing)** — (xem lưu ý đầu domain).
- **AWS cost management tools with appropriate use cases (for example, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report)** — (xem lưu ý đầu domain).
- **AWS storage services with appropriate use cases (for example, Amazon FSx, Amazon EFS, Amazon S3, Amazon EBS)** — Chọn storage theo use case và giá.
- **Backup strategies** — Chiến lược backup.
- **Block storage options (for example, hard disk drive [HDD] volume types, solid state drive [SSD] volume types)** — Loại EBS: SSD (gp3, io2) vs HDD (st1, sc1 — rẻ, hợp đọc tuần tự).
- **Data lifecycles** — Vòng đời dữ liệu.
- **Hybrid storage options (for example, AWS DataSync, AWS Transfer Family, AWS Storage Gateway)** — Lựa chọn lưu trữ lai.
- **Storage access patterns** — Mẫu truy cập (thường xuyên, hiếm, không đoán được).
- **Storage tiering (for example, cold tiering for object storage)** — Phân tầng: S3 Standard → Infrequent Access → Glacier (lạnh, rẻ).
- **Storage types with associated characteristics (for example, object, file, block)** — Đặc điểm từng loại storage.

Skills in:
- **Designing appropriate storage strategies (for example, batch uploads to Amazon S3 compared with individual uploads)** — Chiến lược lưu trữ (vd upload theo lô để giảm số request).
- **Determining the correct storage size for a workload** — Chọn đúng dung lượng.
- **Determining the lowest cost method of transferring data for a workload to AWS storage** — Cách chuyển dữ liệu rẻ nhất (online qua mạng vs Snow Family).
- **Determining when storage auto scaling is required** — Khi nào cần storage tự mở rộng.
- **Managing S3 object lifecycles** — Lifecycle rule: tự chuyển tầng/xoá object theo thời gian.
- **Selecting the appropriate backup and/or archival solution** — Chọn backup/lưu trữ dài hạn.
- **Selecting the appropriate service for data migration to storage services** — Chọn dịch vụ di chuyển dữ liệu.
- **Selecting the appropriate storage tier** — Chọn tầng lưu trữ.
- **Selecting the correct data lifecycle for storage** — Chọn vòng đời dữ liệu đúng.
- **Selecting the most cost-effective storage service for a workload** — Chọn dịch vụ lưu trữ rẻ nhất mà vẫn đáp ứng yêu cầu.

#### 4.2 Design cost-optimized compute solutions (Thiết kế compute tối ưu chi phí)

Knowledge of:
- **AWS cost management service features (for example, cost allocation tags, multi-account billing)** — (xem lưu ý đầu domain).
- **AWS cost management tools with appropriate use cases (for example, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report)** — (xem lưu ý đầu domain).
- **AWS global infrastructure (for example, Availability Zones, AWS Regions)** — Giá khác nhau giữa Region; phí truyền dữ liệu giữa AZ/Region.
- **AWS purchasing options (for example, Spot Instances, Reserved Instances, Savings Plans)** — Cách mua: On-Demand, Spot (rẻ nhưng có thể bị thu hồi), Reserved Instances / Savings Plans (cam kết 1–3 năm để giảm giá).
- **Distributed compute strategies (for example, edge processing)** — Xử lý tại edge.
- **Hybrid compute options (for example, AWS Outposts)** — Outposts: hạ tầng AWS đặt tại data center của khách.
- **Instance types, families, and sizes (for example, memory optimized, compute optimized, virtualization)** — Họ instance: general purpose, compute optimized, memory optimized...
- **Optimization of compute utilization (for example, containers, serverless computing, microservices)** — Tận dụng tài nguyên tốt hơn bằng container/serverless.
- **Scaling strategies (for example, auto scaling, hibernation)** — Auto scaling, hibernation (ngủ đông EC2, giữ RAM để khởi động nhanh).

Skills in:
- **Determining an appropriate load balancing strategy (for example, Application Load Balancer [Layer 7] compared with Network Load Balancer [Layer 4] compared with Gateway Load Balancer)** — ALB (HTTP, Layer 7), NLB (TCP/UDP, Layer 4, hiệu năng rất cao), GWLB (đưa traffic qua thiết bị bảo mật bên thứ ba).
- **Determining appropriate scaling methods and strategies for elastic workloads (for example, horizontal compared with vertical, EC2 hibernation)** — Chọn cách scale.
- **Determining cost-effective AWS compute services with appropriate use cases (for example, AWS Lambda, Amazon EC2, AWS Fargate)** — So sánh chi phí Lambda / EC2 / Fargate theo kiểu tải.
- **Determining the required availability for different classes of workloads (for example, production workloads, non-production workloads)** — Môi trường dev/test không cần HA như production → tiết kiệm.
- **Selecting the appropriate instance family for a workload** — Chọn họ instance.
- **Selecting the appropriate instance size for a workload** — Chọn kích thước instance (right-sizing).

#### 4.3 Design cost-optimized database solutions (Thiết kế database tối ưu chi phí)

Knowledge of:
- **AWS cost management service features (for example, cost allocation tags, multi-account billing)** — (xem lưu ý đầu domain).
- **AWS cost management tools with appropriate use cases (for example, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report)** — (xem lưu ý đầu domain).
- **Caching strategies** — Cache để giảm tải và chi phí DB.
- **Data retention policies** — Chính sách lưu giữ dữ liệu.
- **Database capacity planning (for example, capacity units)** — Lập kế hoạch dung lượng (vd DynamoDB on-demand vs provisioned capacity).
- **Database connections and proxies** — Kết nối và proxy DB.
- **Database engines with appropriate use cases (for example, heterogeneous migrations, homogeneous migrations)** — Chọn engine và kiểu migration.
- **Database replication (for example, read replicas)** — Sao chép DB.
- **Database types and services (for example, relational compared with non-relational, Amazon Aurora, Amazon DynamoDB)** — Các loại DB và dịch vụ.

Skills in:
- **Designing appropriate backup and retention policies (for example, snapshot frequency)** — Tần suất snapshot và thời gian giữ.
- **Determining an appropriate database engine (for example, MySQL compared with PostgreSQL)** — Chọn engine.
- **Determining cost-effective AWS database services with appropriate use cases (for example, DynamoDB compared with Amazon RDS, serverless)** — So sánh chi phí DynamoDB / RDS / serverless.
- **Determining cost-effective AWS database types (for example, time series format, columnar format)** — Chọn DB theo dạng dữ liệu: chuỗi thời gian, dạng cột (vd Redshift).
- **Migrating database schemas and data to different locations and/or different database engines** — Di chuyển schema + dữ liệu (AWS DMS; đổi engine thì cần chuyển đổi schema).

#### 4.4 Design cost-optimized network architectures (Thiết kế mạng tối ưu chi phí)

Knowledge of:
- **AWS cost management service features (for example, cost allocation tags, multi-account billing)** — (xem lưu ý đầu domain).
- **AWS cost management tools with appropriate use cases (for example, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report)** — (xem lưu ý đầu domain).
- **Load balancing concepts (for example, ALB)** — Chi phí load balancer.
- **NAT gateways (for example, NAT instance costs compared with NAT gateway costs)** — So sánh chi phí NAT instance (tự quản) vs NAT gateway (managed).
- **Network connectivity (for example, private lines, dedicated lines, VPNs)** — Đường truyền riêng, chuyên dụng, VPN.
- **Network routing, topology, and peering (for example, AWS Transit Gateway, VPC peering)** — Nối nhiều VPC: VPC peering (1–1) vs Transit Gateway (hub trung tâm).
- **Network services with appropriate use cases (for example, DNS)** — Dịch vụ mạng như DNS (Route 53).

Skills in:
- **Configuring appropriate NAT gateway types for a network (for example, a single shared NAT gateway compared with NAT gateways for each Availability Zone)** — Một NAT gateway dùng chung (rẻ nhưng là single point of failure) vs mỗi AZ một cái (HA nhưng đắt hơn).
- **Configuring appropriate network connections (for example, AWS Direct Connect compared with VPN compared with internet)** — Chọn kết nối theo chi phí/băng thông/độ ổn định.
- **Configuring appropriate network routes to minimize network transfer costs (for example, Region to Region, Availability Zone to Availability Zone, private to public, AWS Global Accelerator, VPC endpoints)** — Giảm phí truyền dữ liệu (vd dùng VPC endpoint để S3 traffic không đi qua NAT gateway).
- **Determining strategic needs for content delivery networks (CDNs) and edge caching** — Khi nào CDN/edge cache giúp giảm chi phí.
- **Reviewing existing workloads for network optimizations** — Rà soát workload hiện có để tối ưu mạng.
- **Selecting an appropriate throttling strategy** — Chọn cách giới hạn tốc độ request (vd throttling ở API Gateway).
- **Selecting the appropriate bandwidth allocation for a network device (for example, a single VPN compared with multiple VPNs, Direct Connect speed)** — Chọn băng thông phù hợp.

## Phạm vi dịch vụ (tóm tắt)

Exam guide có danh sách **In-Scope AWS Services** (không đầy đủ tuyệt đối, có thể thay đổi). Các nhóm và dịch vụ tiêu biểu:

| Nhóm | Dịch vụ tiêu biểu trong danh sách |
|---|---|
| Compute / Serverless / Containers | EC2, EC2 Auto Scaling, Elastic Beanstalk, Batch, Outposts, Lambda, Fargate, ECR, ECS, EKS |
| Storage | S3, S3 Glacier, EBS, EFS, FSx, Storage Gateway, AWS Backup |
| Database | RDS, Aurora, Aurora Serverless, DynamoDB, ElastiCache, Redshift, DocumentDB, Neptune, Keyspaces |
| Networking | VPC, Route 53, CloudFront, ELB, Global Accelerator, Direct Connect, Site-to-Site VPN, Client VPN, Transit Gateway, PrivateLink |
| Security | IAM, IAM Identity Center, KMS, CloudHSM, ACM, Secrets Manager, Cognito, GuardDuty, Macie, Inspector, Detective, Security Hub, Shield, WAF, Firewall Manager, Network Firewall, Directory Service, RAM, Artifact |
| Application Integration | SQS, SNS, EventBridge, Step Functions, MQ, AppFlow |
| Analytics | Athena, Glue, Kinesis, EMR, Lake Formation, MSK, OpenSearch Service, Amazon Quick, Redshift, Data Exchange, Data Pipeline |
| Management & Governance | CloudFormation, CloudWatch, CloudTrail, Config, Organizations, Control Tower, Systems Manager, Compute Optimizer, Service Catalog, Well-Architected Tool, AWS CLI... |
| Migration & Transfer | DMS, DataSync, Snow Family, Transfer Family, Application Migration Service, Application Discovery Service |
| Cost Management | Budgets, Cost Explorer, Cost and Usage Report, Savings Plans |
| Khác | API Gateway, Amplify, X-Ray, các dịch vụ AI (Comprehend, Polly, Rekognition, Textract, Transcribe, Translate, Lex, SageMaker AI), Kinesis Video Streams |

Danh sách đầy đủ: https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html

**Gợi ý cho track DevOps:** những phần trùng nhiều nhất với công việc DevOps là VPC/networking, IAM, EC2 + Auto Scaling + ELB, container (ECS/EKS/ECR), CloudFormation, CloudWatch/CloudTrail, S3, RDS. Đây nên là trọng tâm học trước.

## Phong cách câu hỏi

- **Câu tình huống (scenario-based)**: thường mô tả một công ty, hệ thống hiện tại và yêu cầu ("A company runs... The company needs to..."). Đọc kỹ ràng buộc.
- **Từ khoá quyết định đáp án**: "MOST cost-effective", "LEAST operational overhead", "MOST secure", "highly available", "with minimal changes to the application". Cùng một bài toán, đổi từ khoá là đổi đáp án đúng. Gạch chân từ khoá trước khi đọc đáp án.
- **Hai dạng**: multiple choice (1 đúng / 4) và multiple response (≥ 2 đúng / ≥ 5, đề ghi rõ "Select TWO" hoặc "Select THREE").
- **Distractor hợp lý**: đáp án sai thường "nghe có vẻ đúng" — vẫn chạy được nhưng không thoả hết yêu cầu (đắt hơn, nhiều việc vận hành hơn, không HA...).
- **Không trừ điểm khi đoán sai** — câu bỏ trống tính là sai, nên **luôn chọn đáp án** cho mọi câu.
- **15 câu không tính điểm** nằm lẫn trong đề, không biết câu nào → làm tất cả nghiêm túc.
- **Tính điểm bù trừ**: không cần đạt từng domain, chỉ cần tổng ≥ 720.
- **Với người đọc tiếng Anh trung bình**: câu hỏi dài, nhiều chữ → đăng ký **ESL +30** (130 → 160 phút), luyện đọc đề thi thử bằng tiếng Anh, học thuộc các cụm từ khoá ở trên.

## Tài liệu ôn chính hãng

- **Exam guide SAA-C03** (đọc bản tiếng Anh, đây là "đề cương" chính thức): https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html
- **Trang chứng chỉ + kế hoạch ôn 4 bước** (Practice Question Set → học lấp lỗ hổng → ôn luyện → Practice Exam): https://aws.amazon.com/certification/certified-solutions-architect-associate/
- **AWS Skill Builder — trang Exam Prep SAA-C03**: https://skillbuilder.aws/category/exam-prep/solutions-architect-associate-SAA-C03
  - **Official Practice Question Set** — 20 câu, **miễn phí**, đúng phong cách đề thật, có giải thích (theo trang https://aws.amazon.com/certification/certification-prep/).
  - **Exam Prep course (bản miễn phí)** — khoá ~2 giờ, đi qua từng domain và câu hỏi mẫu.
  - **Official Practice Exam** và **Exam Prep Enhanced** — cần **subscription** (Individual từ 29 USD/tháng theo trang certification-prep).
- **Webinar / Exam Readiness miễn phí**: https://aws.amazon.com/training/events/
- **AWS Training Live trên Twitch (miễn phí)**: https://twitch.tv/awstraininglive
- **AWS Well-Architected Framework** — nền tảng tư duy của cả đề thi (exam guide nói đề kiểm tra khả năng thiết kế "based on the AWS Well-Architected Framework"). Link docs chưa được fetch trong session này — sẽ xác minh khi dùng làm tài liệu bài học.
- **Chính sách thi**: https://aws.amazon.com/certification/policies/before-testing/ (ESL +30, giá, giấy tờ) · https://aws.amazon.com/certification/policies/after-testing/ (thi lại, kết quả)

**Không dùng** các trang "exam dump", "braindump", "real exam questions": vi phạm thoả thuận thi của AWS và có thể bị thu hồi chứng chỉ.

## Những điểm chưa xác minh

- Danh sách ngôn ngữ của **tài liệu ôn tập** trên Skill Builder (trang Skill Builder không đọc được nội dung khi fetch).
- Ngày chính xác thay đổi của exam guide bản 1.1 có hiệu lực trên đề thi (AWS chỉ nói "khoảng 1 tháng sau khi công bố").
- Mốc thời gian phát hành SAA-C04 (nếu có): **không tìm thấy thông báo chính hãng**.
- Yêu cầu kỹ thuật cụ thể cho thi online (máy tính, phòng thi): trang "Before Testing" không liệt kê chi tiết khi fetch.

## Nguồn & ngày truy cập (2026-11-05)

| Nguồn | URL |
|---|---|
| Trang chứng chỉ SAA | https://aws.amazon.com/certification/certified-solutions-architect-associate/ |
| Exam guide SAA-C03 (tổng quan) | https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html |
| Domain 1 | https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain1.html |
| Domain 2 | https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain2.html |
| Domain 3 | https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html |
| Domain 4 | https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain4.html |
| Technologies and Concepts | https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-technologies-concepts.html |
| In-Scope Services | https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html |
| Revisions | https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-revisions.html |
| Before Testing (ESL +30, giá, ID) | https://aws.amazon.com/certification/policies/before-testing/ |
| After Testing (thi lại, kết quả) | https://aws.amazon.com/certification/policies/after-testing/ |
| Certification prep | https://aws.amazon.com/certification/certification-prep/ |
| Blog: cập nhật chứng chỉ 09/2026 | https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/ |
| Blog: DVA-C03 & SAP-C03 (27/10/2026) | https://aws.amazon.com/blogs/training-and-certification/register-now-updated-developer-associate-and-solutions-architect-professional-exams/ |
