# YouTube Downloader

This Python script enables you to download YouTube videos by selecting a specific resolution and format. It utilizes the `yt-dlp` library to interact with YouTube and download videos.

## Installation

1. Ensure you have Python installed on your system.
2. Install the `yt-dlp` library using pip:

   ```bash
   pip install -U yt-dlp
   ```

## Usage

1. Run the script by executing `yt_downloader.py`.
2. Enter the URL of the YouTube video you want to download.
3. Select the desired video resolution and format from the available options.
4. Review the video information and confirm your selection to start the download.

## Features

- Select specific video resolution and format.
- Monitor download progress, speed, and estimated time remaining.
- Get summary information about the video before downloading.
- Display video title, duration, FPS, format, and view count.
- Handle common network and connection errors.
- Support MP4 output merging (requires FFmpeg).
