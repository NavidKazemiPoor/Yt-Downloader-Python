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


def print_network_error(is_download: bool = False):
    print("\n" + "=" * 55)
    if is_download:
        print("❌ Download failed - Cannot access YouTube!")
        print("➡️ Please turn on VPN and try again.")
    else:
        print("❌ Cannot connect to YouTube!")
        print()
        print("Possible reasons:")
        print("  • YouTube is filtered/blocked in your network (Iran)")
        print("  • Connection was forcibly closed by firewall/DPI")
        print("  • No internet or DNS problem")
        print()
        print("➡️ Solution: Turn on a good VPN and try again.")
    print("=" * 55)


def print_generic_error(error_msg: str):
    print("\n" + "=" * 55)
    print("❌ Error:")
    print(f"  {error_msg}")
    print("=" * 55)