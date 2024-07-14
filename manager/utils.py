import gspread
from google.oauth2.service_account import Credentials
from django.conf import settings
import json
from decouple import config

sheet_id = config("SHEET_ID")
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

def get_google_client():
    """
    Returns a Google Sheets client
    """
    creds = Credentials.from_service_account_info(json.loads(settings.CREDS_JSON_STR), scopes=scopes)
    client = gspread.authorize(creds)
    return client

def create_google_sheet(sheet_name):
    """
    Creates a new Google Sheet and returns the URL
    """
    client = get_google_client()
    workbook = client.open_by_key(sheet_id)
    new_sheet = workbook.add_worksheet(title=sheet_name,rows=100,cols=20)
    
    header_row = ['Time', 'Food', 'Quantity']
    new_sheet.insert_row(header_row, index=1)
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit#gid={new_sheet.id}"

def delete_google_sheet(sheet_name):
    """
    Deletes a Google Sheet based on its name
    """
    client = get_google_client()
    workbook = client.open_by_key(sheet_id)
    sheets = workbook.worksheets()

    for sheet in sheets:
        if sheet.title == sheet_name:
            workbook.del_worksheet(sheet)
            break

def get_patient_sheet(sheet_name):
    """
    Retrieves a Google Sheet object based on its name
    """
    client = get_google_client()
    workbook = client.open_by_key(sheet_id)
    sheets = workbook.worksheets()

    for sheet in sheets:
        if sheet.title == sheet_name:
            return sheet
        
def fetch_excel_data(sheet_name, start_line, end_line):
    sheet = get_patient_sheet(sheet_name)

    # Fetching data from specific columns and rows
    data = sheet.get(f'A{start_line}:C{end_line}') 
    
    # Extracting data into separate arrays for each column
    Food = [row[0] for row in data]
    Time = [row[1] for row in data]
    Quantity = [row[2] for row in data]
    
    return Food, Time, Quantity
