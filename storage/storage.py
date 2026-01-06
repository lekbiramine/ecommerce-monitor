import pandas as pd
from pathlib import Path
from datetime import datetime, timezone

def save_current_products(products, file_path):
    """Save a list of products to an Excel file, creating parent directories if they don't exist.
    Args: products (list): List of product dictionaries to save. file_path (str): Path where the Excel file will be saved."""

    df = pd.DataFrame(products)
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(file_path, index=False, engine="openpyxl")


def append_price_history(products, history_file_path):
    """
    Appends product price data to an Excel history file with a UTC timestamp.
    Creates the file and parent directories if they don't exist, or concatenates with existing data.
    Returns nothing; writes the updated data directly to the Excel file specified by history_file_path.
    """
    
    df_new = pd.DataFrame(products)
    df_new["timestamp"] = datetime.now(timezone.utc).replace(tzinfo=None)
    path = Path(history_file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        df_existing = pd.read_excel(path, engine="openpyxl")
        df_final = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_final = df_new

    df_final.to_excel(path, index=False, engine="openpyxl")