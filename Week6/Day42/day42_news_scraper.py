import requests
from bs4 import BeautifulSoup

print("==== NEWS SCRAPER ====")

url = "https://legit.ng"   # you can change this later

try:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("a")

    results = []

    for link in headlines:
        title = link.text.strip()
        href = link.get("href")

        if title and href:
            results.append((title, href))

    print("\n--- HEADLINES ---")
    for i, (title, link) in enumerate(results[:10], start=1):
        print(f"{i}. {title}")
        print(f"   {link}")

    # Save to file
    with open("news.txt", "w", encoding="utf-8") as file:
        for title, link in results:
            file.write(f"{title}\n{link}\n\n")

    print("\nSaved to news.txt")

except Exception as e:
    print("Error:", e)