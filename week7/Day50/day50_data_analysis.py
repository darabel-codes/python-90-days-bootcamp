import json
from collections import Counter

print("==== JOB DATA ANALYSIS ====")

# Load your JSON file
with open("clean_jobs.json", "r", encoding="utf-8") as file:
    jobs = json.load(file)

try:
    with open("report.txt", "w") as f:
        # Total jobs
        total_jobs = len(jobs)
        # print(f"Total jobs: {total_jobs}")
        f.write(f"Total jobs: {total_jobs}\n\n")

        # Count companies
        companies = [job["company"] for job in jobs]
        company_count = Counter(companies)

        f.write("Top Companies Hiring:\n")
        for company, count in company_count.most_common(5):
            f.write(f"{company}: {count}\n")
        
        # Count locations
        locations = [job["location"] for job in jobs]
        location_count = Counter(locations)
        f.write("\nTop Locations:\n")
        for location, count in location_count.most_common(5):
            f.write(f"{location}: {count}\n")
        
        # Keyword analysis
        python_jobs = [job for job in jobs if "python" in job["title"].lower()]
        # print(f"\nPython-related jobs: {len(python_jobs)}")
        f.write(f"\nPython-related jobs: {len(python_jobs)}\n")
        
        # Most common job titles
        titles = [job["title"] for job in jobs]
        title_count = Counter(titles)

        f.write("\nTop Job Titles:\n")
        for title, count in title_count.most_common(5):
            f.write(f"{title}: {count}\n")
        
        remote_jobs = [job for job in jobs if "remote" in job["location"].lower()]
        f.write(f"\nRemote jobs: {len(remote_jobs)}\n")
        
        # Percentage of Python Jobs
        python_percentage = (len(python_jobs) / total_jobs) * 100
        f.write(f"\nPercentage of Python-related jobs: {python_percentage:.2f}%\n")

    print("Report has been generated successfully in report.txt")

except Exception as error:
    print(f"An error occurred during analysis: {error}")




