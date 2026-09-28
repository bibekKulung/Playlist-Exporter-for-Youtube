# pip install yt-dlp pandas openpyxl
import yt_dlp
import pandas as pd
import os
import sys

# Ask user for the playlist URL
print("=" * 50)
print("  YouTube Playlist Extractor")
print("=" * 50)
url = input("\nPaste the YouTube playlist URL:\n> ").strip()

# Basic validation
if not url or "youtube.com" not in url and "youtu.be" not in url:
    print("\n❌ Invalid URL. Please provide a valid YouTube playlist link.")
    sys.exit(1)

# Get the folder where the script is run from
script_dir = os.getcwd()

# Extract playlist info
print("\n⏳ Fetching playlist info...")
try:
    ydl = yt_dlp.YoutubeDL({'extract_flat': True, 'quiet': True})
    info = ydl.extract_info(url, download=False)
except Exception as e:
    print(f"\n❌ Failed to extract playlist:\n{e}")
    sys.exit(1)

# Build rows
rows = [
    {
        'SN': i + 1,
        'Topic of the Video': v.get('title', 'Untitled'),
        'Link': f"https://www.youtube.com/watch?v={v['id']}"
    }
    for i, v in enumerate(info.get('entries', []))
]

if not rows:
    print("\n❌ No videos found in this playlist.")
    sys.exit(1)

# Save to where the script is run from
output_path = os.path.join(script_dir, "playlist.xlsx")
pd.DataFrame(rows).to_excel(output_path, index=False)

print(f"\n✅ Done! Saved {len(rows)} videos to:\n{output_path}")

# Open the file automatically (cross-platform)
if os.name == 'nt':           # Windows
    os.startfile(output_path)
elif sys.platform == 'darwin':  # macOS
    os.system(f'open "{output_path}"')
else:                          # Linux
    os.system(f'xdg-open "{output_path}"')
