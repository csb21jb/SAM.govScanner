import requests
import json
import smtplib
import re
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import openai  # type: ignore # OpenAI integration

# === CONFIGURATION ===
EMAIL_CREDENTIALS_FILE = "/root/PATH_TO_FOLDER/SAM.govScanner/email_creds.json" # change as required
DATA_FILE = "/root/projects/SAM.govScanner/sam_gov_data.json" # change as required
SAM_GOV_API_KEY = "PUT YOUR SAM.GOV API HERE"
OPENAI_API_KEY = "PUT YOUR OPEN API KEY HERE"  # Replace with actual OpenAI API key

# Load email credentials
with open(EMAIL_CREDENTIALS_FILE, 'r') as creds_file:
    creds = json.load(creds_file)
    FROM_EMAIL = creds['email']
    FROM_PASSWORD = creds['password']

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Define NAICS Codes to filter opportunities
NAICS_CODES = [
    "541512", "541519", "541330", "541511", "541715", "541690", # Edit NAICS CODES
    "541310", "561621", "541611", "517110", "541513", "541410", "561990" # Edit NAICS CODES
]

# Get current date and set date range for fetching data
current_date = datetime.now()
posted_from = (current_date - timedelta(days=5)).strftime("%m/%d/%Y")
posted_to = current_date.strftime("%m/%d/%Y")

# Fetch data from SAM.gov API
print("📡 Fetching data from SAM.gov...")

params = {
    "limit": 1000,  # Maximize results
    "api_key": SAM_GOV_API_KEY,
    "postedFrom": posted_from,
    "postedTo": posted_to
}

response = requests.get("https://api.sam.gov/opportunities/v2/search", params=params)

if response.status_code == 200:
    data = response.json()
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("✅ Data fetched and saved successfully.")
else:
    print(f"❌ Error fetching data: {response.status_code} - {response.text}")
    exit()

# Load the JSON data
with open(DATA_FILE, "r") as f:
    sam_gov_data = json.load(f)

# Filter opportunities based on NAICS codes
opportunities = [
    opp for opp in sam_gov_data.get('opportunitiesData', [])
    if opp.get("naicsCode", "N/A") in NAICS_CODES
]

# Check if we have valid opportunities
if not opportunities:
    print("❌ No contract opportunities matching specified NAICS codes.")
    exit()

# AI Analysis for the top 10 opportunities
print("🤖 Running AI analysis on top opportunities...")

for opp in opportunities[:10]:
    ai_prompt = f"""
    Evaluate this government contract for Taupe Solutions and CyberStorm Defense:

    <b>Title:</b> {opp.get('title', 'N/A')}<br>
    <b>NAICS Code:</b> {opp.get('naicsCode', 'N/A')}<br>
    <b>Posted Date:</b> {opp.get('postedDate', 'N/A')}<br>
    <b>Response Deadline:</b> {opp.get('responseDeadLine', 'N/A')}<br>

    Provide a succinct analysis of how well this contract aligns with their cybersecurity and
    government contracting expertise. Include a rating out of 10 based on the alignment with their capabilities.

    AI Prompt for Proposal Evaluation:

Taupe Solutions and CyberStorm Defense are leading cybersecurity firms specializing in securing government
agencies, the Department of Defense (DoD), and private sector clients against cyber threats. Taupe Solutions,
 founded in 2021, provides vulnerability assessments, penetration testing, and physical security evaluations
 to identify cyber and physical gaps. With expertise in special operations, cyber warfare, and sensitive activities,
 they deliver consultation, network hardening, and employee-focused security solutions. Their services include
 red teaming, threat assessments, compliance readiness (CMMC, NIST 800-171, FedRAMP, FISMA), and securing critical assets
 against evolving digital threats.

CyberStorm Defense, founded in 2015, brings deep expertise in DevSecOps, application security, cloud security, identity
and access management (IAM), and industrial control system (ICS) protection. They integrate security into software development,
CI/CD pipelines, and supply chain security while ensuring regulatory compliance, risk management, and proactive cyber threat monitoring.
Their team specializes in penetration testing, digital forensics, disaster recovery, business continuity planning, and 24/7 security operations.

Task: Analyze the provided government contract opportunity and determine alignment with Taupe Solutions and CyberStorm Defense’s expertise.
Assign a rating (X/10) based on how well the opportunity fits their capabilities. Consider effort, compliance requirements, competition, and potential risks (funding instability, scope creep, regulatory
 hurdles, etc.). Provide a clear recommendation, —either "Recommend" or "Don't Recommend", with reasoning. Keep the response very concise with no more
 than 100 words.

Final Output Format:
Recommendation:[Recommend / Do Not Recommend]
Rating: [X/10]
Analysis: [Concise strategic response]
Proposal Effort Estimate: [Small/Medium/Large]
Competitive Insights: [Key risks, opportunities, differentiators, etc.]
    """

    print(f"📨 Sending AI request for: {opp.get('title', 'N/A')}")

    try:
        ai_response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a government contracting expert."}, # Edit your role so AI has context who its trying to be
                {"role": "user", "content": ai_prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )

        ai_content = ai_response.choices[0].message.content.strip()
        print(f"✅ AI Response for {opp.get('title', 'N/A')}:\n{ai_content}")

        # Remove all unwanted asterisks (*) commonly used in markdown
        ai_content = re.sub(r"[*]", "", ai_content)

        # Updated regex to match "Rating: X/10" or variations, excluding those with an asterisk
        rating_match = re.search(r"Rating:\s*(\d+(\.\d+)?)/10(?!\*)", ai_content)

        if rating_match:
            opp["ai_rating"] = rating_match.group(1)  # Extract rating without "/10"
            print(f"✔️ Extracted Rating: {opp['ai_rating']}")
        else:
            print("⚠️ Rating not found in AI response. Assigning default rating: <b>5.0</b>")
            opp["ai_rating"] = "5.0"  # Assign default rating if missing

        # Ensure headers are bold in HTML
        ai_content = re.sub(r"(Recommendation:)", r"<b>\1</b>", ai_content, flags=re.IGNORECASE)
        ai_content = re.sub(r"(Rating:)", r"<b>\1</b>", ai_content, flags=re.IGNORECASE)
        ai_content = re.sub(r"(Analysis:)", r"<b>\1</b>", ai_content, flags=re.IGNORECASE)
        ai_content = re.sub(r"(Proposal Effort Estimate:)", r"<b>\1</b>", ai_content, flags=re.IGNORECASE)
        ai_content = re.sub(r"(Competitive Insights:)", r"<b>\1</b>", ai_content, flags=re.IGNORECASE)

        opp["ai_analysis"] = ai_content

    except Exception as e:
        print(f"❌ AI request failed for {opp.get('title', 'N/A')}: {e}")
        opp["ai_rating"] = "<b>5.0</b>"  # Default rating in HTML bold
        opp["ai_analysis"] = f"AI request failed: {e}"

# Remove contracts where AI Rating & Analysis are "N/A"
filtered_opportunities = [
    opp for opp in opportunities if opp.get("ai_rating") != "N/A"
]

if not filtered_opportunities:
    print("❌ No valid opportunities after AI filtering. Email will not be sent.")
    exit()

# Format email with filtered results
print("📧 Preparing email...")

email_body = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; color: #333; }
        .container { width: 100%; max-width: 800px; margin: auto; padding: 10px; }
        h2 { color: #0056b3; text-align: center; }
        .notice-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        .notice-table th, .notice-table td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        .notice-table th { background-color: #0056b3; color: white; }
        .notice-table tr:nth-child(even) { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <div class="container">
        <h2>SAM.gov Opportunities Report</h2>
        <p>Top filtered contract opportunities for Taupe Solutions and CyberStorm Defense.</p>
        <table class="notice-table">
            <tr>
                <th>Rank</th>
                <th>Title</th>
                <th>NAICS Code</th>
                <th>Response Deadline</th>
                <th>AI Rating</th>
                <th>AI Insight</th>
                <th>Details</th>
            </tr>
"""

for i, opp in enumerate(filtered_opportunities, start=1):
    email_body += f"""
        <tr>
            <td>{i}</td>
            <td>{opp.get('title', 'N/A')}</td>
            <td>{opp.get('naicsCode', 'N/A')}</td>
            <td>{opp.get('responseDeadLine', 'N/A')}</td>
            <td><b>{opp.get('ai_rating', 'N/A')}</b></td>
            <td>{opp.get('ai_analysis', 'N/A')}</td>
            <td><a href="{opp.get('uiLink', '#')}" target="_blank">View</a></td>
        </tr>
    """

email_body += "</table></div></body></html>"

# Send email
# Function to send email
def send_email(from_email, from_password, to_emails, subject, body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = ", ".join(to_emails)
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'html'))  # Set content type to HTML

        # Create SMTP session for sending the mail
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)  # Use Yahoo's SMTP server and port
        server.starttls()

        # Login to the server
        server.login(from_email, from_password)

        # Convert the Multipart msg into a string
        text = msg.as_string()

        # Send the email to all recipients
        server.sendmail(from_email, to_emails, text)

        # Close the server connection
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Send the email to multiple recipients
send_email(
    from_email=FROM_EMAIL,
    from_password=FROM_PASSWORD,
    to_emails=['PUT ANOTHER EMAIL ADDRESS HERE', 'PUT YOUR EMAIL ADDRESS HERE'],  # Add more emails here
    subject='SAM.gov Opportunities Report - NAICS & Keywords',
    body=email_body
)

print("✅ Script execution completed!")
