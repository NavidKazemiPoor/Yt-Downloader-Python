from downloader import YouTubeDownloader


def select_and_download(url: str):
    downloader = YouTubeDownloader()

    info = downloader.get_info(url)
    if not info:
        return

    valid_formats = downloader.get_valid_formats(info)
    if not valid_formats:
        print("No suitable formats found.")
        return

    downloader.print_formats(valid_formats)

    selected_id = input("\nEnter format ID:\t").strip()
    selected = next(
        (f for f in valid_formats if str(f["format_id"]) == selected_id),
        None,
    )

    if not selected:
        print("Invalid format selected.")
        return

    downloader.print_summary(info, selected)

    confirm = input("\nDo you want to download this? (Y/N):\t").strip().lower()
    if confirm == "y":
        downloader.download(url, selected_id)
    else:
        print("Download cancelled.")


def run():
    print("--- YouTube Downloader (yt-dlp) ---")
    while True:
        url = input("\nEnter Video URL (or q to quit):\t").strip()
        if url.lower() == "q":
            break
        if not url:
            continue
        select_and_download(url)