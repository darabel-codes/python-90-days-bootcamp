import json
import csv
import os
from scraper import scrape_jobs
from cleaner import clean_jobs
from analyzer import analyze_jobs

# Ensure data folder exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

json_path = os.path.join(DATA_DIR, "jobs.json")
csv_path = os.path.join(DATA_DIR, "jobs.csv")
report_path = os.path.join(DATA_DIR, "report.txt")


def scrape_and_save():
    jobs = scrape_jobs()
    cleaned = clean_jobs(jobs)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=4)

    print(f"\n✅ Saved {len(cleaned)} jobs to JSON")


def export_csv():
    if not os.path.exists(json_path):
        print("⚠️ No data found. Run scraper first.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "company", "location"])
        writer.writeheader()
        writer.writerows(jobs)

    print("✅ Exported to CSV")


def view_report():
    if not os.path.exists(json_path):
        print("⚠️ No data found. Run scraper first.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    report = analyze_jobs(jobs)

    with open(report_path, "w") as f:
        f.write(report)

    print("\n📊 JOB REPORT")
    print(report)


def main():
    while True:
        print("\n==== JOB TRACKER MENU ====")
        print("1. Scrape Jobs")
        print("2. View Report")
        print("3. Export to CSV")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            scrape_and_save()

        elif choice == "2":
            view_report()

        elif choice == "3":
            export_csv()

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()