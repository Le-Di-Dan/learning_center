# Module 01 — Linux & quản trị hệ thống

- **Tầng**: Cốt lõi · **Cấp độ đích**: L4
- **Giờ ước tính**: 40 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: Không
- **Liên quan chứng chỉ**: Không trực tiếp (nền tảng cho CKA, AWS)
- **Tài liệu chính hãng gốc**: https://documentation.ubuntu.com/server/ · https://www.gnu.org/software/coreutils/manual/ · `man` pages
- **Vì sao cần**: Linux có trong 68.6% tin J/M (100% bắt buộc khi được nhắc). Mọi server, container, Kubernetes node đều chạy Linux.

## Sau module này bạn sẽ làm được
1. Thao tác thành thạo trên server Linux chỉ bằng terminal (không GUI)
2. Quản lý user, quyền, process, service (systemd), disk, log
3. Triển khai một ứng dụng Node.js chạy như service sau Nginx
4. Chẩn đoán có phương pháp các sự cố kinh điển: disk đầy, service không lên, CPU cao, sai quyền

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | DevOps là gì & dựng lab Linux trên Mac | Hiểu vai trò DevOps; tạo VM Ubuntu Server (Multipass/OrbStack) để thực hành | 1.5 | chưa viết |
| 02 | Shell & hệ thống file | Điều hướng cây thư mục FHS, đường dẫn tuyệt đối/tương đối, man/--help | 1.5 | chưa viết |
| 03 | Làm việc với file & text | cat/less/head/tail, grep, find, pipe, redirect, stdin/stdout/stderr | 2 | chưa viết |
| 04 | User, group & permission | Quyền rwx, chmod/chown, sudo, umask, nguyên tắc least privilege | 1.5 | chưa viết |
| 05 | Process & signal | ps/top/htop, kill/signal, foreground/background, nice | 1.5 | chưa viết |
| 06 | Package management | apt, repository, cài/gỡ/cập nhật phần mềm an toàn | 1 | chưa viết |
| 07 | systemd & journald | Viết unit file, quản lý service, đọc log bằng journalctl | 2 | chưa viết |
| 08 | Disk, storage & filesystem | df/du, mount, fstab, LVM cơ bản, inode | 1.5 | chưa viết |
| 09 | SSH & làm việc từ xa | SSH key, ~/.ssh/config, scp/rsync, hardening SSH cơ bản | 1.5 | chưa viết |
| 10 | Troubleshooting Linux có phương pháp | Quy trình chẩn đoán: triệu chứng → giả thuyết → kiểm chứng; các lệnh vàng | 2 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-server-setup | Thiết lập server: user, nhóm, quyền thư mục dự án, SSH key | lab | ✅ | L2 |
| ex02-app-as-service | Chạy TaskFlow API bằng systemd sau Nginx, log qua journald | lab | ✅ | L3 |
| ex03-broken-server | Sửa server bị lỗi (service không start, sai quyền, disk đầy) | debug | ✅ | L3 |
| ex04-incident-rca | Tình huống production: xử lý sự cố + viết RCA ngắn | tư duy | ✅ | L4 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 01`)
- [ ] `check.sh` của ex02 pass: service `taskflow-api` enabled, tự khởi động lại khi bị kill, Nginx trả 200
- [ ] Giải quyết ex03 trong ≤ 45 phút không cần gợi ý mức 3
