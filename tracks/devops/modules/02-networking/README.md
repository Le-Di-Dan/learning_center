# Module 02 — Networking cho DevOps

- **Tầng**: Quan trọng → nâng L4 · **Cấp độ đích**: L4
- **Giờ ước tính**: 30 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 01-linux
- **Liên quan chứng chỉ**: aws-saa (VPC), cka (Services & Networking)
- **Tài liệu chính hãng gốc**: https://developer.mozilla.org/en-US/docs/Web/HTTP · https://nginx.org/en/docs/ · RFC 1918, RFC 9110
- **Vì sao cần**: 51% tin J/M, 61.1% mọi level; nền của VPC, Kubernetes networking và gần như mọi bài debug khi phỏng vấn.

## Sau module này bạn sẽ làm được
1. Giải thích đường đi của một HTTP request từ trình duyệt tới server (DNS, TCP, TLS, HTTP)
2. Tính subnet/CIDR, thiết kế dải IP cho môi trường nhiều tầng
3. Cấu hình Nginx làm reverse proxy + load balancer + TLS
4. Debug sự cố mạng bằng dig, curl -v, ss, traceroute, tcpdump

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | Một request đi đâu? Mô hình TCP/IP | Các tầng mạng qua ví dụ DevTools Network tab bạn đã quen | 1.5 | chưa viết |
| 02 | IP, subnet & CIDR | Tính dải IP, private/public IP, NAT; bài tập chia subnet | 2 | chưa viết |
| 03 | TCP, UDP & port | 3-way handshake, port, socket, ss/nc | 1.5 | chưa viết |
| 04 | DNS chuyên sâu | Record A/AAAA/CNAME/MX/TXT, TTL, resolver, dig | 1.5 | chưa viết |
| 05 | HTTP & TLS | Method, status, header, certificate chain, openssl, curl -v | 2 | chưa viết |
| 06 | Routing, NAT & firewall | Route table, iptables/nftables, ufw | 2 | chưa viết |
| 07 | Reverse proxy & load balancer với Nginx | upstream, health check, L4 vs L7 | 2 | chưa viết |
| 08 | Troubleshooting mạng | Quy trình debug từng tầng, tcpdump cơ bản | 2 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-subnet-and-proxy | Thiết kế subnet + Nginx reverse proxy có TLS cho TaskFlow | lab | ✅ | L2 |
| ex02-network-debug | Sửa lỗi: DNS sai, port đóng, firewall chặn | debug | ✅ | L3 |
| ex03-timeout-investigation | Tình huống: website timeout ngắt quãng — phân tích & báo cáo | tư duy | ✅ | L4 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 02`)
- [ ] Chia đúng 10/10 bài subnet trong quiz
- [ ] ex02: tìm và sửa đủ 3 lỗi, giải thích được bằng chứng của từng lỗi
