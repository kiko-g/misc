#!/bin/bash
for f in *.webm; do
    ffmpeg -i "$f" -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k "mp4/${f%.*}.mp4"
done
