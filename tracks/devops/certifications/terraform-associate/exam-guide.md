# HashiCorp Certified: Terraform Associate (004) — Tóm tắt exam guide

> Nguồn chính hãng: [Trang chứng chỉ Terraform Associate](https://developer.hashicorp.com/certifications/terraform-associate) · [Exam Content List 004](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004) · [Learning Path 004](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-study-004) · [Sample Questions 004](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-questions-004) · Kiểm tra ngày: 2026-11-05
>
> Nhắc người học: thông tin phí, thời lượng, chính sách có thể thay đổi. **Mở lại trang chứng chỉ chính hãng để kiểm tra trước khi đăng ký thi.**

## Thông tin kỳ thi

| Mục | Giá trị |
|---|---|
| Mã đề / phiên bản hiện hành | **Terraform Associate (004)** — kiểm tra trên **Terraform 1.12**, có nội dung về **HCP Terraform** |
| Phiên bản mới sắp áp dụng | Không thấy thông báo phiên bản 005 trên trang chính hãng (ngày 2026-11-05). Bản 003 không còn là bản hiện hành: trang chứng chỉ chỉ ghi 004, và đường dẫn ôn tập `certification-003` hiện mở ra trang "Associate Prep (004)". Ngày ngừng chính thức của 003 / ngày phát hành 004: **chưa xác minh** |
| Format | Trắc nghiệm (multiple choice). Trang Sample Questions mô tả 3 dạng câu: **True/False**, **Multiple choice** (1 đáp án), **Multiple answer** (nhiều đáp án — đề ghi rõ cần chọn mấy đáp án) |
| Số câu | **Chưa xác minh** — HashiCorp không công bố số câu trên trang chứng chỉ. Nhiều nguồn bên thứ ba ghi "khoảng 57 câu", nhưng chính họ ghi chú đây là con số không chính thức |
| Thời lượng | 60 phút (1 hour) |
| Điểm đạt | **Không công bố** — bài trợ giúp của HashiCorp Certifications (kết quả tìm kiếm, không mở được trang) ghi "We do not publish our passing scores at this time". Kết quả Associate hiện ngay là Pass/Fail, không kèm % điểm |
| Phí thi | **$70.50 USD** + thuế/phí địa phương. **Không** kèm lượt thi lại miễn phí ("Free retake not included") |
| Ngôn ngữ đề | Tiếng Anh (English) |
| Hình thức | Online proctored (thi online có giám thị qua webcam). Phải tuân thủ quy định về giấy tờ tùy thân, hệ thống máy và phòng thi — xem [Exam appointment rules and requirements](https://hashicorp-certifications.zendesk.com/hc/en-us/articles/26234761626125) (trang này chặn truy cập tự động; nội dung chi tiết **chưa xác minh**) |
| Hiệu lực | 2 năm |
| Thi lại khi trượt | Theo kết quả tìm kiếm bài trợ giúp chính hãng ([retake rules](https://hashicorp-certifications.zendesk.com/hc/en-us/articles/360049773991-What-are-the-HashiCorp-exam-retake-rules)): chờ 7 ngày giữa 2 lần thi, tối đa 4 lần trong 365 ngày liên tục. **Chỉ đọc được snippet, chưa mở được trang** |
| Hỗ trợ người không nói tiếng Anh bản xứ | **Không tìm thấy chính sách cộng giờ dành riêng cho người không nói tiếng Anh bản xứ (ESL)** trên nguồn chính hãng. HashiCorp có chính sách "reasonable accommodation" chung: gửi yêu cầu **ít nhất 3 ngày làm việc trước ngày thi**, yêu cầu thêm giờ qua nút "Request Accommodation" trên màn hình đặt lịch của Certiverse ([bài trợ giúp](https://hashicorp-certifications.zendesk.com/hc/en-us/articles/360046049832-I-require-special-accommodations-for-my-exam-what-should-I-do) — chỉ đọc được snippet). Có cấp thêm giờ cho lý do ngôn ngữ hay không: **chưa xác minh** — nếu muốn, hãy hỏi trực tiếp bộ phận hỗ trợ chứng chỉ của HashiCorp |
| Điều kiện tiên quyết | Không bắt buộc. Khuyến nghị: kỹ năng terminal cơ bản; hiểu kiến trúc on-premises và cloud. Kinh nghiệm thực tế dùng Terraform trong production là tốt nhất, nhưng có thể tự luyện các objective trên môi trường demo cá nhân |

### Gia hạn chứng chỉ (recertification)
Theo trang chứng chỉ (đọc ngày 2026-11-05):
- **Đang có 004 còn hạn**: thi đậu Terraform Infrastructure Engineer Professional, hoặc Terraform Authoring and Operations Advanced (AWS/Azure) → gia hạn Associate; hoặc thi lại 004 từ **6 tháng trước ngày hết hạn** để gia hạn chính chứng chỉ đang có.
- **Đang có 002/003 còn hạn**: thi Professional/Advanced để gia hạn; hoặc thi 004 từ 6 tháng trước ngày hết hạn → nhận chứng chỉ 004 **mới, riêng biệt** (ngày hết hạn của chứng chỉ cũ giữ nguyên).
- **Đã hết hạn**: thi Associate bản hiện hành bất kỳ lúc nào → nhận chứng chỉ mới.

### Thay đổi so với 003 (chính hãng liệt kê 4 chủ đề mới)
| Objective | Nội dung mới |
|---|---|
| 4f | `depends_on` và lifecycle rule `create_before_destroy` |
| 4g | Validate configuration bằng custom conditions |
| 4h | Ephemeral values và write-only arguments |
| 8c | Tổ chức và dùng HCP Terraform workspaces và projects |

> Hệ quả thực tế: tài liệu/khoá học viết cho 003 vẫn dùng được phần lớn, nhưng **thiếu 4 chủ đề trên** và thường dùng tên cũ "Terraform Cloud" (nay là **HCP Terraform**).

## Domain & tỷ trọng

HashiCorp **không công bố tỷ trọng %** cho từng domain. Cột "Số câu ước tính" dưới đây do mentor tự chia **theo số objective con** của mỗi domain (tổng 37 objective), cho một đề thi thử 57 câu — **đây là ước tính để luyện tập, không phải số liệu chính hãng**.

| # | Domain | Số objective | Tỷ trọng | Số câu ước tính (đề thi thử 57 câu) |
|---|---|---|---|---|
| 1 | Infrastructure as Code (IaC) with Terraform | 3 (1a–1c) | Không công bố | 5 |
| 2 | Terraform fundamentals | 4 (2a–2d) | Không công bố | 6 |
| 3 | Core Terraform workflow | 7 (3a–3g) | Không công bố | 11 |
| 4 | Terraform configuration | 8 (4a–4h) | Không công bố | 12 |
| 5 | Terraform modules | 4 (5a–5d) | Không công bố | 6 |
| 6 | Terraform state management | 4 (6a–6d) | Không công bố | 6 |
| 7 | Maintain infrastructure with Terraform | 3 (7a–7c) | Không công bố | 5 |
| 8 | HCP Terraform | 4 (8a–8d) | Không công bố | 6 |
| | **Tổng** | **37** | | **57** |

## Objective chi tiết (dịch & giải thích)

> Tên objective giữ nguyên tiếng Anh theo [Exam Content List 004](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004). Ở cuối mỗi dòng là tên tài liệu chính hãng HashiCorp gợi ý cho objective đó. Chính hãng ghi rõ: tutorial có thể dùng một cloud provider cụ thể làm ví dụ, nhưng **đề thi không yêu cầu kiến thức riêng của provider nào** (AWS, Azure...).

### Domain 1 — Infrastructure as Code (IaC) with Terraform (Hạ tầng dưới dạng code với Terraform)
- **1a Explain what IaC is** — Giải thích IaC là gì: mô tả hạ tầng (server, network, database...) bằng file code thay vì click tay trên console; code được lưu trong Git, review và chạy lặp lại được. *Tài liệu: What is Terraform?; Infrastructure as Code in a Private or Public Cloud; Introduction to Infrastructure as Code.*
- **1b Describe the advantages of IaC patterns** — Nêu lợi ích của IaC: tự động hoá, nhất quán giữa các môi trường, version control (lịch sử thay đổi), review được, tái sử dụng, giảm lỗi thao tác tay. *Tài liệu: Why Terraform; Infrastructure as Code in a Private or Public Cloud; Introduction to Infrastructure as Code.*
- **1c Explain how Terraform manages multi-cloud, hybrid cloud, and service-agnostic workflows** — Giải thích vì sao Terraform dùng được cho nhiều cloud cùng lúc, kết hợp on-prem + cloud, và cả dịch vụ không phải cloud (DNS, GitHub, monitoring...): nhờ một workflow chung + hệ thống provider. *Tài liệu: Multi-Cloud Deployment; Introduction to Infrastructure as Code.*

### Domain 2 — Terraform fundamentals (Kiến thức nền tảng Terraform)
- **2a Install and version Terraform providers** — Cài và ghim phiên bản provider: khối `required_providers`, version constraint (`~>`, `>=`), file khoá `.terraform.lock.hcl`, nâng cấp provider bằng `terraform init -upgrade`. *Tài liệu: Providers; Specifying Provider Requirements; Dependency Lock File; Provider Block Reference; Lock and Upgrade Provider Versions; Initialize Terraform Configuration.*
- **2b Describe how Terraform uses providers** — Hiểu provider là plugin để Terraform gọi API của từng nền tảng; Terraform tải provider khi `init`; cấu hình provider bằng khối `provider`. *Tài liệu: Provider Block Reference; Provider Overview; Provider Requirements; How Terraform Works with Plugins; Initialize Terraform Configuration.*
- **2c Write Terraform configuration using multiple providers** — Viết config dùng nhiều provider (hoặc nhiều cấu hình của cùng một provider, ví dụ 2 region): dùng `alias` và chỉ định `provider = ...` trong resource. *Tài liệu: Provider Block Reference; Provider Requirements; Define Infrastructure with Terraform Resources.*
- **2d Explain how Terraform uses and manages state** — Giải thích state (trạng thái) là gì và để làm gì: ánh xạ resource trong code ↔ đối tượng thật, lưu metadata, giúp tính plan; vì sao không sửa tay file state. *Tài liệu: Purpose of Terraform State; Manage Resources in Terraform State.*

### Domain 3 — Core Terraform workflow (Quy trình làm việc cốt lõi)
- **3a Describe the Terraform workflow** — Mô tả vòng đời Write → Plan → Apply (và các lệnh `init`, `validate`, `plan`, `apply`, `destroy`). *Tài liệu: Core Terraform Workflow; Create Infrastructure; Create a Terraform Plan; Apply Terraform Configuration; Initialize Terraform Configuration.*
- **3b Initialize a Terraform working directory** — Biết `terraform init` làm gì: tải provider, module, cấu hình backend, tạo/đọc lock file. *Tài liệu: Dependency Lock File; Command: init; Initialize Terraform Configuration.*
- **3c Validate a Terraform configuration** — Dùng `terraform validate` kiểm tra cú pháp và tính nhất quán nội bộ của config (không gọi API thật). *Tài liệu: Command: validate; Validate your Configuration.*
- **3d Generate and review an execution plan for Terraform** — Tạo và đọc execution plan (kế hoạch thực thi): ký hiệu `+`, `-`, `~`, `-/+`; lưu plan ra file (`-out`); hiểu resource graph (đồ thị phụ thuộc). *Tài liệu: Resource Graph; Command: plan; Create a Terraform Plan.*
- **3e Apply changes to infrastructure with Terraform** — Dùng `terraform apply` (có/không có file plan), hiểu khi nào Terraform hỏi xác nhận. *Tài liệu: Command: apply; Apply Terraform Configuration.*
- **3f Destroy Terraform-managed infrastructure** — Dùng `terraform destroy` để xoá toàn bộ hạ tầng do Terraform quản lý; hiểu hệ quả. *Tài liệu: Command: destroy; Destroy Infrastructure.*
- **3g Apply formatting and style adjustments to a configuration** — Dùng `terraform fmt` để định dạng code theo chuẩn. *Tài liệu: Command: fmt; Format the Configuration.*

### Domain 4 — Terraform configuration (Viết cấu hình Terraform)
- **4a Use and differentiate `resource` and `data` blocks** — Phân biệt `resource` (Terraform tạo và quản lý) với `data` (data source — chỉ đọc thông tin có sẵn). *Tài liệu: Resources; Data Sources; Query Data Sources.*
- **4b Refer to resource attributes and create cross-resource references** — Tham chiếu thuộc tính resource (`aws_instance.web.id`...) và dùng tham chiếu đó để nối các resource với nhau; hiểu cú pháp resource address. *Tài liệu: Resource Addressing; References to Named Values; Create Resource Dependencies.*
- **4c Use variables and outputs** — Khai báo `variable` (kiểu, default, description, validation), truyền giá trị (file `.tfvars`, `-var`, biến môi trường `TF_VAR_`), khai báo `output`. *Tài liệu: Manage values in modules; Output Block Reference; Variable Block Reference; Customize Terraform Configuration with Variables; Output Data from Terraform.*
- **4d Understand and use complex types** — Dùng kiểu phức hợp: `list`, `map`, `set`, `object`, `tuple`. *Tài liệu: Complex Types; Customize Terraform Configuration with Variables.*
- **4e Write dynamic configuration using expressions and functions** — Viết config động bằng expression (biểu thức điều kiện, `for`, splat, `dynamic` block) và built-in function. *Tài liệu: Built-in Functions; Create Dynamic Expressions; Perform Dynamic Operations with Functions.*
- **4f Define resource dependencies in configuration** *(mới ở 004)* — Khai báo phụ thuộc: phụ thuộc ngầm định (qua tham chiếu) và tường minh với `depends_on`; lifecycle rule `create_before_destroy`. *Tài liệu: Resource Graph; Create Resource Dependencies.*
- **4g Validate configuration using custom conditions** *(mới ở 004)* — Dùng custom conditions để kiểm tra: `validation` trong variable, `precondition`/`postcondition`, khối `check`. *Tài liệu: Validate Your Configuration; Use Checks to Validate Infrastructure; Validate Modules with Custom Conditions.*
- **4h Understand best practices for managing sensitive data, including secrets management with Vault** *(mới ở 004)* — Thực hành tốt khi xử lý dữ liệu nhạy cảm: `sensitive = true`, hiểu rằng giá trị nhạy cảm vẫn có thể nằm trong state, ephemeral values và write-only arguments (chính hãng nêu trong danh sách chủ đề mới), lấy secret từ Vault qua Vault provider. *Tài liệu: Manage Sensitive Data; Vault Provider for Terraform; Upgrade RDS Major Version; Protect Sensitive Input Variables; Inject Secrets into Terraform Using the Vault Provider.*

### Domain 5 — Terraform modules (Module)
- **5a Explain how Terraform sources modules** — Biết module lấy từ đâu: đường dẫn local, Terraform Registry (public/private), Git, HTTP... qua tham số `source`. *Tài liệu: Find and Use Modules; Modules Overview; Use Registry Modules in Configuration.*
- **5b Describe variable scope within modules** — Hiểu phạm vi biến: module con không tự thấy biến của module cha; phải truyền qua input variable và lấy kết quả ra qua output. *Tài liệu: Module Block Reference; Manage values in modules; Build and Use a Local Module.*
- **5c Use modules in configuration** — Gọi module bằng khối `module`, truyền input, dùng output của module (`module.<tên>.<output>`), ghép nhiều module (composition). *Tài liệu: Module Composition; Output Block Reference; Manage values in modules; Use Registry Modules in Configuration.*
- **5d Manage module versions** — Ghim phiên bản module bằng tham số `version` (áp dụng cho module từ registry). *Tài liệu: Module Block Reference: Version Argument; Use Registry Modules in Configuration.*

### Domain 6 — Terraform state management (Quản lý state)
- **6a Describe the local backend** — Mô tả backend `local`: state lưu ở file `terraform.tfstate` trên máy; mặc định khi không cấu hình backend. *Tài liệu: Backend Block Configuration; Backend Type: local; Initialize Terraform Configuration.*
- **6b Describe state locking** — Giải thích state locking (khoá state): tránh 2 người/2 pipeline cùng ghi state một lúc; backend nào hỗ trợ; khi nào cần `force-unlock`. *Tài liệu: State Storage and Locking; State Locking.*
- **6c Configure remote state using the backend block** — Cấu hình remote state bằng khối `backend` (ví dụ S3, HCP Terraform...), di chuyển state khi đổi backend. *Tài liệu: State Storage and Locking; Backend Block Configuration.*
- **6d Manage resource drift and Terraform state** — Xử lý drift (hạ tầng thật bị sửa lệch so với code): chế độ refresh-only (`-refresh-only`), refactor state bằng khối `moved` và `removed`. *Tài liệu: Terraform State; Refactor Terraform State; Refresh-Only Mode; Removed Block Reference; Moved Block Reference; Manage Resource Drift; Use Refresh-Only Mode.*

### Domain 7 — Maintain infrastructure with Terraform (Vận hành hạ tầng bằng Terraform)
- **7a Import existing infrastructure into your Terraform workspace** — Đưa hạ tầng đang có (tạo tay trước đó) vào quản lý của Terraform: lệnh `terraform import` và cách import theo config. *Tài liệu: Command: import; Import Existing Resources; Import Terraform Configuration.*
- **7b Use the CLI to inspect state** — Dùng CLI xem state: `terraform state list`, `terraform state show`, `terraform show`... *Tài liệu: State Command; Manage Resources in State.*
- **7c Describe when and how to use verbose logging** — Bật log chi tiết để debug: biến môi trường `TF_LOG` (mức `TRACE`, `DEBUG`...) và `TF_LOG_PATH`. *Tài liệu: Debugging Terraform; Enable Terraform Logging.*

### Domain 8 — HCP Terraform (Nền tảng HCP Terraform, tên cũ: Terraform Cloud)
- **8a Use HCP Terraform to create infrastructure** — Dùng HCP Terraform để tạo hạ tầng: workspace, remote operations (plan/apply chạy trên HCP Terraform thay vì máy cá nhân), các workflow CLI/VCS. *Tài liệu: Workspaces; HCP Terraform Workflow; HCP Terraform Overview; Remote Operations; HCP Terraform Get Started Collection.*
- **8b Describe HCP Terraform collaboration and governance features** — Mô tả tính năng cộng tác và quản trị: teams, private registry, policy enforcement (Sentinel/OPA), dynamic credentials, drift detection & health, variable sets, explorer, change requests, projects. *Tài liệu: Explorer; HCP Private Registry Overview; Change Requests Overview; HCP Terraform Policy Enforcement; Projects Overview; Health; HCP Terraform Teams; Authenticate Providers with Dynamic Credentials; Drift Detection; Variable Sets; Detect Drift and Enforce Policies; Enforce OPA Policies.*
- **8c Describe how to organize and use HCP Terraform workspaces and projects** *(mới ở 004)* — Tổ chức workspace theo project, dùng variable sets dùng chung, nối workspace bằng run triggers. *Tài liệu: Run Triggers; Variable Sets; Projects Overview; Connect Workspaces with Run Triggers; Organize Workspaces with Projects.*
- **8d Configure and use HCP Terraform integration** — Kết nối CLI với HCP Terraform: `terraform login`, khối `cloud`, migrate state lên HCP Terraform, nâng phiên bản Terraform trong workspace. *Tài liệu: Use CLI with HCP Terraform; Connect to HCP Terraform; Migrate Terraform State to HCP Terraform; Remote Operations; Command: login; Migrate State to HCP Terraform; Upgrade Terraform Version in HCP Terraform; Collaborate Using HCP Terraform.*

> Ghi chú: phần giải thích tiếng Việt và ví dụ lệnh trong ngoặc là diễn giải của mentor để định hướng ôn tập; danh sách objective và tên tài liệu lấy từ trang chính hãng. Khi soạn bài học cho từng objective, phải WebFetch tài liệu gốc tương ứng để xác minh chi tiết (cú pháp, hành vi theo Terraform 1.12).

## Phong cách câu hỏi

- **Dạng câu** (theo trang Sample Questions chính hãng): True/False; Multiple choice (chọn 1); Multiple answer (chọn nhiều — đề ghi rõ số đáp án cần chọn).
- **Độ dài**: đề Associate thiên về kiến thức khái niệm và hành vi của lệnh/khối cấu hình, câu tương đối ngắn so với đề AWS (nhận xét của mentor dựa trên câu mẫu, không phải tuyên bố chính hãng).
- **Trung lập provider**: không cần kiến thức riêng AWS/Azure/GCP; tập trung vào Terraform core và HCP Terraform.
- **Theo phiên bản Terraform 1.12**: hành vi lệnh và tính năng tính theo bản 1.12 — tránh học theo tài liệu quá cũ.
- **Mẹo cho người đọc tiếng Anh còn hạn chế**: thời gian 60 phút khá sát; nên luyện đọc nhanh các từ khoá hay gặp như *NOT*, *EXCEPT*, *Select two*, *Which of the following*, *best describes*.

## Tài liệu ôn chính hãng

- [Trang chứng chỉ Terraform Associate (004)](https://developer.hashicorp.com/certifications/terraform-associate) — thông tin kỳ thi, đăng ký, gia hạn.
- [Associate Prep (004) — collection](https://developer.hashicorp.com/terraform/tutorials/certification-004) — gồm 3 trang dưới:
  - [Learning Path - Terraform Associate 004](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-study-004) — lộ trình ôn từ đầu đến cuối theo 8 objective.
  - [Exam Content List - Terraform Associate 004](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004) — objective + tài liệu cho từng objective (dùng để ôn có chọn lọc).
  - [Sample Questions - Terraform Associate 004](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-questions-004) — câu hỏi mẫu chính hãng (để làm quen format).
- Tất cả tutorial trên developer.hashicorp.com miễn phí. Có thể luyện hoàn toàn local (Terraform CLI + provider `local`, `random`, Docker provider, hoặc LocalStack) để tránh chi phí cloud. Với Domain 8, cần tài khoản HCP Terraform — **điều kiện gói miễn phí hiện tại chưa xác minh**, kiểm tra trước khi tạo tài khoản.
- Trung tâm trợ giúp chứng chỉ HashiCorp (quy định thi, thi lại, accommodation): https://hashicorp-certifications.zendesk.com — trang chặn truy cập tự động, người học cần tự mở bằng trình duyệt.

> **Cảnh báo**: Không dùng "exam dump"/"real exam questions" — vi phạm thoả thuận thi của HashiCorp và có thể bị thu hồi chứng chỉ. Câu hỏi luyện tập trong repo này đều là câu tự soạn theo objective chính thức.

---

### Nguồn đã kiểm tra (2026-11-05)
| Nguồn | Trạng thái |
|---|---|
| https://developer.hashicorp.com/certifications/infrastructure-automation | Đã đọc |
| https://developer.hashicorp.com/certifications | Đã đọc |
| https://developer.hashicorp.com/certifications/terraform-associate | Đã đọc |
| https://developer.hashicorp.com/terraform/tutorials/certification-004 | Đã đọc |
| https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004 | Đã đọc |
| https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-study-004 | Đã đọc |
| https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-questions-004 | Đã đọc |
| https://developer.hashicorp.com/terraform/tutorials/certification-003 | Đã đọc — hiển thị nội dung 004 |
| hashicorp-certifications.zendesk.com (rules, retake, accommodation, passing score) | HTTP 403 — chỉ có snippet kết quả tìm kiếm |

### Mục chưa xác minh
- Số câu hỏi chính thức (không công bố; bên thứ ba ghi ~57).
- Điểm đạt (HashiCorp không công bố).
- Ngày phát hành 004 / ngày ngừng 003.
- Có cộng giờ cho người không nói tiếng Anh bản xứ hay không.
- Chi tiết quy định giấy tờ / hệ thống / phòng thi; chi tiết chính sách thi lại (chỉ có snippet).
- Điều kiện gói miễn phí HCP Terraform.
