import httpx
import time
from datetime import datetime

URLS = [
    "https://google.com",
    "https://github.com",
    "https://httpbin.org/status/500",
]

def check(url):
    start = time.time()
    try:
        response = httpx.get(url, timeout=10, follow_redirects=True)
        ms = round((time.time() - start) * 1000)
        return {"url": url, "up": response.status_code < 500, "ms": ms, "code": response.status_code}
    except Exception as e:
        return {"url": url, "up": False, "ms": None, "error": str(e)}

def log(result):
    now = datetime.now().strftime("%H:%M:%S")
    icon = "✓" if result["up"] else "✗"
    ms = f"{result['ms']}ms" if result.get("ms") else "timeout"
    print(f"[{now}] {icon}  {result['url']}  {ms}")

print("Checking URLs...\n")
while True:
    for url in URLS:
        log(check(url))
    print("---")
    time.sleep(60)