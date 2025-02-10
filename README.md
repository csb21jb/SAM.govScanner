![image](https://github.com/csb21jb/SAM.govScanner/assets/94072917/7186d534-d39b-446e-8396-7727747c8054)

# SAM.govScanner

## Overview

This Python script fetches contract opportunities from SAM.gov, focusing on specific keywords related to cybersecurity and IT security. It compiles the results into a single email, providing business professionals with an efficient and effective way to stay updated on relevant contract opportunities.

## Features




## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/csb21jb/SAM.govScanner.git
    cd SAM.govScanner
    ```

2. **Set up email credentials**:
    - Edit the file named `email_creds.json` in the project directory with the following content:
    ```json
    {
        "email": "youremail@example.com",
        "password": "your_app_password"
    }
    ```
    - For Yahoo accounts, generate an app-specific password on yahoo webpage under the security section. This will ensure that your real password isnt used and if compromised, you can just remove this access from yahoo.
    - For Gmail accounts, conduct the same thing in the security section which will generate the password for the application.

3. **Obtain SAM.gov API key**:
    - You MUST have an active SAM.gov account to make this work
    - Go here for further info on SAM.gov API keys - https://open.gsa.gov/api/get-opportunities-public-api/
    - Log into your SAM.gov account to get your API key and place it in the SAM.govScanner.py file

 4. **Edit Python script**
    - Add the email address of the account you wish to recieve mail on.

      
## Usage

1. Use in a cronjob to run everyday, weekly, or monthly.
   
3. **Run the script manually**: 
    ```sh
    python3 SAM.govScanner.py
    ```

4. **Output**:
    - The script will fetch contract opportunities from SAM.gov for the specified keywords.
    - It compiles the results into a single email body, which is then sent to the specified email address above.

## Example Output

The email will contain sections for each keyword, listing the contract opportunities found. Each section will include details such as the title, notice ID, posted date, solicitation number, description, response deadline, NAICS code, point of contact, and a link to the opportunity.

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


