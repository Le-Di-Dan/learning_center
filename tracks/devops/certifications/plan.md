# Kế hoạch chứng chỉ — DevOps

> Dựa trên: `research/skills-matrix.md` (ngày 2026-11-05). Thông tin đề thi kiểm tra trên trang chính hãng ngày 2026-11-05 — **kiểm tra lại trước khi đăng ký** (AWS đang thay phiên bản nhiều đề; Kubernetes v1.38 dự kiến ra 12/2026 nên đề CKA có thể đổi phiên bản đầu 2027).

## Chứng chỉ mục tiêu (theo thứ tự thi)
| # | Chứng chỉ (mã đề) | Đơn vị cấp | % tin nhắc tới (J/M) | Lý do chọn | Phí thi | Sau module | Dự kiến thi |
|---|---|---|---|---|---|---|---|
| 1 | AWS Certified Solutions Architect – Associate (SAA-C03) | Amazon Web Services | 19.6% tin nhắc chứng chỉ có tên AWS (vượt ngưỡng 15%) | AWS là cloud số 1 trong dữ liệu (68.6%); SA Associate là chứng chỉ AWS được gọi tên nhiều nhất trong các tin (CoderPush, GoTymeX, VPS, i3 Verticals, Greychain); HR nhận diện tốt nhất; kiến thức thiết kế dùng trực tiếp ở vòng system design | 150 USD | 08-aws-advanced | tuần 26 (~05/2027) |
| 2 | Certified Kubernetes Administrator (CKA) | The Linux Foundation / CNCF | 5.9% (CKA/CKAD/CKS gộp) | Không đạt ngưỡng 15% nhưng là **chuẩn de-facto** của Kubernetes — kỹ năng Cốt lõi (66.7%). Thi thực hành trên terminal → chứng minh năng lực thật, rất có giá trị ở vòng hands-on | 445 USD (gồm 1 lần thi lại + 2 lượt killer.sh) | 12-kubernetes-admin | tuần 38 (~07–08/2027) |
| 3 | HashiCorp Terraform Associate (004) — **tuỳ chọn** | HashiCorp | 0% | Không có tin nào nhắc, nhưng rẻ (70.50 USD), học xong module 09 là gần đủ kiến thức. Chỉ thi nếu đang nhanh hơn kế hoạch | 70.50 USD | 09-terraform | linh hoạt |

## Đã cân nhắc nhưng không chọn
| Chứng chỉ | % tin | Lý do không chọn (lúc này) |
|---|---|---|
| AWS Certified CloudOps Engineer – Associate (SOA-C03, tên cũ SysOps Administrator) | ~4% gọi tên SysOps | Nội dung rất sát DevOps (monitoring, deployment, Terraform/CDK, EventBridge) nhưng ít được nhà tuyển dụng gọi tên hơn SAA. Hai đề trùng ~50% kiến thức → **lựa chọn hàng đầu cho chứng chỉ thứ 4** sau khi đi làm |
| AWS Certified DevOps Engineer – Professional | ~4% | Cấp Professional, cần kinh nghiệm thực tế; để sau 1–2 năm làm DevOps |
| CKAD / CKS | 4.2% mỗi loại | CKAD thiên về developer; CKS yêu cầu có CKA còn hạn → cân nhắc sau CKA |
| Azure AZ-104 / AZ-400 | ≤ 4.2% | Đã chọn AWS làm cloud chính; Azure chỉ học ở mức so sánh |
| Red Hat EX280, Security+, Linux certification | 1.4% mỗi loại | Quá ít tin nhắc tới |

## Ghi chú
- Tổng chi phí dự kiến: 150 + 445 = **595 USD** (+ 70.50 USD nếu thi Terraform). Có thể mua thêm AWS Official Practice Exam (subscription Skill Builder từ 29 USD/tháng) trong tháng luyện thi.
- **Hỗ trợ cho người không nói tiếng Anh bản xứ**:
  - AWS: đăng ký **ESL +30** (thêm 30 phút) **một lần** tại aws.training → Certification → Request Exam Accommodations, **trước khi** đặt lịch thi. Đề không có tiếng Việt → thi bằng tiếng Anh.
  - CKA: không cộng giờ vì ngôn ngữ; được mở kubernetes.io/docs (kể cả bản dịch) trong lúc thi. Đề có tiếng Anh/Trung/Nhật.
  - Terraform: không thấy chính sách ESL riêng; hỏi bộ phận hỗ trợ chứng chỉ nếu cần.
- Không dùng exam dump (vi phạm thoả thuận thi). Mọi câu hỏi luyện tập do mentor tự soạn theo objective chính thức.
