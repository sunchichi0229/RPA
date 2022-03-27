from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.delete_rows(8) #8番目にある７番目の学生Dataを削除
ws.delete_rows(8, 3) #8番目から３行の学生Dataを削除

wb.save("sample_delete_row.xlsx")
