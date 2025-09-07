import requests
import os
from urllib.parse import urlparse
import hashlib

def generate_unique_filename(url, existing_files):
    """
    Generate a unique filename from the URL.
    If no filename exists in URL, create one using a hash.
    Prevents overwriting duplicates.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename:  # If URL has no filename
        filename = "downloaded_image.jpg"

    # Check for duplicates
    if filename in existing_files:
        # Append hash of URL to make it unique
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{url_hash}{ext}"

    return filename


def fetch_image(url, folder="Fetched_Images"):
    """Fetch a single image from a URL and save it into folder."""
    try:
        # Ensure folder exists
        os.makedirs(folder, exist_ok=True)

        # Request with headers (be respectful to servers)
        headers = {"User-Agent": "UbuntuImageFetcher/1.0"}
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()  # Raise error for HTTP issues

        # Check content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped: {url} (Not an image)")
            return None

        # Get existing files in folder
        existing_files = set(os.listdir(folder))

        # Generate filename safely
        filename = generate_unique_filename(url, existing_files)

        # Save file
        filepath = os.path.join(folder, filename)
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return filename

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")
    return None


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs (comma-separated)
    urls = input("Please enter one or more image URLs (separated by commas): ").split(",")

    for url in urls:
        url = url.strip()
        if url:
            fetch_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
