import pandas as pd
import os

def save_current_products(products,file_path):
    df = pd.DataFrame(products)
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    df.to_excel(file_path,index=False,engine="openpyxl")
    