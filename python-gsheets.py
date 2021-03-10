import gspread

data = 123
gc = gspread.service_account()
sheet = gc.open("test-sheet")
sheet.values_update('Sheet1!A1',params={'valueInputOption': 'RAW'},body={'values': data})
