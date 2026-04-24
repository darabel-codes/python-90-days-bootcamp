import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("div", class_="card-content")

    results = []

    for job in jobs:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p").text.strip()

        results.append({
            "title": title,
            "company": company,
            "location": location
        })

    return results