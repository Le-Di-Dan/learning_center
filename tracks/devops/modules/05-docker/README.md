# Module 05 — Docker & container

- **Tầng**: Quan trọng → nâng L4 · **Cấp độ đích**: L4
- **Giờ ước tính**: 30 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 01-linux, 02-networking
- **Liên quan chứng chỉ**: cka (nền tảng container)
- **Tài liệu chính hãng gốc**: https://docs.docker.com/ · https://github.com/opencontainers/image-spec
- **Vì sao cần**: Container 56.9% tin J/M; tiền đề bắt buộc của Kubernetes và CI/CD hiện đại.

## Sau module này bạn sẽ làm được
1. Giải thích container vs VM (namespace, cgroup)
2. Viết Dockerfile multi-stage, image nhỏ, chạy non-root, build multi-arch
3. Dựng môi trường nhiều service bằng Docker Compose
4. Debug container và scan lỗ hổng image

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | Container là gì? | So với VM; namespace, cgroup, OCI | 1.5 | chưa viết |
| 02 | Image, container & registry | Vòng đời container, lệnh cơ bản, Docker Hub | 1.5 | chưa viết |
| 03 | Viết Dockerfile | Layer, cache, .dockerignore, CMD vs ENTRYPOINT | 1.5 | chưa viết |
| 04 | Multi-stage build cho Vue + Node | Image nhỏ, non-root, reproducible | 2 | chưa viết |
| 05 | Volume & dữ liệu bền vững | bind mount vs volume, backup | 1 | chưa viết |
| 06 | Docker networking | bridge, host, DNS giữa container, publish port | 1.5 | chưa viết |
| 07 | Docker Compose | Môi trường multi-service: web, api, postgres, redis | 2 | chưa viết |
| 08 | Bảo mật image | Base image, Trivy scan, secrets khi build | 1.5 | chưa viết |
| 09 | Debug container | logs, exec, inspect, healthcheck, resource limit | 1.5 | chưa viết |
| 10 | Hệ sinh thái runtime & multi-arch | containerd, Podman, buildx arm64/amd64 (Mac M-series) | 1 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-dockerize-taskflow | Dockerize TaskFlow (multi-stage, non-root) | lab | ✅ | L2 |
| ex02-compose-stack | Compose full stack có healthcheck, volume, network riêng | lab | ✅ | L3 |
| ex03-broken-containers | Sửa container lỗi (crash, mạng, quyền volume) | debug | ✅ | L3 |
| ex04-harden-image | Tối ưu & hardening image, Trivy không còn CRITICAL | project | ✅ | L4 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 05`)
- [ ] Image API < 200MB, chạy non-root, build được cả linux/amd64 và linux/arm64
- [ ] `docker compose up` từ repo sạch → app chạy trong ≤ 2 phút
