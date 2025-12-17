import asyncio
from playwright.async_api import async_playwright
import os

# 获取当前脚本所在的文件夹路径，用于存放浏览器数据
USER_DATA_DIR = os.path.join(os.getcwd(), "fiverr_browser_data")

async def run_persistent_bot():
    print("🤖 启动【持久化记忆】间谍机器人...")
    print(f"📁 浏览器缓存路径: {USER_DATA_DIR}")

    async with async_playwright() as p:
        # 【核心修改】使用 launch_persistent_context
        # 这会启动一个带有“记忆”的真实 Chrome 浏览器
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR, # 记忆存放在这里
            channel="chrome",            # 强制使用电脑上的 Chrome 正式版
            headless=False,              # 有头模式
            slow_mo=1000,
            args=['--disable-blink-features=AutomationControlled'], # 去除机器人特征
            viewport={"width": 1280, "height": 720}
        )
        
        page = browser.pages[0] # 获取第一个标签页

        # 1. 访问 Fiverr
        print("🌍 正在进入 Fiverr...")
        try:
            await page.goto("https://www.fiverr.com/search/gigs?query=PCB%20Design", timeout=60000)
        except:
            print("⚠️ 载入稍慢，继续执行...")

        # 2. 关键交互区
        print("\n" + "="*50)
        print("🚨 【首次运行必读】 🚨")
        print("1. 第一次运行通常会弹验证码/Press & Hold。")
        print("2. 请手动搞定它！直到你看到一排排的 PCB 商品列表。")
        print("3. 一旦验证通过，你的身份就被保存了。下次再跑就不用验证了。")
        print("4. 确保页面上有显示价格（比如 $20）。")
        print("="*50 + "\n")
        
        input(">>> 看到价格列表后，请在这里按回车键开始抓取...")

        # 3. 视觉抓取数据
        print("⏳ 正在扫描价格...")
        
        # 查找页面上所有带 $ 的文字
        try:
            price_elements = await page.get_by_text("$").all()
            
            prices_found = []
            
            for el in price_elements:
                txt = await el.text_content()
                txt = txt.strip()
                # 筛选合法的价格数字
                if txt.startswith("$") and len(txt) < 10 and any(char.isdigit() for char in txt):
                    prices_found.append(txt)
            
            # 去重并打印
            unique_prices = list(set(prices_found))
            
            if len(unique_prices) > 0:
                print(f"\n✅ 成功抓取到 {len(unique_prices)} 个价格数据:")
                print(unique_prices[:10]) # 只显示前10个
                
                # 简单算个平均值（去掉$符号）
                nums = [int(p.replace("$", "").replace(",", "")) for p in unique_prices if p.replace("$", "").isdigit()]
                if nums:
                    avg_price = sum(nums) / len(nums)
                    print(f"\n📊 市场平均报价约为: ${avg_price:.2f}")
            else:
                print("⚠️ 没抓到数据，请确保屏幕上能直接看到价格数字。")

        except Exception as e:
            print(f"❌ 出错: {e}")

        print("\n💤 任务结束 (按回车关闭浏览器)...")
        input() # 防止浏览器秒关，让你看清结果
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_persistent_bot())