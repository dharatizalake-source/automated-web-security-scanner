"""
Automated Web Security Header Scanner
Author: Dharati Zalake

Purpose:
Checks security-related HTTP response headers for a website that you own
or have explicit permission to assess. This is a basic educational checker,
not a full penetration-testing tool.

Run:
    python Dharati_Zalake_AutomatedWebScanner.py
Then enter an authorized website URL when prompted.
"""

from urllib.parse import urlparse
import requests

SECURITY_HEADERS = {
    "Strict-Transport-Security": (
        "Helps browsers use HTTPS for future visits. Relevant for HTTPS sites."
    ),
    "Content-Security-Policy": (
        "Can help reduce cross-site scripting and other content-injection risks."
    ),
    "X-Content-Type-Options": (
        "Usually set to 'nosniff' to reduce MIME-type sniffing."
    ),
    "X-Frame-Options": (
        "Can help prevent clickjacking; CSP frame-ancestors is a modern alternative."
    ),
    "Referrer-Policy": (
        "Controls how much referrer information browsers send."
    ),
    "Permissions-Policy": (
        "Lets a site restrict access to selected browser features."
    ),
}

def normalize_url(raw_url):
    """Validate and normalize a user-provided HTTP(S) URL."""
    raw_url = raw_url.strip()
    if not raw_url:
        raise ValueError("No URL was entered.")
    if "://" not in raw_url:
        raw_url = "https://" + raw_url
    parsed = urlparse(raw_url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("Enter a valid http:// or https:// website URL.")
    if parsed.username or parsed.password:
        raise ValueError("URLs containing usernames or passwords are not accepted.")
    return raw_url

def scan_website(url):
    """Make one ordinary GET request and inspect the returned headers."""
    response = requests.get(
        url,
        timeout=10,
        allow_redirects=True,
        headers={"User-Agent": "Educational-Web-Header-Scanner/1.0"},
    )
    final_url = response.url
    print("\n=== Scan summary ===")
    print(f"Requested URL: {url}")
    print(f"Final URL:     {final_url}")
    print(f"HTTP status:   {response.status_code}")
    print(f"HTTPS used:    {urlparse(final_url).scheme == 'https'}")
    print("\n=== Security header checks ===")

    present = 0
    for header, explanation in SECURITY_HEADERS.items():
        value = response.headers.get(header)
        if value:
            present += 1
            print(f"[PRESENT] {header}: {value}")
        else:
            print(f"[MISSING] {header}")
        print(f"          Why it matters: {explanation}")

    print(f"\nResult: {present} of {len(SECURITY_HEADERS)} checked headers were present.")
    print("Note: A missing header is a review item, not proof that the website is vulnerable.")
    print("This tool does not test for exploits, inspect application code, or certify security.")

def main():
    print("Automated Web Security Header Scanner")
    print("Use only on a website you own or have permission to assess.")
    raw_url = input("Enter authorized website URL (example: https://example.com): ")
    try:
        url = normalize_url(raw_url)
        scan_website(url)
    except ValueError as exc:
        print(f"Input error: {exc}")
    except requests.exceptions.SSLError:
        print("Connection failed because TLS/SSL verification failed. Check the URL/certificate.")
    except requests.exceptions.Timeout:
        print("The website did not respond within 10 seconds.")
    except requests.exceptions.RequestException as exc:
        print(f"Could not complete the request: {exc}")

if __name__ == "__main__":
    main()
