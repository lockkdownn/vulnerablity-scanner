from flask import Flask, render_template, request, send_file
from scan import spider_target, get_spider_status, start_scan, get_scan_status, get_scan_results
from report import generate_report
import time
import os

app = Flask(__name__)
REPORTS_DIR = "reports"  # Directory to save reports

# Ensure the reports directory exists
os.makedirs(REPORTS_DIR, exist_ok=True)


@app.route("/")
def home():
    """Render the home page with a form to start a scan."""
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    """Start a vulnerability scan for the provided URL."""
    target = request.form["url"]
    if not target:
        return "Error: Please provide a target URL.", 400

    # Spider the target
    spider_id = spider_target(target)
    if not spider_id:
        return "Error: Failed to start spider scan.", 500

    # Wait for the spider to complete
    while True:
        spider_status = get_spider_status(spider_id)
        if spider_status == "100":  # Spider completed
            break
        time.sleep(5)

    # Start the active scan
    scan_id = start_scan(target)
    if not scan_id:
        return "Error: Failed to start active scan.", 500

    # Wait for the active scan to complete
    while True:
        scan_status = get_scan_status(scan_id)
        if scan_status == "100":  # Scan completed
            break
        time.sleep(10)

    # Retrieve scan results
    results = get_scan_results()

    # Generate a report
    report_file = os.path.join(REPORTS_DIR, f"report_{int(time.time())}.pdf")
    generate_report(report_file, results)

    return f"Scan complete! Download your report <a href='/download?file={report_file}'>here</a>."


@app.route("/download")
def download():
    """Download a generated report."""
    file_path = request.args.get("file")
    if not file_path or not os.path.exists(file_path):
        return "Error: File not found.", 404
    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
