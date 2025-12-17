from fastapi import FastAPI
import random
from datetime import datetime

# 1. 初始化 App
app = FastAPI(
    title="Yang-Tech Crypto API",
    description="一个用于获取实时加密货币价格的专用接口。",
    version="1.0.0"
)

# --- 模拟获取价格的核心逻辑 ---
def get_btc_price():
    # 这里模拟去雅虎财经查价格 (为了演示速度，用随机数代替)
    # 真实项目中，你可以把之前的 yfinance 代码放进来
    return round(random.uniform(95000, 99000), 2)

# 2. 定义接口 (Endpoints)

@app.get("/")
def read_root():
    """首页：打个招呼"""
    return {"message": "欢迎访问 Yang-Tech-Lab API 服务器！请访问 /docs 查看文档。"}

@app.get("/get_price")
def read_price():
    """获取最新 BTC 价格"""
    price = get_btc_price()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 返回 JSON 数据 (这是 API 的标准格式)
    return {
        "asset": "BTC-USD",
        "price": price,
        "timestamp": now,
        "status": "active"
    }

@app.get("/analyze/{threshold}")
def analyze_price(threshold: float):
    """
    智能分析接口：
    客户可以输入一个阈值 (threshold)，我们告诉他是否该买入。
    例如访问：/analyze/98000
    """
    current_price = get_btc_price()
    
    if current_price < threshold:
        advice = "BUY NOW! (Price is low)"
    else:
        advice = "HOLD. (Price is high)"
        
    return {
        "current_price": current_price,
        "your_threshold": threshold,
        "ai_advice": advice
    }