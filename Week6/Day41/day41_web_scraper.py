import requests
from bs4 import BeautifulSoup

print("==== SIMPLE WEB SCRAPER ====")

url = "https://cnn.com"

try:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # Get page title
    title = soup.title.text
    print(f"Page Title: {title}")

    # Get all links
    print("\n--- LINKS ---")
    links = soup.find_all("a")
    headings = soup.find_all("h1")

    with open("links.txt", "w") as f:
        for link in links:
            href = link.get("href")
            f.write(str(href) + "\n")

    print("\n--- HEADINGS ---")
    for heading in headings:
        print(heading.text)

    with open("headings.txt", "w") as f:
        for heading in headings:
            f.write(str(heading.text) + "\n")

except Exception as e:
    print("Error:", e)