import requests
from bs4 import BeautifulSoup

print("==== MULTI-PAGE SCRAPER ====")

base_url = "https://legit.ng?page="  # change this later

all_results = []

try:
    for page in range(1, 6):   # scrape 5 pages
        print(f"\nScraping page {page}...")

        url = base_url + str(page)
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a")

        for link in links:
            title = link.text.strip()
            href = link.get("href")

            if title and href != "#":
                all_results.append((title, href))

    print("\n--- RESULTS ---")

    for i, (title, link) in enumerate(all_results[:15], start=1):
        print(f"{i}. {title}")
        print(f"   {link}")

    # Save to file
    with open("multi_page_results.txt", "w", encoding="utf-8") as f:
        for title, link in all_results:
            f.write(f"{title}\n{link}\n\n")

    print("\nSaved to multi_page_results.txt")

except Exception as e:
    print("Error:", e)