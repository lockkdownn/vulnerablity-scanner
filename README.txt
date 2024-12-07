# Vulnerability Scanner Application

This application is a web-based tool for performing vulnerability scans on websites using OWASP ZAP. It automates tasks such as spidering, active scanning, and report generation to help identify and document potential security vulnerabilities.

---

## Features
- **Target Spidering**: Crawl a target website to map its structure.
- **Active Scanning**: Identify vulnerabilities using OWASP ZAP.
- **Report Generation**: Generate detailed PDF reports of scan results.
- **Web Interface**: Simple web interface built with Flask for ease of use.

---

## Requirements
- **Python 3.x**
- Flask (`pip install flask`)
- ReportLab (`pip install reportlab`)
- OWASP ZAP (with API enabled)

---

## File Structure
- `app.py`: The main application file handling routes and user interactions.
- `scan.py`: Module to interact with the OWASP ZAP API for scanning operations.
- `report.py`: Generates PDF reports of scan results.
- `templates/`: HTML templates for the web interface.
- `reports/`: Directory where generated reports are stored.

---
# IMP FILES needed to be create 

Set up a `reports` folder to store all generated reports, ensuring they are saved in the designated directory. Additionally, create a `templates` folder to house the `index.html` file for the web interface.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/lockkdownn/vulnerablity-scanner.git    
    cd vulnerability-scanner
    ```

2. Install the required Python packages:
    ```bash
    pip install flask reportlab
    ```

3. Ensure OWASP ZAP is installed and running:
    - Download and install [OWASP ZAP](https://www.zaproxy.org/).
    - Enable the API by modifying ZAP settings or using the command-line options.

4. Update the API key in `scan.py`:
    Replace the placeholder `API_KEY` with your ZAP API key.

---

## Usage
1. Start the Flask application:
    bash
    python app.py
    

2. Open the web interface:
    Navigate to `http://127.0.0.1:5000` in your browser.

3. Enter the target URL and initiate the scan. Once complete, download the generated report.

---

## Notes
- Ensure ZAP is configured to allow connections from the application.
- Results may vary based on target site configurations and permissions.

---

## Disclaimer
This tool is intended for ethical use only. Ensure you have proper authorization before scanning any target. Unauthorized scanning may violate laws or agreements.
