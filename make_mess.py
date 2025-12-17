import openpyxl

# 1. 创建一个新的工作簿
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Raw_Orders" # 给表起个名

# 2. 写入表头 (Header)
sheet.append(["OrderID", "Product Name", "Price", "Customer Email"])

# 3. 写入“脏数据” (模拟真实世界的混乱)
data = [
    [1001, "  Iphone 15 Case ", "$15.99", " John@Gmail.com "], # 坑：空格、美元符号、大写邮箱
    [1002, "samsung galaxy s24", "999", "SARAH@HOTMAIL.COM"],    # 坑：全小写产品、全大写邮箱
    [1003, "Xiaomi 14 Pro", "N/A", " mike.doe@yahoo.com"],       # 坑：价格是 N/A (甚至不是数字)
    [1004, "  USB-C Cable  ", "$5.00", "test_user@abc.com"],     # 坑：前后超多空格
    [1005, "Airpods Pro 2", "249.00", "Admin@Store.com"]         # 只有这一条是干净的
]

# 把脏数据一行行写进去
for row in data:
    sheet.append(row)

# 4. 保存这个烂摊子
wb.save("Fiverr_Messy_Data.xlsx")
print("✅ 任务完成：脏乱差的 Excel 文件已生成！")