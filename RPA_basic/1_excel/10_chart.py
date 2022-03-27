from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

from openpyxl.chart import BarChart, Reference, LineChart
#B2:C11までのデータをチャートで表す
# bar_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3 )
# bar_chart = BarChart() #Chartの種類を設定(Bar, Line, Pie, ...)
# bar_chart.add_data(bar_value) #Chartのデータ追加
# ws.add_chart(bar_chart, "E1") #chartを入れる位置・定義

#B1:B11までのデータ
line_value = Reference(ws, min_row=1, max_row=11, min_col=2, max_col=3 )
line_chart = LineChart()
line_chart.add_data(line_value, titles_from_data=True)
line_chart.title = "成績" #タイトル
line_chart.style = 10 #すでに決まったスタイル適用
line_chart.y_axis.title = "点数" #yのタイトル
line_chart.x_axis.title = "番号" #ｘのタイトル
ws.add_chart(line_chart, "E1")


wb.save("sample_chart.xlsx")