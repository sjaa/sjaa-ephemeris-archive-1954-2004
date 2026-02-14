#!/usr/bin/env python3
"""
Download SJAA Ephemeris newsletter PDFs from the SJAA website.

Scrapes https://www.sjaa.net/about/sjaa-newsletter-ephemeris/ for PDF links
and downloads them into the appropriate date-ranged folder in this project.

Usage:
    python scripts/download_newsletters.py [--start-year YEAR] [--dry-run] [--include-bw]
"""

import argparse
import os
import re
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin

BASE_URL = "https://www.sjaa.net"
NEWSLETTER_URL = f"{BASE_URL}/about/sjaa-newsletter-ephemeris/"

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Map year ranges to folder names
YEAR_RANGES = [
    (2005, 2009, "2005-2009"),
    (2010, 2019, "2010-2019"),
    (2020, 2029, "2020-2029"),
]


class PDFLinkExtractor(HTMLParser):
    """Extract all <a> tags with href ending in .pdf."""

    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href", "")
            if href.lower().endswith(".pdf"):
                self.links.append(href)


def fetch_page(url):
    """Fetch a webpage and return its HTML content."""
    req = urllib.request.Request(
        url, headers={"User-Agent": "SJAA-Archive-Downloader/1.0"}
    )
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


def extract_pdf_links(html):
    """Extract all PDF links from HTML content."""
    parser = PDFLinkExtractor()
    parser.feed(html)
    return parser.links


def resolve_url(href):
    """Resolve a potentially relative URL to an absolute one."""
    if href.startswith("http"):
        return href
    return urljoin(BASE_URL, href)


def extract_date_from_url(url):
    """
    Extract (year, month) from a PDF URL.

    Handles these URL patterns:
      /wp-content/uploads/YYYY/MM/...
      /eph/YYYY-MM/...
      /eph/YYMM/...

    Returns (year, month) tuple or None if date can't be determined.
    """
    # Pattern: /wp-content/uploads/YYYY/MM/...
    m = re.search(r"/wp-content/uploads/(\d{4})/(\d{2})/", url)
    if m:
        return int(m.group(1)), int(m.group(2))

    # Pattern: /eph/YYYY-MM/...
    m = re.search(r"/eph/(\d{4})-(\d{2})/", url)
    if m:
        return int(m.group(1)), int(m.group(2))

    # Pattern: /eph/YYMM/... (e.g., /eph/0501/, /eph/1312/)
    m = re.search(r"/eph/(\d{2})(\d{2})/", url)
    if m:
        yy = int(m.group(1))
        mm = int(m.group(2))
        year = 2000 + yy if yy < 50 else 1900 + yy
        return year, mm

    return None


def get_target_folder(year):
    """Get the date-range folder name for a given year."""
    for start, end, folder in YEAR_RANGES:
        if start <= year <= end:
            return folder
    return None


def is_bw_pdf(url):
    """Check if a URL points to a black-and-white version."""
    return "BW" in os.path.basename(url)


def download_file(url, dest_path, dry_run=False):
    """Download a file from URL to dest_path."""
    if dry_run:
        print(f"  [DRY RUN] Would download: {url}")
        print(f"         -> {os.path.relpath(dest_path, PROJECT_ROOT)}")
        return True

    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "SJAA-Archive-Downloader/1.0"}
        )
        with urllib.request.urlopen(req) as response:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(dest_path, "wb") as f:
                f.write(response.read())
        print(f"  Downloaded: {os.path.relpath(dest_path, PROJECT_ROOT)}")
        return True
    except urllib.error.HTTPError as e:
        print(f"  ERROR ({e.code}): {url}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"  ERROR: {url} - {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Download SJAA Ephemeris newsletter PDFs"
    )
    parser.add_argument(
        "--start-year",
        type=int,
        default=2005,
        help="First year to download (default: 2005)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be downloaded without actually downloading",
    )
    parser.add_argument(
        "--include-bw",
        action="store_true",
        help="Also download black-and-white versions of PDFs",
    )
    args = parser.parse_args()

    print(f"Fetching newsletter page...")
    html = fetch_page(NEWSLETTER_URL)

    raw_links = extract_pdf_links(html)
    print(f"Found {len(raw_links)} PDF links on page")

    # Process and filter links
    downloads = []
    skipped = 0
    for href in raw_links:
        url = resolve_url(href)
        date = extract_date_from_url(url)
        if date is None:
            print(f"  Warning: can't parse date from URL, skipping: {href}")
            skipped += 1
            continue

        year, month = date
        if year < args.start_year:
            skipped += 1
            continue

        if is_bw_pdf(url) and not args.include_bw:
            skipped += 1
            continue

        folder = get_target_folder(year)
        if folder is None:
            print(f"  Warning: no folder mapping for year {year}, skipping: {href}")
            skipped += 1
            continue

        # Build YYMM subfolder code (matches existing project convention)
        yymm = f"{year % 100:02d}{month:02d}"
        filename = os.path.basename(url)
        dest = os.path.join(PROJECT_ROOT, folder, yymm, filename)

        downloads.append((url, dest, year, month))

    print(f"\n{len(downloads)} PDFs to download, {skipped} skipped")

    # Sort by date
    downloads.sort(key=lambda x: (x[2], x[3]))

    # Download
    success = 0
    existed = 0
    fail = 0
    for url, dest, year, month in downloads:
        if os.path.exists(dest):
            print(f"  Exists: {os.path.relpath(dest, PROJECT_ROOT)}")
            existed += 1
            continue

        if download_file(url, dest, dry_run=args.dry_run):
            success += 1
        else:
            fail += 1

        # Brief pause between downloads to be polite to the server
        if not args.dry_run:
            time.sleep(0.5)

    print(f"\nDone: {success} downloaded, {existed} already existed, {fail} failed")


if __name__ == "__main__":
    main()
