def clean_jobs(jobs):
    seen = set()
    clean_list = []

    for job in jobs:
        title = job["title"].strip().lower()
        company = job["company"].strip().lower()
        location = job["location"].strip().lower()

        job_id = (title, company)

        if job_id not in seen:
            seen.add(job_id)
            clean_list.append({
                "title": title.title(),
                "company": company.title(),
                "location": location.title()
            })

    return clean_list