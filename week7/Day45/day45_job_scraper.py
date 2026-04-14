import requests
from bs4 import BeautifulSoup
import json
import time

print("==== JOB SCRAPER ====")

base_url = "https://realpython.github.io/fake-jobs/"  # replace later

jobs = []

try:
    for page in range(1, 4):
        print(f"\nScraping page {page}...")

        url = base_url + str(page)
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        job_cards = soup.find_all("div", class_="job")  # adjust later

        for job in job_cards:
            title_tag = job.find("h2")
            company_tag = job.find("span", class_="company")
            link_tag = job.find("a")

            if title_tag and company_tag and link_tag:
                job_data = {
                    "title": title_tag.text.strip(),
                    "company": company_tag.text.strip(),
                    "link": link_tag.get("href")
                }

                jobs.append(job_data)

        time.sleep(2)

    print(f"\nTotal jobs found: {len(jobs)}")

    # Save to JSON
    with open("jobs.json", "w", encoding="utf-8") as file:
        json.dump(jobs, file, indent=4)

    print("Saved to jobs.json")

except Exception as e:
    print("Error:", e)