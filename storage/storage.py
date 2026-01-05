"""
storage.py

This module handles all the storage and history tracking for the E-commerce Product Intelligence Scraper.

It contains functions to:
1. Save the current list of scraped products into an Excel file.
2. Append new product snapshots to a historical record with timestamps.

We use pandas for tabular data management, openpyxl for Excel writing, pathlib for safe path handling,
and timezone-aware datetime objects for accurate timestamping.

This design ensures:
- Safe creation of directories and files.
- Consistent, professional, and future-proof handling of time data.
- Separation of current snapshot vs. historical record.
"""

# Import pandas for creating and manipulating tabular data
import pandas as pd

# Import Path from pathlib for object-oriented, cross-platform path management
from pathlib import Path

# Import datetime and timezone for timestamping history in a timezone-aware manner
from datetime import datetime, timezone


def save_current_products(products, file_path):
    """
    Save the current product list to an Excel file.

    Parameters:
    - products: list of dictionaries
        This comes directly from parser.py after extracting product data from the Target page.
        Each dictionary contains keys like 'title', 'price', 'comparison_price', 'brand', 'variations'.
    - file_path: str or Path
        The file path where the Excel file should be saved (e.g., "data/current_products.xlsx").

    This function ensures the data folder exists, converts products to a DataFrame, and saves it
    in Excel format using openpyxl.
    """

    # Convert the list of product dictionaries into a pandas DataFrame
    df = pd.DataFrame(products)
    # Variable 'df' is chosen because it's standard in pandas for "DataFrame" objects

    # Convert the string file path into a Path object for safer handling
    path = Path(file_path)
    # Variable 'path' chosen to represent the filesystem path of the file

    # Ensure the parent directory exists; if not, create it
    path.parent.mkdir(parents=True, exist_ok=True)
    # parents=True ensures all missing directories in the path are created
    # exist_ok=True prevents error if the directory already exists

    # Save the DataFrame to Excel
    df.to_excel(file_path, index=False, engine="openpyxl")
    # index=False prevents pandas from writing a default integer index column
    # engine="openpyxl" is required for writing .xlsx files


def append_price_history(products, history_file_path):
    """
    Append a new snapshot of products to a historical record with timestamps.

    Parameters:
    - products: list of dictionaries
        Same as in save_current_products, comes from parser.py.
    - history_file_path: str or Path
        File path to the historical Excel record (e.g., "data/history.xlsx").

    Function behavior:
    - Converts products into a DataFrame.
    - Adds a 'timestamp' column with timezone-aware UTC datetime.
    - If the history file exists, append the new snapshot to existing records.
    - If the file doesn't exist, create a new history file.
    - Saves the combined DataFrame back to Excel.
    """

    # Convert the list of product dictionaries into a DataFrame
    df_new = pd.DataFrame(products)
    # 'df_new' is a new snapshot of current products, separate from historical data

    # Add a timestamp column to record the exact UTC time of scraping
    df_new["timestamp"] = datetime.now(timezone.utc)
    # datetime.now(timezone.utc) ensures a timezone-aware timestamp
    # Column name 'timestamp' is self-explanatory for historical tracking

    # Convert the history file path to a Path object
    path = Path(history_file_path)
    # 'path' represents where the historical record will be saved

    # Ensure the parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)
    # Automatically creates the 'data/' folder if it doesn't exist

    # Check if the history file already exists
    if path.exists():
        # Read the existing historical Excel file into a DataFrame
        df_existing = pd.read_excel(path, engine="openpyxl")
        # df_existing contains all previously saved snapshots

        # Concatenate the old history with the new snapshot
        df_final = pd.concat([df_existing, df_new], ignore_index=True)
        # ignore_index=True resets the row index so there are no duplicate indices

    else:
        # If no history exists, the new snapshot becomes the first historical record
        df_final = df_new

    # Save the combined DataFrame back to Excel
    df_final.to_excel(path, index=False, engine="openpyxl")
    # index=False prevents writing a default integer index
    # engine="openpyxl" required for .xlsx
