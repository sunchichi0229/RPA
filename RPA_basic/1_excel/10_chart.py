from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

from openpyxl.chart import BarChart, Reference
#B2:C11までのデータをチャートで表す
bar_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3 )
bar_chart = BarChart()