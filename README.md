# YouTube Downloader (yt-dlp)

A clean, modular command-line YouTube downloader built with [yt-dlp](https://github.com/yt-dlp/yt-dlp).

Supports format selection, progress tracking, and smart error handling (especially useful in restricted networks like Iran).

---

## Features

- List available video formats with resolution, FPS, size, and codec
- Interactive format selection
- Progress bar with download speed and ETA
- Automatic merging to MP4
- Network / filter error detection with helpful messages
- Clean modular architecture (easy to extend)

---

## Project Structure

youtube_downloader/
├── init.py
├── errors.py # Network & filter error detection + messages
├── downloader.py # Core YouTubeDownloader class
├── cli.py # Command-line interface
└── main.py # Entry point

---

## Requirements

- Python 3.9+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

Install dependencies:

```bash
pip install yt-dlp
```

# Installation

## Option 1: Clone the repositoryBash

git clone https://github.com/YOUR_USERNAME/youtube-downloader.git
cd youtube-downloader

# Option 2: Run directly

## Just place the files in a folder and run:

python main.py

--- YouTube Downloader (yt-dlp) ---

Enter Video URL (or q to quit): https://www.youtube.com/watch?v=dQw4w9WgXcQ

--- Available Formats ---

## ID Resolution FPS Ext Size Type

137 1080p 30 mp4 45.2 MB 1080p
136 720p 30 mp4 22.1 MB 720p
135 480p 30 mp4 12.4 MB 480p
...

Enter format ID: 137

--- Summary ---
Title : Frank Garcia - Never Gonna Give You Up
Duration : 3.55 min
Resolution : 1080p
FPS : 30
Format : mp4
Views : 1500000000

Do you want to download this? (Y/N): y

Downloading... 45.2% | Speed: 3.2MiB/s | ETA: 00:12
...
Download completed successfully!
