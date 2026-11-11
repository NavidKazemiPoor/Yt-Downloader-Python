
import yt_dlp
import os


def is_network_or_filter_error(error_msg: str) -> bool:
    error_msg = error_msg.lower()
    keywords = [
        "unable to download webpage",
        "unable to download api page",
        "urlopen error",
        "connection refused",
        "connection reset",
        "forcibly closed",
        "winerror 10054",
        "winerror 10060",
        "winerror 10061",
        "timed out",
        "timeout",
        "network is unreachable",
        "name or service not known",
        "failed to resolve",
        "http error 403",
        "http error 429",
        "ssl",
        "certificate",
        "transporterror",
        "remote host",
        "getaddrinfo failed",
    ]
    return any(keyword in error_msg for keyword in keywords)


def format_selector(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'socket_timeout': 15,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])

            print("\n--- Available Formats ---\n")
            print(f"{'ID':<8} {'Resolution':<12} {'FPS':<6} {'Ext':<6} {'Size':<10} {'Type'}")
            print("-" * 60)

            valid_formats = []

            for f in formats:
                if f.get('vcodec') != 'none' and f.get('height'):
                    filesize = f.get('filesize') or f.get('filesize_approx')
                    size_str = f"{filesize / 1024 / 1024:.1f} MB" if filesize else "N/A"
                    fps = f.get('fps') or '-'

                    print(
                        f"{f['format_id']:<8} "
                        f"{f.get('height', 'N/A')}p{'':<7} "
                        f"{str(fps):<6} "
                        f"{f.get('ext', ''):<6} "
                        f"{size_str:<10} "
                        f"{f.get('format_note', '')}"
                    )

                    valid_formats.append(f)

            if not valid_formats:
                print("No suitable formats found.")
                return

            selected_id = input("\nEnter format ID:\t").strip()

            selected = next(
                (f for f in valid_formats if str(f['format_id']) == selected_id),
                None
            )

            if not selected:
                print("Invalid format selected.")
                return

            print("\n--- Summary ---")
            print(f"Title      : {info.get('title')}")
            print(f"Duration   : {info.get('duration', 0) / 60:.2f} min")
            print(f"Resolution : {selected.get('height')}p")
            print(f"FPS        : {selected.get('fps', 'N/A')}")
            print(f"Format     : {selected.get('ext')}")
            print(f"Views      : {info.get('view_count', 'N/A')}")

            confirm = input("\nDo you want to download this? (Y/N):\t").strip().lower()

            if confirm == 'y':
                download_video(url, selected_id)
            else:
                print("Download cancelled.")

    except Exception as e:
        error_msg = str(e)
        print("\n" + "=" * 55)

        if is_network_or_filter_error(error_msg):
            print("❌ Cannot connect to YouTube!")
            print()
            print("Possible reasons:")
            print("  • YouTube is filtered/blocked in your network (Iran)")
            print("  • Connection was forcibly closed by firewall/DPI")
            print("  • No internet or DNS problem")
            print()
            print("➡️ Solution: Turn on a good VPN and try again.")
        else:
            print("❌ Error:")
            print(f"  {error_msg}")

        print("=" * 55)


def download_video(url, format_id):

    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0%').strip()
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')

            print(
                f"\rDownloading... {percent} | Speed: {speed} | ETA: {eta}",
                end='',
                flush=True
            )

        elif d['status'] == 'finished':
            print("\n\nDownload finished. Processing...")

    ydl_opts = {
        'format': format_id,
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'noplaylist': True,
        'merge_output_format': 'mp4',
        'socket_timeout': 30,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download completed successfully!\n")

    except Exception as e:
        error_msg = str(e)
        print("\n" + "=" * 55)

        if is_network_or_filter_error(error_msg):
            print("❌ Download failed - Cannot access YouTube!")
            print("➡️ Please turn on VPN and try again.")
        else:
            print("❌ Download Error:")
            print(f"  {error_msg}")

        print("=" * 55)


def main():
    print("--- YouTube Downloader (yt-dlp) ---")

    while True:
        url = input("\nEnter Video URL (or q to quit):\t").strip()

        if url.lower() == 'q':
            break

        if not url:
            continue

        format_selector(url)


if __name__ == '__main__':
    main()
