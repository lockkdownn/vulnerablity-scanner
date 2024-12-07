from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_report(file_name, findings):
    """Generate a PDF report of the scan results."""
    c = canvas.Canvas(file_name, pagesize=letter)
    c.setFont("Helvetica", 10)

    # Report title and metadata
    c.drawString(100, 750, "Vulnerability Scan Report")
    c.drawString(100, 730, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(100, 710, "Scan Results:")

    # Column headers with better spacing
    c.drawString(50, 690, "No.")
    c.drawString(100, 690, "Alert")
    c.drawString(300, 690, "Severity")
    c.drawString(450, 690, "URL")

    y = 670  # Start writing below the header

    for idx, finding in enumerate(findings, start=1):
        # Align the text into columns, truncating if the text is too long for the column
        c.drawString(50, y, str(idx))
        alert_text = finding['alert']
        severity_text = finding['risk']
        url_text = finding['url']

        # Ensure the text fits into the columns
        if len(alert_text) > 20:
            alert_text = alert_text[:17] + "..."
        if len(severity_text) > 10:
            severity_text = severity_text[:7] + "..."
        if len(url_text) > 40:
            url_text = url_text[:37] + "..."

        c.drawString(100, y, alert_text)
        c.drawString(300, y, severity_text)
        c.drawString(450, y, url_text)
        
        y -= 20  # Move down for the next line
        if y < 50:  # Start a new page if we run out of space
            c.showPage()
            y = 750
            # Reprint headers on the new page
            c.drawString(50, y, "No.")
            c.drawString(100, y, "Alert")
            c.drawString(300, y, "Severity")
            c.drawString(450, y, "URL")
            y -= 20

    c.save()
    print(f"Report generated: {file_name}")

# Test the report generation (optional)
if __name__ == "__main__":
    test_findings = [
        {"alert": "Missing Anti-clickjacking Header", "risk": "Medium", "url": "http://example.com/"},
        {"alert": "Content Security Policy (CSP) Header Not Set", "risk": "Medium", "url": "http://example.com/sitemap.xml"},
        {"alert": "Content Security Policy (CSP) Header Not Set", "risk": "Medium", "url": "http://example.com/robots.txt"},
        {"alert": "Content Security Policy (CSP) Header Not Set", "risk": "Medium", "url": "http://example.com/"},
        {"alert": "Retrieved from Cache", "risk": "Informational", "url": "http://example.com/robots.txt"},
        {"alert": "Server Leaks Version Information via 'Server' HTTP Response Header", "risk": "High", "url": "http://example.com/sitemap.xml"},
        {"alert": "Server Leaks Version Information via 'Server' HTTP Response Header", "risk": "High", "url": "http://example.com/"},
        {"alert": "X-Content-Type-Options Header Missing", "risk": "Low", "url": "http://example.com/"},
    ]
    generate_report("test_report.pdf", test_findings)
