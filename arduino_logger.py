import serial  # 导入串口库
import time
import pandas as pd
from datetime import datetime

print("📡 正在寻找 Arduino...")

# --- 配置区域 ---
# 如果你有真板子，去设备管理器看它是 COM 几，比如 'COM3'
PORT = 'COM3'  
BAUD_RATE = 9600 # 必须和 Arduino 代码里的 Serial.begin(9600) 一样

# 准备一个列表存数据
data_log = []

try:
    # 1. 尝试连接板子 (因为你没插板子，这行运行会报错，但这很正常)
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    print(f"✅ 成功连接到 {PORT}")
    
    print("开始记录数据 (按 Ctrl+C 停止)...")
    
    while True:
        # 2. 读取 Arduino 发过来的一行字
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            
            # 3. 获取当前时间
            now = datetime.now().strftime("%H:%M:%S")
            
            print(f"[{now}] 收到信号: {line}")
            
            # 4. 存入列表
            data_log.append({
                "时间": now,
                "信号内容": line
            })
            
            # (可选) 如果收到 "Light OFF"，我们可以让 Python 做点别的事
            # 比如：自动发邮件报警、自动截图等等...这就是自动化的威力！

except serial.SerialException:
    print("⚠️ 没检测到板子！")
    print("提示：这是一段【未来代码】。等你买了 Arduino Uno 插上电脑，")
    print("把代码里的 PORT 改成正确的端口号，它就能帮你自动记账了！")

except KeyboardInterrupt:
    # 当你按 Ctrl+C 强制停止时，保存数据
    print("\n🛑 停止记录。正在保存到 Excel...")
    df = pd.DataFrame(data_log)
    df.to_excel("sensor_data.xlsx", index=False)
    print("✅ 数据已保存到 sensor_data.xlsx")