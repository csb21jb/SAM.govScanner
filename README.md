![image](https://github.com/csb21jb/SAM.govScanner/assets/94072917/7186d534-d39b-446e-8396-7727747c8054)

# SAM.govScanner

## Overview

This Python script fetches contract opportunities from SAM.gov, focusing on specific keywords related to cybersecurity and IT security. It compiles the results into a single email, providing business professionals with an efficient and effective way to stay updated on relevant contract opportunities.

## Features

- **Fetches data**: Retrieves contract opportunities from SAM.gov based on a predefined list of keywords.
- **Date range**: Searches for opportunities posted within the last 90 days.
- **Email report**: Compiles the results into a single email body, making it easy to read and navigate.
- **Unique entries**: Ensures no duplicate entries in the report.
- **Timestamped filename**: Uses a Date-Time Group (DTG) format for generating filenames.

## Keywords

The script searches for opportunities using the following keywords (add or takeaway as needed):

- Cybersecurity
- Information Technology
- IT Security
- Network Security
- Data Protection
- Cloud Security
- Risk Management
- Intrusion Detection
- Security Operations Center (SOC)
- Vulnerability Assessment
- Penetration Testing
- Incident Response
- Security Audit
- Encryption
- Firewall
- Cyber Defense
- Threat Intelligence
- Identity and Access Management (IAM)
- Security Information and Event Management (SIEM)
- Cloud
- Ethernet

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/sam-gov-opportunities-report.git
    cd sam-gov-opportunities-report
    ```

2. **Set up email credentials**:
    - Edit the file named `email_creds.json` in the project directory with the following content:
    ```json
    {
        "email": "youremail@example.com",
        "password": "your_app_password"
    }
    ```
    - For Yahoo accounts, generate an app-specific password if necessary on yahoo webpage under the security section. This will ensure that your real password isnt used and if compromised, you can just remove this access from yahoo.
    - For Gmail accounts, conduct the same thing in the security section which will generate the password for the application.

## Usage

1. **Run the script**:
    ```sh
    python3 SAM.govScanner.py
    ```

2. **Output**:
    - The script will fetch contract opportunities from SAM.gov for the specified keywords.
    - It compiles the results into a single email body, which is then sent to the specified email address above.

## Example Output

The email will contain sections for each keyword, listing the contract opportunities found. Each section will include details such as the title, notice ID, posted date, solicitation number, description, response deadline, NAICS code, point of contact, and a link to the opportunity.

```
Keyword: Cyber Defense
================================================================================
Title: Joint Cyber Defense Collaborative Planning Support
Notice ID: a5996413e08848f684cae31844c894ed
Posted Date: 2024-05-06
Solicitation Number: PCCS-24-50005
Description: https://api.sam.gov/prod/opportunities/v1/noticedesc?noticeid=a5996413e08848f684cae31844c894ed
Response Deadline: 2024-05-17T17:00:00-04:00
NAICS Code: 541330
Point of Contact: Hannah Moussa, Shawn Curro
Link: https://sam.gov/opp/a5996413e08848f684cae31844c894ed/view
--------------------------------------------------------------------------------


Keyword: Threat Intelligence
================================================================================
Title: NATO Request for Information: Threat Intelligence Analytics Platform
Notice ID: 304d01de920e48f99cefd27f95b67e44
Posted Date: 2024-05-22
Solicitation Number: RFI-ACT-SACT-24-66
Description: https://api.sam.gov/prod/opportunities/v1/noticedesc?noticeid=304d01de920e48f99cefd27f95b67e44
Response Deadline: 2024-08-12T09:00:00-04:00
NAICS Code: 541519
Point of Contact: N/A
Link: https://sam.gov/opp/304d01de920e48f99cefd27f95b67e44/view
--------------------------------------------------------------------------------
```

## Business Application

### Efficiency

By automating the process of searching and compiling contract opportunities, this script saves significant time and effort for business professionals. Instead of manually searching SAM.gov for relevant contracts, the script provides a consolidated report, making it easy to stay informed.

### Effectiveness

The script ensures that all relevant opportunities are captured and presented in an organized manner. By focusing on specific keywords, businesses can quickly identify and act on the most pertinent contracts, enhancing their ability to secure new business.

### Real-Time Updates

With the script's ability to fetch opportunities posted within the last 90 days and send timely email reports, businesses can stay ahead of the competition by being among the first to respond to new opportunities.

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


