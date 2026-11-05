# Module 14 — Monitoring, logging & observability

- **Tầng**: Cốt lõi · **Cấp độ đích**: L4
- **Giờ ước tính**: 40 (chưa gồm ôn tập) · **Điều kiện tiên quyết**: 11-kubernetes-core
- **Liên quan chứng chỉ**: Không
- **Tài liệu chính hãng gốc**: https://prometheus.io/docs/ · https://grafana.com/docs/ · https://opentelemetry.io/docs/ · https://www.elastic.co/docs
- **Vì sao cần**: Monitoring/Observability 64.7% tin J/M (Prometheus 39.2%, Grafana 33.3%); Logging 37.3% (ELK 19.6%).

## Sau module này bạn sẽ làm được
1. Thu thập metric bằng Prometheus, viết PromQL, dựng dashboard Grafana
2. Thiết kế alert có ý nghĩa (không spam)
3. Dựng logging tập trung, tracing cơ bản với OpenTelemetry
4. Đi từ alert tới root cause bằng metric + log + trace

## Danh sách bài học
| # | Bài | Mục tiêu (1 dòng) | Giờ | Trạng thái file |
|---|---|---|---|---|
| 01 | Observability là gì? | Metric, log, trace; golden signals, RED, USE | 1.5 | chưa viết |
| 02 | Prometheus | Kiến trúc pull, scrape, exporter | 1.5 | chưa viết |
| 03 | PromQL | Selector, rate, aggregation, histogram | 2 | chưa viết |
| 04 | Instrument ứng dụng Node.js | Metric tuỳ chỉnh bằng prom-client | 1.5 | chưa viết |
| 05 | Grafana dashboard | Panel, variable, dashboard as code | 1.5 | chưa viết |
| 06 | Alerting tử tế | Alertmanager, rule, routing, tránh alert fatigue | 1.5 | chưa viết |
| 07 | kube-prometheus-stack | Giám sát Kubernetes bằng Helm chart chuẩn | 1.5 | chưa viết |
| 08 | Logging tập trung | EFK/ELK, structured logging; so sánh Loki | 2 | chưa viết |
| 09 | Tracing với OpenTelemetry | Span, trace, collector (cơ bản) | 1.5 | chưa viết |
| 10 | Từ alert tới root cause | Quy trình điều tra sự cố bằng dữ liệu | 1.5 | chưa viết |

## Bài tập
| Mã | Tên | Loại (lab/debug/tư duy/project) | Bắt buộc | Cấp độ chứng minh |
|---|---|---|---|---|
| ex01-metrics-dashboard | Prometheus + Grafana cho TaskFlow, 4 golden signals | lab | ✅ | L2 |
| ex02-alerting | Alert rule + Alertmanager gửi thông báo | lab | ✅ | L3 |
| ex03-logging-stack | Logging tập trung cho TaskFlow | lab | ✅ | L3 |
| ex04-incident-investigation | Điều tra sự cố bằng metric/log/trace, viết báo cáo | tư duy | ✅ | L4 |

> Đề bài, rubric và `check.sh` được tạo khi giao bài (`/bai-tap`). Bài tập dùng **TaskFlow** — dự án xuyên suốt (xem `roadmap.md`).

## Definition of Done
- [ ] Tất cả bài tập bắt buộc đạt ≥ 80/100 + vấn đáp
- [ ] Quiz module ≥ 80% (`/on-tap module 14`)
- [ ] Dashboard có 4 golden signals; alert bắn trong ≤ 2 phút khi lỗi 5xx > 5%
- [ ] Mọi log của TaskFlow là JSON, tìm được theo request-id
