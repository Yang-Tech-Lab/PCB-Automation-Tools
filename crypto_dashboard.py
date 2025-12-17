import streamlit as st
import requests
import time
import pandas as pd
import random

st.set_page_config(page_title="Yang-Tech Crypto Monitor", page_icon="📈")

st.title("📈 比特币实时监控大屏")
st.caption("Frontend: Streamlit | Backend: FastAPI | Architecture: Microservices")

# 定义你的 API 地址 (就是刚才你测试成功的那个网址)
API_URL = "http://127.0.0.1:8000/get_price"

# 创建占位符 (用来动态刷新数据)
price_metric = st.empty()
chart_placeholder = st.empty()
history_data = []

st.write("🔴 正在连接 Yang-Tech API 服务器...")

# 循环请求数据 (模拟实时监控)
for i in range(100):
    try:
        # --- 关键一步：前端呼叫后端 ---
        response = requests.get(API_URL)
        
        if response.status_code == 200:
            data = response.json() # 拿到刚才那个 JSON
            
            price = data['price']
            timestamp = data['timestamp'].split(" ")[1] # 只取时间部分
            
            # 1. 更新大数字
            price_metric.metric(
                label="BTC-USD 实时价格", 
                value=f"${price:,.2f}",
                delta=f"{random.uniform(-50, 50):.2f}" # 模拟一点波动显示
            )
            
            # 2. 更新图表
            history_data.append({"Time": timestamp, "Price": price})
            df = pd.DataFrame(history_data)
            chart_placeholder.line_chart(df.set_index("Time"))
            
            # 休息 1 秒再请求
            time.sleep(1)
            
        else:
            st.error("无法连接到 API 服务器！")
            break
            
    except Exception as e:
        st.error(f"连接错误: {e}")
        st.info("请检查：你的 FastAPI 黑框框是不是关掉了？")
        break