from flask import Flask, render_template, redirect
import json
import os
from scraper import scrape_jobs
from cleaner import clean_jobs
from analyzer import analyze_jobs

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

json_path = os.path.join(DATA_DIR, "jobs.json")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/loading")
def loading():
    return render_template("loading.html")


@app.route("/scrape")
def scrape():
    jobs = scrape_jobs()
    cleaned = clean_jobs(jobs)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=4)

    return redirect("/")


@app.route("/report")
def report():
    if not os.path.exists(json_path):
        return "No data found. Please scrape first."

    with open(json_path, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    report_data = analyze_jobs(jobs)

    return render_template("report.html", report=report_data)


if __name__ == "__main__":
    app.run(debug=True)