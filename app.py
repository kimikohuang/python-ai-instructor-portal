# ==============================================================================
# [Script] Instructor-Side Secure Script & Teaching Prompt Portal
# 【教師專屬】加密講稿與課堂提示管理系統（精準對齊明志科大課表時間）
# ==============================================================================

import streamlit as st

# 1. 頁面基本配置
st.set_page_config(
    page_title="Instructor Script Portal - Python AI Applications",
    layout="wide",
    page_icon="🗝️"
)

# 2. 密碼保護設定
CORRECT_PASSWORD = "kimiko115"

def check_password():
    """驗證密碼的函式"""
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    # 登入畫面
    st.markdown("## 🔐 Instructor Portal Login")
    st.caption("This is a private teaching script portal for the instructor. Please enter the password to unlock.")
    
    password = st.text_input("Password (請輸入教師專屬密碼):", type="password")
    if st.button("Unlock (解鎖)"):
        if password == CORRECT_PASSWORD:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("😕 Incorrect password. Please try again. (密碼錯誤，請重新輸入)")
    return False

if not check_password():
    st.stop()

# ==============================================================================
# 密碼通過後的教師專屬介面
# ==============================================================================

st.title("🗝️ 教師專屬講稿與課堂提示控制台")
st.caption("🎯 精確對齊學校節次時間：第 2 節 (09:00-09:50)｜第 3 節 (10:00-10:50)｜第 4 節 (11:00-11:50)")

st.markdown("---")

# 側邊欄：快速導航與系統工具
with st.sidebar:
    st.header("📌 導航控制台")
    selected_week = st.selectbox("選擇上課週次", [f"Week {i}" for i in range(1, 19)])
    st.markdown("---")
    st.markdown("**💡 開學日提醒**：")
    st.info("大螢幕請先投影學生端 Syllabus 網頁。若有同學未帶筆電，可引導啟用 Pair Programming（兩人一組）。")
    
    if st.button("🔒 鎖定返回登入頁"):
        st.session_state["password_correct"] = False
        st.rerun()

# 主畫面：Week 1 詳細講稿
if selected_week == "Week 1":
    st.header("📅 Week 1: 課程導覽與自然語言編程 (Course Onboarding & Vibe Coding)")
    st.markdown("🕒 **日期**：2026/09/10 (四) | 📍 **地點**：實體教室")
    
    tab1, tab2, tab3 = st.tabs([
        "第 2 節 (09:00 - 09:50)", 
        "第 3 節 (10:00 - 10:50)", 
        "第 4 節 (11:00 - 11:50)"
    ])
    
    with tab1:
        st.subheader("🎙️ 第 2 節：破冰、課程總覽與心態建立 (09:00 - 09:50)")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **09:00 - 09:10 ｜ 破冰與門戶導覽**
              * *中文說明*：歡迎同學，介紹這門課的核心目標，引導掃描大螢幕 QR Code 進入網頁及加入 LINE 社群。提醒 LINE 暱稱設為「學號末三碼 + 名字」（例如 `205 Huy`）。
            * **09:10 - 09:30 ｜ 建立指揮家思維 (Conductor Mindset)**
              * *中文說明*：強調不需要寫程式底子。不是當苦練樂器細節的樂手，而是當指揮家，以自然語言提示詞指揮 AI。
            * **09:30 - 09:45 ｜ 評量標準與期望管理**
              * *中文說明*：說明 50% 平常實作、20% 期中、30% 期末專案，強調初學者友善與步驟式引導。
            * **09:45 - 09:50 ｜ 第一節總結與 Q&A**
              * *中文說明*：解答疑問，預告 10:00 進入雲端上機環境。
            """)
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **09:00 - 09:10**: *"Welcome everyone to Python AI Applications! Please scan the QR Code on the screen to open our course portal and join our LINE OpenChat. Remember to set your LINE nickname as your last 3 digits plus your name, for example, '205 Huy'."*
            * **09:10 - 09:30**: *"You do not need any coding background. Previously, programming meant memorizing dense syntax. Today, you act as the **conductor** of an orchestra. You guide the AI with natural language prompts to create business solutions."*
            * **09:30 - 09:45**: *"Our grading policy: 50% for weekly in-class hands-on labs, 20% for the midterm, and 30% for the final project showcase. Beginners are warmly welcome!"*
            * **09:45 - 09:50**: *"Any questions before we take a short break? When we return at 10:00, we will open our web browsers and dive straight into Google Colab."*
            """)
            
    with tab2:
        st.subheader("🎙️ 第 3 節：雲環境開箱與 Live Demo 示範 (10:00 - 10:50)")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **10:00 - 10:15 ｜ Google 帳號與 Colab 環境確認**
              * *中文說明*：帶領同學登入 Colab。若有未帶電腦的同學，引導採 Pair Programming（兩人一組共用螢幕）。
            * **10:15 - 10:35 ｜ 現場即時示範：抓取台積電股價**
              * *中文說明*：老師大螢幕現場示範 4 行 Python 代碼，抓取台積電 (`2330.TW`) 股價並即時繪製走勢圖。
            * **10:35 - 10:45 ｜ 連結商業與數據的價值**
              * *中文說明*：引導同學連結大一經濟與會計數據，說明動態視覺化如何協助經管商業決策。
            * **10:45 - 10:50 ｜ 課間緩衝與疑難排解**
              * *中文說明*：開放讓連線或帳號有問題的同學上前詢問，確保 11:00 準時進入 Lab 0 實作。
            """)
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **10:00 - 10:15**: *"Welcome back! Please open your laptops, sign into your Google account, and visit `colab.research.google.com`. If you don't have a laptop today, please pair up with the classmate next to you. In tech teams, this is called 'Pair Programming'."*
            * **10:15 - 10:35**: *"Look up at the main screen. With just four lines of Python, we connect to market data and fetch TSMC's daily prices (ticker `2330.TW`), instantly plotting a visual trend."*
            * **10:35 - 10:45**: *"Think back to freshman Economics and Accounting. Instead of static tables, Python empowers you to observe market volatility dynamically. In our next session, you will run this notebook yourself."*
            * **10:45 - 10:50**: *"Take a 10-minute break. If anyone has Wi-Fi or Google login issues, come to the front now so we can solve it before our hands-on lab at 11:00."*
            """)
            
    with tab3:
        st.subheader("🎙️ 第 4 節：Lab 0 實作與 AI 助教互動 (11:00 - 11:50)")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **11:00 - 11:15 ｜ Lab 0 任務佈達與動手操作**
              * *中文說明*：發布第一週任務，請同學點開網頁上的 Colab 連結，親手運行程式並嘗試將代號換成蘋果 (`AAPL`)。
            * **11:15 - 11:35 ｜ 走動巡視與側邊欄 AI 助教介紹**
              * *中文說明*：走動巡視。提醒卡關的同學可透過網頁側邊欄的 AI 助教提問（支援匿名與各國語言）。
            * **11:35 - 11:45 ｜ 加碼挑戰（針對進度超前者）**
              * *中文說明*：引導進度較快者將台積電與蘋果的數據繪製在同一張圖表上作初步對比。
            * **11:45 - 11:50 ｜ 課堂總結與下週預告**
              * *中文說明*：嘉許全班完成首次雲端執行，預告下週「市場數據工程：Apple 與 TSMC 的深入對比」。
            """)
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **11:00 - 11:15**: *"Click the Week 1 Colab link on our course portal. Run the first cell and try changing the stock symbol from TSMC to Apple (`AAPL`). Watch the chart update automatically."*
            * **11:15 - 11:35**: *(Walking around)* *"If you hit an error, remember you can ask our **Course AI Assistant** in the sidebar. It accepts questions in English, Chinese, and Vietnamese, and you can ask anonymously."*
            * **11:35 - 11:45**: *"For fast learners, here is your bonus challenge: plot both Apple and TSMC on the same graph to compare their performance side-by-side!"*
            * **11:45 - 11:50**: *"Fantastic job today! Everyone ran their first Python script in the cloud. Next week, we will explore Market Data Engineering with a deep comparison between Apple and TSMC. See you next Thursday!"*
            """)

else:
    st.info(f"🚧 **{selected_week} 教師專屬講稿與提示** 蓄勢待發中！")
