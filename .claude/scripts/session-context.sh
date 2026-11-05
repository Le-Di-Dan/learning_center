#!/usr/bin/env bash
# Hook SessionStart: in tóm tắt trạng thái học để Claude biết người học đang ở đâu.
ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
PROFILE="$ROOT/learner/profile.md"
TODAY="$(date +%Y-%m-%d)"

echo "[Learning Center] Hôm nay: $TODAY"

if [ ! -f "$PROFILE" ]; then
  echo "[Learning Center] Người học CHƯA onboard. Khi người học nói muốn học / chuyển sang một role, dùng skill bat-dau."
  exit 0
fi

TRACK="$(sed -n 's/^active_track:[[:space:]]*//p' "$PROFILE" | head -n 1 | tr -d '"'"'"' ')"
echo "[Learning Center] Track đang học: ${TRACK:-chưa chọn}"

PROGRESS="$ROOT/tracks/$TRACK/progress.md"
if [ -z "$TRACK" ] || [ ! -f "$PROGRESS" ]; then
  echo "[Learning Center] Chưa có progress.md cho track này → tiếp tục bat-dau / lap-roadmap."
  exit 0
fi

# Phần "## Tóm tắt" của progress.md
awk '/^## Tóm tắt/{f=1; print; next} /^## /{if (f) exit} f' "$PROGRESS"

# Đếm mục ôn tập đến hạn (cột 4 của bảng "## Lịch ôn tập" là ngày ôn tiếp YYYY-MM-DD)
awk -F'|' -v t="$TODAY" '
  /^## Lịch ôn tập/ {f=1; next}
  /^## / {f=0}
  f && NF >= 6 {
    d = $5; gsub(/[[:space:]]/, "", d)
    if (d ~ /^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/ && d <= t) n++
  }
  END { if (n > 0) print "[Learning Center] Có " n " mục đến hạn ôn tập → gợi ý người học chạy /on-tap trước khi học bài mới." }
' "$PROGRESS"
