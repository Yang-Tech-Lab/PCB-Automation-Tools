import csv
import random

# 1. 定义一些基础素材
products = ["iPhone 13 Case", "Samsung S22 Ultra", "USB-C Cable 1m", "Anker Charger 20W", "iPad Screen Protector", "Sony Headphones", "Logitech Mouse", "Mechanical Keyboard"]
statuses = ["In Stock", "Out of Stock", "Low Stock", "", "Pre-order"]
currencies = ["$", "USD ", "", "￥"] # 用来制造价格列的混乱

def generate_messy_row():
    """生成一行混乱的数据"""
    # 随机选一个产品，并随机在前后加空格 (制造脏数据)
    name = random.choice(products)
    if random.random() > 0.5:
        name = " " + name + "  " 
    
    # 随机生成价格，有时候是纯数字，有时候带符号，有时候是空的
    base_price = random.randint(5, 100)
    if random.random() > 0.1:
        price = f"{random.choice(currencies)}{base_price}.{random.randint(0,99)}"
    else:
        price = "" # 10% 的概率价格缺失

    # 随机库存状态
    stock = random.choice(statuses)

    # 随机生成 SKU，有时候乱写，有时候缺失
    if random.random() > 0.9:
        sku = "" # 10% 概率缺失 SKU
    elif random.random() > 0.8:
        sku = "UNKNOWN-ITEM" # 乱码 SKU
    else:
        # 正常的 SKU 格式
        sku = f"{name.strip().split()[0].upper()}-{random.randint(100,999)}"

    return [name, price, stock, sku]

# 2. 主程序：生成 500 行数据
filename = "messy_amazon_data_large.csv"

print(f"🚀 正在制造混乱数据: {filename} ...")

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # 写入表头
    writer.writerow(["Product Name", "Price (Messy)", "Stock Status", "SKU_ID"])
    
    # 循环 500 次
    for i in range(500):
        writer.writerow(generate_messy_row())

print(f"✅ 完成！已生成 500 条脏数据。")