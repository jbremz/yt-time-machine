#!/usr/bin/env python3
"""Parse YouTube watch-history.html from Google Takeout into JSON."""

import re
import json
import sys
from pathlib import Path

def parse_history(html_path: str) -> list[dict]:
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Each entry is an outer-cell div
    raw_entries = re.split(r'<div class="outer-cell[^"]*">', content)[1:]

    entries = []
    for raw in raw_entries:
        # Extract video URL and title
        video_match = re.search(
            r'Watched\s+<a href="https://www\.youtube\.com/watch\?v=([^"&]+)"[^>]*>([^<]+)</a>',
            raw,
        )
        if not video_match:
            continue  # skip removed/missing videos and ads

        video_id = video_match.group(1)
        title = video_match.group(2)

        # Extract channel name and URL
        channel_match = re.search(
            r'<a href="https://www\.youtube\.com/channel/([^"]+)"[^>]*>([^<]+)</a>',
            raw,
        )
        channel = channel_match.group(2) if channel_match else None
        channel_id = channel_match.group(1) if channel_match else None

        # Extract date — format: "21 Feb 2026, 10:18:44 GMT"
        date_match = re.search(
            r'(\d{1,2}\s\w{3}\s\d{4},\s[\d:]+\s\w+)', raw
        )
        if not date_match:
            continue

        date_str = date_match.group(1)

        entries.append({
            "id": video_id,
            "title": title,
            "channel": channel,
            "channelId": channel_id,
            "date": date_str,
        })

    return entries


def main():
    src = Path(__file__).parent / "watch-history.html"
    if not src.exists():
        print(f"Error: {src} not found.")
        print("Copy your watch-history.html into this directory first.")
        print("See README.md for instructions.")
        sys.exit(1)

    print(f"Parsing {src}...")
    entries = parse_history(str(src))
    print(f"Found {len(entries)} video entries.")

    out = Path(__file__).parent / "data.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False)

    print(f"Wrote {out} ({out.stat().st_size / 1024 / 1024:.1f} MB)")


if __name__ == "__main__":
    main()
