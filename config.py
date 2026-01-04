import os 
from dotenv import load_dotenv

load_dotenv()

SEARCH_URL = "https://www.target.com/s?searchTerm=laptop"
CHECK_INTERVAL_SECONDS = 1800
PRODUCT_LIST_FILE = "data/product_list.xlsx"
PRODUCT_DETAILS_FILE = "data/current_products.xlsx"
HISTORY_FILE = "data/history.xlsx"
EMAIL_ALERTS = True
SMTP_SERVER = os.environ.get("SMTP_SERVER","smtp.gmail.com")
SMTP_PORT = os.environ.get("SMTP_PORT",587)
EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER")