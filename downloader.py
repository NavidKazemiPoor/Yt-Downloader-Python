import yt_dlp
from errors import is_network_or_filter_error, print_network_error, print_generic_error


class YouTubeDownloader:
    def __init__(self, socket_timeout: int = 30):
        self.socket_timeout = socket_timeout

    def get_info(self, url: str) -> dict | None:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "socket_timeout": 15,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            error_msg = str(e)
            if is_network_or_filter_error(error_msg):
                print_network_error(is_download=False)
            else:
                print_generic_error(error_msg)
            return None

    def get_valid_formats(self, info: dict) -> list:
        formats = info.get("formats", [])
        valid = []
        for f in formats:
            if f.get("vcodec") != "none" and f.get("height"):
                valid.append(f)
        return valid

    def print_formats(self, formats: list):
        print("\n--- Available Formats ---\n")
        print(f"{'ID':<8} {'Resolution':<12} {'FPS':<6} {'Ext':<6} {'Size':<10} {'Type'}")
        print("-" * 60)

        for f in formats:
            filesize = f.get("filesize") or f.get("filesize_approx")
            size_str = f"{filesize / 1024 / 1024:.1f} MB" if filesize else "N/A"
            fps = f.get("fps") or "-"
            print(
                f"{f['format_id']:<8} "
                f"{f.get('height', 'N/A')}p{'':<7} "
                f"{str(fps):<6} "
                f"{f.get('ext', ''):<6} "
                f"{size_str:<10} "
                f"{f.get('format_note', '')}"
            )

    def print_summary(self, info: dict, selected: dict):
        print("\n--- Summary ---")
        print(f"Title      : {info.get('title')}")
        print(f"Duration   : {info.get('duration', 0) / 60:.2f} min")
        print(f"Resolution : {selected.get('height')}p")
        print(f"FPS        : {selected.get('fps', 'N/A')}")
        print(f"Format     : {selected.get('ext')}")
        print(f"Views      : {info.get('view_count', 'N/A')}")

    def download(self, url: str, format_id: str) -> bool:
        def progress_hook(d):
            if d["status"] == "downloading":
                percent = d.get("_percent_str", "0%").strip()
                speed = d.get("_speed_str", "N/A")
                eta = d.get("_eta_str", "N/A")
                print(
                    f"\rDownloading... {percent} | Speed: {speed} | ETA: {eta}",
                    end="",
                    flush=True,
                )
            elif d["status"] == "finished":
                print("\n\nDownload finished. Processing...")

        ydl_opts = {
            "format": format_id,
            "outtmpl": "%(title)s.%(ext)s",
            "progress_hooks": [progress_hook],
            "noplaylist": True,
            "merge_output_format": "mp4",
            "socket_timeout": self.socket_timeout,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Download completed successfully!\n")
            return True
        except Exception as e:
            error_msg = str(e)
            if is_network_or_filter_error(error_msg):
                print_network_error(is_download=True)
            else:
                print_generic_error(error_msg)
            return False