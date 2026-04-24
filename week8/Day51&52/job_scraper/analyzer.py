from collections import Counter

def analyze_jobs(jobs):
    total = len(jobs)

    companies = [job["company"] for job in jobs]
    locations = [job["location"] for job in jobs]

    company_count = Counter(companies)
    location_count = Counter(locations)

    report = f"Total Jobs: {total}\n\n"

    report += "Top Companies:\n"
    for c, n in company_count.most_common(5):
        report += f"{c}: {n}\n"

    report += "\nTop Locations:\n"
    for l, n in location_count.most_common(5):
        report += f"{l}: {n}\n"

    return report