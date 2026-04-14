import requests
from bs4 import BeautifulSoup
import json
import time

print("==== JSON WEB SCRAPER ====")

base_url = "https://goal.com/ng/page/"

all_results = []

try:
    for page in range(1, 6):
        print(f"\nScraping page {page}...")
        
        url = base_url + str(page)
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        links = soup.find_all("a")
        
        for link in links:
            title = link.text.strip()
            href = link.get("href")
            
            if title and href and href != "#":
                item = {
                    "title": title,
                    "link": href
                }
                all_results.append(item)
            
        time.sleep(2)  # Be polite and avoid overwhelming the server
        print(f"\nTotal items collected: {len(all_results)}")
            # Save to JSON file
            
    with open("scraper.json", "w", encoding="utf-8") as file:
        json.dump(all_results, file, indent=4)
            
    print("\nSaved to scraper.json")
except Exception as e:
    print("Error:", e)