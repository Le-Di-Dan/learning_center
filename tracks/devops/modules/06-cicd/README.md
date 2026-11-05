# Module 06 — CI/CD: GitLab CI, Jenkins, GitHub Actions

- **Tầng**: Cốt lõi · **Cấp độ đích**: L4
- **Giờ ước tính**: 40 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 03-git, 04-scripting, 05-docker
- **Liên quan chứng chỉ**: Không
- **Tài liệu chính hãng gốc**: https://docs.gitlab.com/ci/ · https://www.jenkins.io/doc/book/pipeline/ · https://docs.github.com/en/actions
- **Vì sao cần**: Nhóm CI/CD có tỷ lệ cao nhất: 84.3% tin J/M. GitLab CI 35.3%, Jenkins 33.3%, GitHub Actions 27.5%.

## Sau module này bạn sẽ làm được
1. Thiết kế pipeline lint → test → build → scan → deploy cho app thật
2. Quản lý secret, environment, runner; deploy có rollback
3. Chuyển pipeline giữa GitLab CI, Jenkins, GitHub Actions
4. Giải thích chiến lược deploy (rolling, blue-green, canary) và DORA metrics

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | CI/CD là gì? | CI, Continuous Delivery vs Deployment, DORA metrics | 1 | chưa viết |
| 02 | GitLab CI cơ bản | .gitlab-ci.yml, stage, job, runner | 1.5 | chưa viết |
| 03 | Pipeline cho TaskFlow | lint, test, build, artifact, cache | 2 | chưa viết |
| 04 | Build & push image trong CI | Registry, tag theo commit/SemVer | 1.5 | chưa viết |
| 05 | Variable, secret & environment | Protected/masked variable, environment, approval | 1.5 | chưa viết |
| 06 | Runner tự host | Docker executor, bảo mật runner | 1.5 | chưa viết |
| 07 | Chiến lược deploy & rollback | Rolling, blue-green, canary, feature flag | 1.5 | chưa viết |
| 08 | Pipeline nâng cao | rules, needs/DAG, include/template, parallel matrix | 1.5 | chưa viết |
| 09 | Jenkins pipeline | Jenkinsfile declarative — chuyển đổi từ GitLab CI | 2 | chưa viết |
| 10 | GitHub Actions | Workflow, reusable workflow, OIDC — so sánh & chuyển đổi | 1.5 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-ci-pipeline | Pipeline CI cho TaskFlow (lint/test/build/push image) | lab | ✅ | L2 |
| ex02-cd-with-rollback | CD tự động lên server, có rollback 1 lệnh | lab | ✅ | L3 |
| ex03-broken-pipeline | Sửa pipeline lỗi (cache, rule, secret, runner) | debug | ✅ | L3 |
| ex04-port-pipeline | Chuyển pipeline sang GitHub Actions và Jenkins (không hướng dẫn) | lab | ✅ | L3 |
| ex05-pipeline-design | Thiết kế pipeline cho monorepo + review bảo mật pipeline | tư duy | ✅ | L4 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 06`)
- [ ] Pipeline TaskFlow xanh, tổng thời gian < 10 phút, merge vào main tự deploy
- [ ] Rollback về bản trước trong < 5 phút (đo được)
