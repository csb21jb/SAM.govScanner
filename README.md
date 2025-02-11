![image](https://github.com/csb21jb/SAM.govScanner/assets/94072917/7186d534-d39b-446e-8396-7727747c8054)

# SAM.govScanner

## Overview


**SAM.govScanner** is a Python-based automation tool that fetches government contract opportunities from SAM.gov using NAICS codes and AI-driven analysis. Designed for businesses in cybersecurity, IT, and government contracting, this tool streamlines opportunity identification, ranks contracts based on relevance, and delivers strategic insights via email.

By integrating **OpenAI’s AI capabilities**, SAM.govScanner goes beyond basic contract searches—it evaluates each opportunity, assigns a relevance rating, and provides **customized recommendations** based on your company’s expertise. This ensures **higher-quality leads, strategic bidding decisions, and increased efficiency** in government contracting.



## **Key Features**

- 🚀 **Automated Opportunity Retrieval** – Fetches the latest SAM.gov opportunities based on **NAICS codes**.
- 🤖 **AI-Powered Opportunity Analysis** – Assesses contract fit for your company, assigns a **relevance rating (1-10)**, and provides concise recommendations.
- 📊 **Custom Business Insights** – Identifies effort estimates, compliance risks, competition levels, and proposal feasibility.
- 📩 **Email Notifications** – Delivers a structured report with AI-ranked opportunities to your inbox.
- 🔄 **Seamless Scheduling** – Works with cron jobs for daily, weekly, or monthly execution.

---

## **Installation**

### **1. Clone the Repository**
```sh
git clone https://github.com/csb21jb/SAM.govScanner.git
cd SAM.govScanner
```

### **2. Set Up Email Credentials**
Edit the file named `email_creds.json` in the project directory and add:
```json
{
    "email": "youremail@example.com",
    "password": "your_app_password"
}
```
- **Yahoo/Gmail Users:** Generate an app-specific password in your account’s security settings - https://www.youtube.com/watch?v=h_LrGeNV36g&t=7s.

### **3. Obtain SAM.gov API Key**
- You **must** have an active SAM.gov account.
- Log in to [SAM.gov API](https://open.gsa.gov/api/get-opportunities-public-api/) and generate an API key.
- Insert it in `SAM.govScanner.py`.

### **4. Configure AI Integration**
- Set up an **OpenAI API Key** for AI-driven contract analysis.
- Insert it in `SAM.govScanner.py`.

### **5. Edit The AI Prompt**
- Ask another AI platform to create a prompt for you and replace.



## **Usage**

### **1. Automate with a Cron Job**
Schedule the script to run daily, weekly, or monthly:
```sh
crontab -e
```
Example (runs daily at 8 AM): NOte - you may have to create a virtual environment for python.
```sh
0 8 * * * source /path/to/SAM.govScanner/venv/bin/activate && python3 /path/to/SAM.govScanner.py
```

### **2. Run Manually**
```sh
python3 SAM.govScanner.py
```

### **3. Output & Email Reports**
- Fetches SAM.gov contracts within the last **5 days**.
- Filters **top opportunities** based on **NAICS codes**.
- Uses **AI to rank contracts** and provide **custom recommendations**.
- Emails structured contract insights, including:
  - **Title, NAICS Code, Deadline**
  - **AI Rating (1-10)**
  - **Proposal Effort Estimate**
  - **Competitive Insights**
  - **Direct SAM.gov Links**


## **Example AI-Generated Analysis**
![image](https://github.com/user-attachments/assets/84a07519-9f74-49ba-9f43-965c60584465)




## **Business Value**

### 🔹 **AI-Powered Decision Support**
- Eliminates **manual contract filtering**—only **high-potential** opportunities are analyzed.
- **Prepares businesses for strategic bidding** by identifying risks, effort estimates, and competitive advantages.

### 🔹 **Time-Saving Automation**
- **No need to search SAM.gov manually**—AI processes contracts and delivers recommendations to your inbox.
- Enables **proactive engagement** with high-relevance contracts.

### 🔹 **Competitive Edge**
- **Ranks contracts by AI-driven relevance**, ensuring focus on **high-value** opportunities.
- Helps businesses **respond faster** and secure **more contracts**.


## **Contributions & Feedback**
We welcome contributions, feedback, and feature requests. Open a GitHub issue or submit a pull request to help improve **SAM.govScanner**.



