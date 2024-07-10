


import os
from backend.PreProcessors.xl2csv import excel_to_csv
from backend.models.csv_handle import handle_csv_query

def process_excel_for_qa(excel_file, query, session_id):
    # Convert Excel to CSV
    csv_path = os.path.join("database/files", f"{session_id}.csv")
    excel_to_csv(excel_file, csv_path)

    # Send CSV and query to the handler
    response_text = handle_csv_query(csv_path, query)
    
    # Ensure the CSV file is removed
    if os.path.exists(csv_path):
        os.remove(csv_path)

    # Ensure the Excel file is removed
    if os.path.exists(excel_file):
        os.remove(excel_file)

    return response_text

