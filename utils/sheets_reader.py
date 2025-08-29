import gspread
from oauth2client.service_account import ServiceAccountCredentials

def leer_todas_las_hojas(sheet_id):
    """
    Lee todas las pestañas de una hoja de cálculo de Google Sheets
    y devuelve un diccionario con los datos por nombre de pestaña.
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open_by_key(sheet_id)
    hojas = spreadsheet.worksheets()

    datos_por_hoja = {}
    for hoja in hojas:
        nombre = hoja.title
        try:
            datos = hoja.get_all_records()
            datos_por_hoja[nombre] = datos
        except Exception as e:
            print(f"⚠️ Error leyendo la hoja '{nombre}': {e}")
            datos_por_hoja[nombre] = []

    return datos_por_hoja

