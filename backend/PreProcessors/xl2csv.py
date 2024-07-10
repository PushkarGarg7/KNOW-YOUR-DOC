import pandas as pd
import os

def excel_to_csv(excel_path, csv_path):
    excel_data = pd.read_excel(excel_path)
    excel_data.to_csv(csv_path, index=False)
    return csv_path
