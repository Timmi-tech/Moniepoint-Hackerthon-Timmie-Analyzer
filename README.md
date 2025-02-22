Moniepoint Hackerthon - Timmie Analyzer

📌 Project Overview

Timmie Analyzer is a Python-based data analytics tool designed to process and extract valuable insights from transaction records. It was developed as part of the Moniepoint Hackathon challenge.

🚀 Features

Parses transaction files from multiple test case folders.

Computes key sales analytics:

Highest Sales Volume Day (Most Transactions)

Highest Sales Value Day (Most Revenue)

Most Sold Product (By Quantity)

Top Sales Staff per Month

Busiest Hour of the Day (Most Transactions)

Generates a detailed sales report.

Web Interface built using Django for easy file uploads and visualization.

🏗️ Problem-Solving Approach

Understanding the Problem: Extracting key business insights from multiple transaction .txt files.

Data Collection: Reading multiple .txt files inside a folder and extracting relevant data.

Data Processing: Parsing transaction details (e.g., sales staff ID, transaction time, products sold, etc.).

Data Analysis: Using dictionaries to compute:

Sales volume per day

Sales value per day

Most sold product

Top sales staff per month

Busiest transaction hour

Compiling Results: Structuring findings for output.

Output & Reporting: Saving results in a structured report (sales_report.txt).

Enhancing Accessibility: Building a Django-based UI for file uploads and real-time analysis.

Adding Features: Supporting .zip file uploads (since Django does not accept folders) and improving the UI using HTML, CSS, and Bootstrap.

📂 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Timmi-tech/Moniepoint-Hackerthon-Timmie-Analyzer.git

cd Moniepoint-Hackerthon-Timmie-Analyzer


3️⃣ Run the Analyzer

python src/Analyze_single_sales.py

4️⃣ Run the Web Interface (Django App)

cd web_app
python manage.py runserver

📊 Sample Output

📌 Highest Sales Volume in a Day: 2025-02-15 (342 transactions)
📌 Highest Sales Value in a Day: 2025-02-18 ($12,430.50)
📌 Most Sold Product ID: 101 (543 units sold)
📊 Top Sales Staff for Each Month:
   - 2025-02: Staff ID 008 ($3,560.75)
⏳ Busiest Hour of the Day: 14:00 (87 transactions)

🛠️ Technologies Used

Python for data processing

Django for web-based file upload & analysis

OS Module for file handling

Dictionary & List Comprehension for efficient data aggregation

HTML, CSS, Bootstrap for frontend design

📷 Screenshots
![screencapture-127-0-0-1-8000-analytics-sales-2025-02-22-14_59_58](https://github.com/user-attachments/assets/0480e373-165f-4dc5-8413-0b3eff48147f)



![screencapture-127-0-0-1-8000-analytics-sales-2025-02-22-15_01_02](https://github.com/user-attachments/assets/3fb950e0-9ecf-4419-af7f-e9c5d856ac16)
![screencapture-127-0-0-1-8000-analytics-sales-2025-02-22-15_02_57](https://github.com/user-attachments/assets/8a9feaec-4b34-458b-ac6c-4366225128a5)

![screencapture-127-0-0-1-8000-analytics-sales-2025-02-22-15_03_57](https://github.com/user-attachments/assets/46ed3071-31e5-4815-8042-83696f42e274)
![screencapture-127-0-0-1-8000-analytics-sales-2025-02-22-15_07_17](https://github.com/user-attachments/assets/742059d2-5420-482b-8037-e033a308b468)


✨ Made with passion for Moniepoint Hackerthon ✨

