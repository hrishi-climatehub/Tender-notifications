import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Load Google credentials from environment variable
creds_json = os.environ.get("GOOGLE_CREDS")
creds_dict = json.loads(creds_json)

# Authorize client
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
client = gspread.authorize(creds)

# Open the Google Sheet by URL or name
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1PtyjgDfe7VYmtpW-UlZM0U84Y6iE9GwR3W3FSSsvj0g/edit?usp=sharing").Tenders  # or .worksheet("Sheet1")

# Example: append a row of tender data
sheet.append_row(["Date", "Tender Title", "Link", "Budget"])
print("Data appended successfully.")

