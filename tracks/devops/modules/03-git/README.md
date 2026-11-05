# Module 03 — Git & quy trình làm việc nhóm

- **Tầng**: Nền tảng · **Cấp độ đích**: L3
- **Giờ ước tính**: 12 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: Không
- **Liên quan chứng chỉ**: Không
- **Tài liệu chính hãng gốc**: https://git-scm.com/doc · https://docs.gitlab.com/user/project/merge_requests/
- **Vì sao cần**: Chỉ 25.5% tin ghi rõ vì nhà tuyển dụng mặc định bạn biết; mọi CI/CD, IaC, GitOps đều dựa trên Git.

## Sau module này bạn sẽ làm được
1. Hiểu Git lưu dữ liệu thế nào (commit, tree, blob, ref)
2. Làm việc theo merge request, giải quyết conflict, rebase sạch
3. Cứu dữ liệu bằng reflog/revert; xử lý khi lỡ commit secret

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | Git hoạt động bên trong | Snapshot, object, HEAD, ref — vì sao Git nhanh | 1.5 | chưa viết |
| 02 | Branch, merge, rebase & conflict | Chọn merge hay rebase; giải conflict | 1.5 | chưa viết |
| 03 | Quy trình nhóm & merge request | Trunk-based vs GitFlow, review, branch protection | 1 | chưa viết |
| 04 | Hoàn tác & cứu dữ liệu | reset/revert/reflog/stash/cherry-pick | 1.5 | chưa viết |
| 05 | Tag, versioning, hooks & bảo vệ secret | SemVer, .gitignore, pre-commit, gitleaks | 1.5 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-team-workflow | Repo TaskFlow trên GitLab: branch protection, MR, tag release | lab | ✅ | L2 |
| ex02-git-rescue | Cứu repo: commit bị mất, lịch sử rối, secret bị lộ | debug | ✅ | L3 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 03`)
- [ ] Repo TaskFlow có ≥ 5 MR đã merge, tag `v0.1.0`, không secret trong lịch sử (gitleaks pass)
