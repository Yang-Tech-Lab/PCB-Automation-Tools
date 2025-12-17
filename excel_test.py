import openpyxl
wb=openpyxl.load_workbook("Project_Money.xlsx")
sheet=wb.active
print(sheet['A1'].value)
print(sheet['B2'].value)