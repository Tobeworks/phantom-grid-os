#!/bin/bash
# phantom-grid-vhs.sh
# Apply Phantom Grid terminal glow effects to a video file.
#
# Usage:
#   ./phantom-grid-vhs.sh input.mp4 [output.mp4]
#
# Effects applied:
#   - Scanlines (drawgrid, 4px rhythm)
#   - Film grain / noise
#   - Vignette (dark edges, luminous center)
#   - Color grade (red bias, slight desaturation)

set -e

INPUT="$1"
OUTPUT="${2:-${INPUT%.*}_pg.mp4}"

if [ -z "$INPUT" ]; then
  echo "Usage: $0 input.mp4 [output.mp4]"
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "Error: file not found: $INPUT"
  exit 1
fi

echo "→ Input:  $INPUT"
echo "→ Output: $OUTPUT"
echo "→ Applying Phantom Grid effects..."

ffmpeg -i "$INPUT" \
  -vf "drawgrid=x=0:y=0:width=0:height=4:color=black@0.2:thickness=2,\
noise=alls=14:allf=t+u,\
vignette=PI/4.5,\
colorchannelmixer=rr=1.05:gg=0.97:bb=0.95" \
  -c:v libx264 -crf 18 -preset slow \
  -c:a copy \
  "$OUTPUT" -y

echo "✓ Done: $OUTPUT"
