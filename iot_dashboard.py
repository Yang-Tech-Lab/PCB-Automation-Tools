import customtkinter as ctk
import time

# --- 1. 设置外观 ---
ctk.set_appearance_mode("Dark")  # 深色模式 (黑客风)
ctk.set_default_color_theme("green")  # 主题色：绿色

# --- 2. 创建窗口 ---
app = ctk.CTk()
app.geometry("400x500")
app.title("Yang-Tech IoT Commander")

# --- 3. 核心功能函数 ---
is_on = False

def toggle_switch():
    global is_on
    is_on = not is_on
    
    if is_on:
        btn.configure(text="SYSTEM ACTIVE", fg_color="#ff4747") # 变红
        status_label.configure(text="Status: CONNECTED & ON", text_color="#4CAF50")
        console.insert("0.0", f"[{time.strftime('%H:%M:%S')}] Relay Activated!\n")
    else:
        btn.configure(text="ACTIVATE SYSTEM", fg_color="#2cc985") # 变绿
        status_label.configure(text="Status: STANDBY", text_color="gray")
        console.insert("0.0", f"[{time.strftime('%H:%M:%S')}] System Shutdown.\n")

# --- 4. 界面布局 ---

# 标题
title = ctk.CTkLabel(app, text="IOT CONTROL CENTER", font=("Roboto Medium", 24))
title.pack(pady=30)

# 状态指示
status_label = ctk.CTkLabel(app, text="Status: STANDBY", font=("Arial", 16), text_color="gray")
status_label.pack(pady=10)

# 大按钮
btn = ctk.CTkButton(app, text="ACTIVATE SYSTEM", command=toggle_switch, width=200, height=60, font=("Arial", 18, "bold"))
btn.pack(pady=40)

# 模拟控制台 (Log)
console = ctk.CTkTextbox(app, width=350, height=150)
console.pack(pady=20)
console.insert("0.0", "System initialized...\nWaiting for commands...\n")

# 底部版权
footer = ctk.CTkLabel(app, text="© 2025 Yang-Tech-Lab", text_color="gray")
footer.pack(side="bottom", pady=10)

# --- 5. 运行 ---
app.mainloop()