import requests
from bs4 import BeautifulSoup
import re

def extract_audio_url(page_url):
    # Fetch the page
    response = requests.get(page_url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # 1. Look for <audio> tags
    audio_tag = soup.find("audio")
    if audio_tag and audio_tag.get("src"):
        return audio_tag["src"]

    # 2. Look for <source> tags inside audio
    source_tag = soup.find("source")
    if source_tag and source_tag.get("src"):
        return source_tag["src"]

    # 3. Regex search for stream URLs in scripts (common for radio sites)
    matches = re.findall(r'(https?://[^\s"\']+\.m3u8|https?://[^\s"\']+\.mp3)', response.text)
    if matches:
        return matches[0]

    return None


if __name__ == "__main__":
    url = "https://radiosindia.com/hellofm.html"# or "https://radiosindia.com/hellofm.html" or "https://listen.openstream.co/4428"  
    audio_url = extract_audio_url(url)
    if audio_url:
        print("Direct audio URL:", audio_url)
        print("You can play it in VLC like:")
        print(f"vlc {audio_url}")
    else:
        print("No audio URL found.")
