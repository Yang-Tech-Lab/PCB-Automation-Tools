import openpyxl
wb=openpyxl.load_workbook("Fiverr_Messy_Data.xlsx")
sheet=wb.active
print("正在启动清洗程序···")
for row in sheet.iter_rows(min_row=2):
    product_cell=row[1]
    price_cell=row[2]
    email_cell=row[3]
    if product_cell.value:
       clean_name=str(product_cell.value).strip().title()
       product_cell.value=clean_name
    if price_cell.value:
       text_price=str(price_cell.value).replace("$","")
    if text_price=="N/A":
       price_cell.value=0
    else:
       price_cell.value=float(text_price)

    if email_cell.value:
       clean_email=str(email_cell.value).strip().lower()
       email_cell.value=clean_email

wb.save("Fiverr_Cleaned_Result.xlsx")
print("恭喜！数据清洗完成，已保存为Fiverr_Cleaned_Result.xlsx")    

    
