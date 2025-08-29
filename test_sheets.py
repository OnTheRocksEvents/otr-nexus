import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Carga credenciales
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
gc = gspread.authorize(creds)

# IDs a probar
IDS = {
    "unificado": "1_WPcxC227gmZminK5AGOJ3vrK7Zjcl4xNb3GxGWxx-0",
    "albaranes": "1zB-snLBoO_lkiK0mq-MYyDUwxm5-S8VM"
}

for name, sheet_id in IDS.items():
    try:
        ss = gc.open_by_key(sheet_id)
        titles = [w.title for w in ss.worksheets()]
        print(f"[OK] {name} → pestañas: {titles}")
    except Exception as e:
        print(f"[ERROR] {name} ({sheet_id}): {e}")
