# Thuật ngữ DevOps Anh–Việt

> Thêm dần khi học. Cột "Gặp ở bài" ghi mã bài `MM-LL` (hoặc "onboarding").

| Tiếng Anh | Tiếng Việt | Giải thích | Gặp ở bài |
|---|---|---|---|
| DevOps | Phát triển + Vận hành | Văn hoá & tập hợp thực hành giúp đưa phần mềm từ code tới production nhanh, an toàn, tự động | onboarding |
| CI/CD (Continuous Integration / Continuous Delivery–Deployment) | Tích hợp liên tục / Phân phối–Triển khai liên tục | Tự động build, test mỗi lần commit; tự động đưa bản mới lên môi trường chạy thật | onboarding |
| Pipeline | Đường ống (quy trình tự động) | Chuỗi bước tự động: lint → test → build → deploy | onboarding |
| Container | Container (gói chạy ứng dụng) | Gói ứng dụng + thư viện cần thiết, chạy cô lập, giống nhau trên mọi máy | onboarding |
| Orchestration | Điều phối | Tự động chạy, phân bổ, scale, phục hồi nhiều container trên nhiều máy (vd Kubernetes) | onboarding |
| IaC (Infrastructure as Code) | Hạ tầng dưới dạng code | Mô tả server, mạng, database bằng file code, lưu trong Git, chạy lặp lại được (vd Terraform) | onboarding |
| Configuration management | Quản lý cấu hình | Tự động cài đặt & cấu hình phần mềm trên nhiều server (vd Ansible) | onboarding |
| Observability | Khả năng quan sát | Hiểu được hệ thống đang làm gì từ metric, log, trace | onboarding |
| Monitoring | Giám sát | Thu thập số liệu và cảnh báo khi có bất thường | onboarding |
| GitOps | GitOps | Git là "nguồn sự thật": muốn đổi hệ thống thì đổi Git, công cụ (Argo CD) tự đồng bộ | onboarding |
| SRE (Site Reliability Engineering) | Kỹ thuật độ tin cậy hệ thống | Cách Google vận hành hệ thống bằng tư duy kỹ sư phần mềm: SLO, error budget, tự động hoá | onboarding |
| SLI / SLO | Chỉ số / Mục tiêu mức dịch vụ | SLI: con số đo chất lượng (vd % request thành công). SLO: mục tiêu cho SLI (vd 99.9%) | onboarding |
| Production | Môi trường thật | Nơi người dùng thật đang sử dụng | onboarding |
| Free tier | Gói miễn phí | Mức sử dụng cloud miễn phí có giới hạn | onboarding |
| Budget alert | Cảnh báo ngân sách | Cảnh báo khi chi phí cloud vượt ngưỡng — đặt TRƯỚC khi tạo tài nguyên | onboarding |
