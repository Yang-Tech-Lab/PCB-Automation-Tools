import tkinter as tk
from tkinter import messagebox
import os

def start_mission():
    # Change status to English
    status_label.config(text="Running... Please wait", fg="red")
    window.update() 
    
    try:
        # 核心逻辑不变，还是调用爬虫脚本
        os.system("python scrape_all_books.py")
        
        # 英文弹窗
        messagebox.showinfo("Success", "Task Completed! \nData saved to Excel successfully.")
        status_label.config(text="Ready", fg="green")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# --- UI Setup ---

# 1. Main Window
window = tk.Tk()
window.title("Fiverr Data Scraper Tool V1.0") # 窗口标题
window.geometry("450x350") # 稍微大一点，显得大气

# 2. Header (Title)
# Helvetica 是非常通用的西文商务字体
title_label = tk.Label(window, text="Web Data Extractor", font=("Helvetica", 22, "bold"))
title_label.pack(pady=20)

# 3. Description
desc_text = "Target: books.toscrape.com\nExtract Product Name, Price, and Rating to Excel."
desc_label = tk.Label(window, text=desc_text, font=("Arial", 10), justify="center")
desc_label.pack()

# 4. Action Button
# 英文按钮，文字加粗
btn = tk.Button(window, text="START SCRAPING", font=("Arial", 12, "bold"), bg="#28a745", fg="white", width=20, height=2, command=start_mission)
btn.pack(pady=30)

# 5. Status Bar
status_label = tk.Label(window, text="Ready", font=("Arial", 10), fg="green")
status_label.pack()

# 6. Branding (Your Studio Name)
footer_label = tk.Label(window, text="© 2025 Developed by Yang-Tech-Lab", font=("Arial", 8), fg="gray")
footer_label.pack(side="bottom", pady=10)

# 7. Loop
window.mainloop()