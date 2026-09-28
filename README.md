# YouTube Playlist Extractor

A simple Python script that extracts all videos from any YouTube playlist into an Excel file (SN, Title, Link). Just paste the playlist URL — the script saves `playlist.xlsx` in the folder where you run it and opens it automatically.

---

## Features

- 🎬 Paste any YouTube playlist URL at runtime — no code editing needed
- 📊 Saves data as `playlist.xlsx` (SN, Topic, Link)
- 📁 Output saved in the folder where you run the script
- 🚀 Auto-opens the Excel file after completion
- ✅ Cross-platform (Windows, macOS, Linux)
- 🛡️ Handles invalid URLs, private playlists, and empty playlists gracefully

---

## Requirements

- **Python 3.7+** ([Download](https://www.python.org/downloads/))
  - ⚠️ Windows: check ✅ **"Add Python to PATH"** during installation
- **yt-dlp** — YouTube extractor
- **pandas** + **openpyxl** — Excel writer

---

## Installation

### 1. Install Python

- **Windows/macOS:** Download from [python.org](https://www.python.org/downloads/)
- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

Verify:
```bash
python --version
```

### 2. Install yt-dlp

```bash
pip install yt-dlp
```

> Update later with: `pip install --upgrade yt-dlp`

### 3. Install remaining libraries

```bash
pip install pandas openpyxl
```

### One-liner (install everything at once):

```bash
pip install yt-dlp pandas openpyxl
```

| Library | Purpose |
|---------|---------|
| `yt-dlp` | Extract YouTube playlist info |
| `pandas` | Organize data into a table |
| `openpyxl` | Write `.xlsx` files |

---

## Usage

1. Open a terminal **in the folder where you want the Excel file saved**.
2. Run the script:
   ```bash
   python playlist_extractor.py
   ```
3. Paste the YouTube playlist URL when prompted.
4. `playlist.xlsx` is created in the current folder and opens automatically.

### Example run

```
==================================================
  YouTube Playlist Extractor
==================================================

Paste the YouTube playlist URL:
> https://youtube.com/playlist?list=PLLrSPLH16tJ3Eg_hZD1BcqsHXmtZE1YeG

⏳ Fetching playlist info...

✅ Done! Saved 42 videos to:
C:\Users\You\Desktop\playlist.xlsx
```

---

## Output Format

| SN | Topic of the Video | Link |
|----|--------------------|------|
| 1  | Introduction       | https://www.youtube.com/watch?v=xxxxx |
| 2  | Getting Started    | https://www.youtube.com/watch?v=yyyyy |
| 3  | Advanced Topics    | https://www.youtube.com/watch?v=zzzzz |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `pip not recognized` | Reinstall Python and enable **"Add to PATH"** |
| `yt-dlp not found` | Run `python -m pip install yt-dlp` |
| `Unable to extract playlist` | Update yt-dlp: `pip install --upgrade yt-dlp` |
| Private playlist error | Make sure the playlist is **public** |
| Permission denied (Linux/macOS) | `chmod +x playlist_extractor.py` |
| Excel doesn't open automatically | Manually open `playlist.xlsx` from the folder |

---

## Optional: Build a Standalone `.exe` (no Python needed to run)

```bash
pip install pyinstaller
pyinstaller --onefile playlist_extractor.py
```

The `.exe` will be in the `dist/` folder — double-click to run.

---

## License

Free to use and modify for personal projects.
