import requests
import time

# OWASP ZAP API configuration
ZAP_API_URL = "http://localhost:8080"  # Default ZAP API URL
API_KEY = "9q6l7eldvepa1qortq792fuf1j"  # Replace with your actual ZAP API key


def spider_target(target_url):
    """Start a spider to add the target to the ZAP site tree."""
    response = requests.get(
        f"{ZAP_API_URL}/JSON/spider/action/scan/",
        params={"url": target_url, "apikey": API_KEY},
    )
    if response.status_code == 200:
        spider_id = response.json().get("scan")
        print(f"Spider started for {target_url}. Spider ID: {spider_id}")
        return spider_id
    else:
        print(f"Failed to start spider: {response.text}")
        return None


def get_spider_status(spider_id):
    """Check the progress of a spider scan."""
    response = requests.get(
        f"{ZAP_API_URL}/JSON/spider/view/status/",
        params={"scanId": spider_id, "apikey": API_KEY},
    )
    if response.status_code == 200:
        return response.json().get("status")
    else:
        print(f"Failed to get spider status: {response.text}")
        return None


def start_scan(target_url):
    """Start an active scan on the target URL."""
    response = requests.get(
        f"{ZAP_API_URL}/JSON/ascan/action/scan/",
        params={"url": target_url, "apikey": API_KEY},
    )
    if response.status_code == 200:
        scan_id = response.json().get("scan")
        print(f"Active scan started for {target_url}. Scan ID: {scan_id}")
        return scan_id
    else:
        print(f"Failed to start scan: {response.text}")
        return None


def get_scan_status(scan_id):
    """Check the progress of an active scan."""
    response = requests.get(
        f"{ZAP_API_URL}/JSON/ascan/view/status/",
        params={"scanId": scan_id, "apikey": API_KEY},
    )
    if response.status_code == 200:
        return response.json().get("status")
    else:
        print(f"Failed to get scan status: {response.text}")
        return None


def get_scan_results():
    """Retrieve the scan results."""
    response = requests.get(
        f"{ZAP_API_URL}/JSON/core/view/alerts/",
        params={"apikey": API_KEY},
    )
    if response.status_code == 200:
        return response.json().get("alerts")
    else:
        print(f"Failed to get scan results: {response.text}")
        return []
