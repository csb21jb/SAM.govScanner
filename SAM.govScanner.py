import subprocess
import sys
from datetime import datetime, timedelta
import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load email credentials
with open('email_creds.json', 'r') as creds_file:
    creds = json.load(creds_file)
    from_email = creds['email']
    from_password = creds['password']

# List of keywords, with "Compliance" removed
keywords = [
    "Cybersecurity", "Information Technology", "IT Security", "Network Security", "Data Protection",
    "Cloud Security", "Risk Management", "Intrusion Detection", "Security Operations Center (SOC)",
    "Vulnerability Assessment", "Penetration Testing", "Incident Response", "Security Audit",
    "Encryption", "Firewall", "Cyber Defense", "Threat Intelligence",
    "Identity and Access Management (IAM)", "Security Information and Event Management (SIEM)",
    "Cloud", "Ethernet"
]

# Base URL
base_url = "https://api.sam.gov/opportunities/v2/search"
api_key = "PUT_YOUR_API_KEY_FROM_SAM.GOV"

# Get current date and date 90 days ago, adjust as needed
current_date = datetime.now()
posted_to = current_date.strftime("%m/%d/%Y")
posted_from = (current_date - timedelta(days=90)).strftime("%m/%d/%Y")

# Get current date and time for filename in DTG format
current_dtg = current_date.strftime("%d%H%MZ%b%Y")

# Initialize a single human-readable file
readable_filename = f"{current_dtg}_all_keywords_readable.txt"

# Set to track unique notice IDs
unique_notice_ids = set()

# Initialize email body content
email_body_content = ""

# Iterate through each keyword and make a GET request
for keyword in keywords:
    params = {
        "limit": 10,
        "api_key": api_key,
        "postedFrom": posted_from,
        "postedTo": posted_to,
        "title": keyword
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Append JSON data to the email body content
        email_body_content += f"Keyword: {keyword}\n"
        email_body_content += "=" * 80 + "\n"
        for opportunity in data.get('opportunitiesData', []):
            if opportunity['noticeId'] not in unique_notice_ids:
                unique_notice_ids.add(opportunity['noticeId'])
                email_body_content += f"Title: {opportunity['title']}\n"
                email_body_content += f"Notice ID: {opportunity['noticeId']}\n"
                email_body_content += f"Posted Date: {opportunity['postedDate']}\n"
                email_body_content += f"Solicitation Number: {opportunity.get('solicitationNumber', 'N/A')}\n"
                email_body_content += f"Description: {opportunity['description']}\n"
                email_body_content += f"Response Deadline: {opportunity.get('responseDeadLine', 'N/A')}\n"
                email_body_content += f"NAICS Code: {opportunity.get('naicsCode', 'N/A')}\n"
                point_of_contact = opportunity.get('pointOfContact', [])
                if point_of_contact:
                    email_body_content += f"Point of Contact: {', '.join([contact['fullName'] for contact in point_of_contact if contact['fullName']])}\n"
                else:
                    email_body_content += "Point of Contact: N/A\n"
                email_body_content += f"Link: {opportunity['uiLink']}\n"
                email_body_content += "-" * 80 + "\n"
        email_body_content += "\n\n"
    else:
        print(f"Failed to retrieve data for keyword: {keyword}. Status Code: {response.status_code}")

# Function to send email
def send_email(from_email, from_password, to_email, subject, body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Create SMTP session for sending the mail from YAHOO. Use GMAIL settings as required
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)  # Use Yahoo's SMTP server and port
        server.starttls()

        # Login to the server
        server.login(from_email, from_password)

        # Convert the Multipart msg into a string
        text = msg.as_string()

        # Send the email
        server.sendmail(from_email, to_email, text)

        # Close the server connection
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Send the email
send_email(
    from_email=from_email,
    from_password=from_password,
    to_email='ADD_AN_EMAIL_ADDRESS',
    subject='SAM.gov Opportunities Report',
    body=email_body_content
)
