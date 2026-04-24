import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

print("==== SMART JOB ALERT BOT ====")

url = "https://realpython.github.io/fake-jobs/"

seen_jobs = set()

# Data cleaning function to standardize text
def clean_text(text):
    return text.strip().lower()


def scrape_jobs():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")

    results = []

    for job in jobs:
        title = clean_text(job.find("h2").text)
        company = clean_text(job.find("h3").text)
        location = clean_text(job.find("p").text)

        job_id = f"{title}-{company}".lower()
        

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

        all_jobs = scrape_jobs()

        unique_jobs = []
        seen = set()

        for job in all_jobs:
            job_id = (job["title"], job["company"])
    
            if job_id not in seen:
                seen.add(job_id)
                unique_jobs.append(job)
        
            with open("clean_jobs.json", "w", encoding="utf-8") as f:
                json.dump(unique_jobs, f, indent=4)
        # for job in jobs:
        #     if job["id"] not in seen_jobs:
        #         print("\n🚨 NEW JOB FOUND!")
        #         print(f"Title: {job['title']}")
        #         print(f"Company: {job['company']}")
        #         print(f"Location: {job['location']}")
        #         print(f"Time: {job['time']}")

        #         seen_jobs.add(job["id"])

        time.sleep(10)
        
        

except KeyboardInterrupt:
    print("\nStopped by user.")