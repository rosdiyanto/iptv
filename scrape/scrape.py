import requests
from urllib.parse import urlparse

url = "http://target_url_iptv.com"

headers = {
    "User-Agent": "OTT Navigator/1.6.9.1 (Linux; Android 11)",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": f"{urlparse(url).scheme}://{urlparse(url).netloc}/",
    "Origin": f"{urlparse(url).scheme}://{urlparse(url).netloc}"
}

r = requests.get(url, headers=headers, timeout=30)

print("Status:", r.status_code)

if r.status_code == 200:
    with open("full.m3u", "w", encoding="utf-8") as f:
        f.write(r.text)

    print("full berhasil disimpan sebagai full.m3u")
else:
    print("Gagal mengambil playlist")