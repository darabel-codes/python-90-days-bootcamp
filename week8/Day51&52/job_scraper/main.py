import os
print("Current working directory:", os.getcwd())



import json
import csv
import os
from scraper import scrape_jobs
from cleaner import clean_jobs
from analyzer import analyze_jobs


os.makedirs("data", exist_ok=True)

print("==== SMART JOB TRACKER ====")

# Step 1: Scrape
jobs = scrape_jobs()

# Step 2: Clean
cleaned_jobs = clean_jobs(jobs)

# Step 3: Save JSON
with open("data/jobs.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_jobs, f, indent=4)

# Step 4: Save CSV
with open("data/jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "company", "location"])
    writer.writeheader()
    writer.writerows(cleaned_jobs)

# Step 5: Analyze
report = analyze_jobs(cleaned_jobs)

# Step 6: Save Report
with open("data/report.txt", "w") as f:
    f.write(report)

print("\n✅ Project Completed Successfully!")
print(report)