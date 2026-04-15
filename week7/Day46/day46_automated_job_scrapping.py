import requests
from bs4 import BeautifulSoup
import json
import time

print("==== JOB TRACKER BOT ====")

url = "https://realpython.github.io/fake-jobs/"

all_jobs = []

def scrape_jobs():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")

    new_jobs = []

    for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p").text.strip()

        job_data = {
            "title": title,
            "company": company,
            "location": location
        }

        new_jobs.append(job_data)

    return new_jobs


try:
    while True:
        print("\nChecking for jobs...")

        jobs = scrape_jobs()

        for job in jobs:
            if job not in all_jobs:
                print(f"New job found: {job['title']}")
                all_jobs.append(job)

        # Save to JSON
        with open("jobs.json", "w", encoding="utf-8") as file:
            json.dump(all_jobs, file, indent=4)

        print(f"Total saved jobs: {len(all_jobs)}")

        time.sleep(10)  # check every 10 seconds

except KeyboardInterrupt:
    print("\nStopped by user.")