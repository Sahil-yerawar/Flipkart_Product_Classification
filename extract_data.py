import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/ysahil/Academics/Research/IIITD/product_classify/Extract Product data-d0c5f23f91e4.json',scope)
client = gspread.authorize(creds)

sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1OZJ9TQQGfo_26LanqmmyBatuWOQfUMUuV7T9-WDeLFA/edit#gid=1396401268')
sheet_ist = sheet.get_worksheet(0)

records_data = sheet_ist.get_all_records()
records_df = pd.DataFrame.from_dict(records_data)
records_df.to_pickle("/home/ysahil/Academics/Research/IIITD/product_classify/record_dump.pkl")
