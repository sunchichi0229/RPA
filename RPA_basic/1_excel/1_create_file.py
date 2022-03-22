from openpyxl import Workbook
wb = Workbook() #新しいワークブック
ws = wb.active #現在活性化しているsheetを持ってくる
ws.title = "Sunsheet" #sheetの名変更
wb.save("sample.xlsx")
wb.close()