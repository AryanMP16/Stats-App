from openpyxl import load_workbook
import xlwings as xw

############ READ ROI:
wbxl=xw.Book("C:/Users/aryan/Documents/GitHub/Stats-App/EXCEL.xlsx")
ball = wbxl.sheets['Value'].range('L46').value
print(ball)