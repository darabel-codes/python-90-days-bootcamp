import requests
import csv
from bs4 import BeautifulSoup
import json
import time

print ("===== JOB SCRAPER TO CSV =====")

url = "https://realpython.github.io/fake-jobs/"

def scrape_jobs():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("div", class_ = "card-content")

    results = []

    for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p").text.strip()
    
        results.append({
            "title": title,
            "company": company,
            "location": location,
            "date": time.strftime("%Y-%m-%d")
        })

    return results

try:
    jobs = scrape_jobs()
    with open("jobs.csv", "w", newline="", encoding ="utf-8") as csvfile:
        fieldnames = ["title", "company", "location", "date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for job in jobs:
            writer.writerow(job)
            
    print(f"{len(jobs)} jobs have been successfully saved to jobs.csv")

except Exception as error:
    print(f"An error occurred: {error}")