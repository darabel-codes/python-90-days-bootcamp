import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

print("==== SMART JOB ALERT BOT ====")

url = "https://realpython.github.io/fake-jobs/"

seen_jobs = set()

def scrape_jobs():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")

    results = []

    for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p").text.strip()

        job_id = f"{title}-{company}"

        results.append({
            "id": job_id,
            "title": title,
            "company": company,
            "location": location,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return results


try:
    while True:
        print("\nChecking for new jobs...")

        jobs = scrape_jobs()

        for job in jobs:
            if job["id"] not in seen_jobs:
                print("\n🚨 NEW JOB FOUND!")
                print(f"Title: {job['title']}")
                print(f"Company: {job['company']}")
                print(f"Location: {job['location']}")
                print(f"Time: {job['time']}")

                seen_jobs.add(job["id"])

        time.sleep(10)

except KeyboardInterrupt:
    print("\nStopped by user.")