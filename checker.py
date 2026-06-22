import httpx
import time
from datetime import datetime
from database import init_db, SessionLocal, PingResult
from dotenv import load_dotenv
import os

load_dotenv()

URLS = [u.strip() for u in os.environ.get("MONITOR_TARGETS", "").split(",")]

def check(url):
    start = time.time()
    try:
        response = httpx.get(url, timeout=10, follow_redirects=True)
        ms = round((time.time() - start) * 1000)
        return {"url": url, "up": response.status_code < 500,
                "ms": ms, "code": response.status_code}
    except Exception as e:
        return {"url": url, "up": False, "ms": None, "error": str(e)}

def save(result):
    db = SessionLocal()
    try:
        row = PingResult(
            url=result["url"],
            is_up=result["up"],
            status_code=result.get("code"),
            response_ms=result.get("ms"),
        )
        db.add(row)
        db.commit()
    finally:
        db.close()

def log(result):
    now = datetime.now().strftime("%H:%M:%S")
    icon = "✓" if result["up"] else "✗"
    ms = f"{result['ms']}ms" if result.get("ms") else "timeout"
    print(f"[{now}] {icon}  {result['url']}  {ms}")

init_db()
print("Database ready. Checking URLs...\n")

while True:
    for url in URLS:
        result = check(url)
        save(result)
        log(result)
    print("---")
    time.sleep(60)