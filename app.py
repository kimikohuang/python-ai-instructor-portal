# ==============================================================================
# [Script] Instructor-Side Secure Script & Teaching Prompt Portal
# 【教師專屬】加密講稿與課堂提示管理系統（含詳細中英文授課時間軸）
# ==============================================================================

import streamlit as st

# 1. 頁面基本配置
st.set_page_config(
    page_title="Instructor Script Portal - Python AI Applications",
    layout="wide",
    page_icon="🗝️"
)

# 2. 密碼保護設定 (您可以隨時在此修改密碼)
CORRECT_PASSWORD = "kimiko115"  # 您可以自行更換這組密碼

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

# 如果密碼未通過，停止執行後續程式碼
if not check_password():
    st.stop()

# ==============================================================================
# 密碼通過後的教師專屬介面
# ==============================================================================

st.title("🗝️ 教師專屬講稿與課堂提示控制台")
st.caption("🎯 建議使用平板或第二台筆電開啟此頁面，作為上課時的口頭提示、中英文授課時間軸與互動金句備忘錄。")

st.markdown("---")

# 側邊欄：快速導航與系統工具
with st.sidebar:
    st.header("📌 導航控制台")
    selected_week = st.selectbox("選擇上課週次", [f"Week {i}" for i in range(1, 19)])
    st.markdown("---")
    st.markdown("**💡 教學小叮嚀**：")
    st.info("開學第一週請務必確認大螢幕投影的是學生端多語系網頁，並引導外籍生掃描 QR Code 加入 LINE 社群。")
    
    if st.button("🔒 鎖定返回登入頁"):
        st.session_state["password_correct"] = False
        st.rerun()

# 主畫面：根據選擇的週次顯示對應的教師講稿
if selected_week == "Week 1":
    st.header("📅 Week 1: 課程導覽與自然語言編程 (Course Onboarding & Vibe Coding)")
    st.markdown("🕒 **日期**：2026/09/10 | 📍 **地點**：實體教室")
    
    # 建立三個分頁對應三節課
    tab1, tab2, tab3 = st.tabs(["第一節 (09:10-10:00)", "第二節 (10:10-11:00)", "第三節 (11:10-12:00)"])
    
    with tab1:
        st.subheader("🎙️ 第一節：破冰、課程總覽與心態建立 (Session 1)")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **00:00 - 10:00 ｜ 破冰與門戶導覽**
              * *中文說明*：歡迎同學，介紹這門課的核心目標，並引導同學掃描大螢幕 QR Code 打開多語系網頁與加入 LINE 社群。提醒 LINE 暱稱設為「學號末三碼 + 名字」（例如 `205 Huy`）。
            * **10:00 - 30:00 ｜ 建立指揮家思維 (Conductor Mindset)**
              * *中文說明*：解釋為什麼不需要寫程式底子。我們不是要當苦命的樂手去背語法，而是要當指揮家，學會用自然語言指揮 AI。
            * **30:00 - 45:00 ｜ 評量標準與期望管理**
              * *中文說明*：說明 50% 課堂實作、20% 期中、30% 期末專案的配分，強調初學者友善與步驟引導。
            * **45:00 - 50:00 ｜ 第一節總結與 Q&A**
              * *中文說明*：開放現場提問，預告準備進入第二節的雲端上機環境。
            """)
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts (英文授課講稿)")
            st.info("""
            * **00:00 - 10:00**: *"Welcome everyone to Python AI Applications! Please scan the QR Code on the screen right now with your phone to open our multi-language syllabus portal and join our LINE OpenChat. Remember to set your LINE nickname as your last 3 digits plus your name, for example, '205 Huy'."*
            * **10:00 - 30:00**: *"You don't need any prior coding background. In the past, learning programming meant memorizing difficult syntax—like learning to play every single note on an instrument. But today, in the era of AI, we act as the **conductor** of an orchestra. You guide the AI with natural language to build powerful business applications."*
            * **30:00 - 45:00**: *"Our grading policy is simple: 50% for weekly in-class practice, 20% for the midterm, and 30% for the final project showcase. Step-by-step guidance is provided in every class, so beginners are very welcome!"*
            * **45:00 - 50:00**: *"Any questions so far? Great. In our next session, we will open our web browsers and jump straight into Google Colab without installing anything heavy."*
            """)
            
    with tab2:
        st.subheader("🎙️ 第二節：雲環境開箱與 Live Demo 示範 (Session 2)")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **00:00 - 15:00 ｜ Google Colab 雲端環境開箱**
              * *中文說明*：帶領同學登入瀏覽器，解說為什麼我們不用安裝複雜軟體，直接在雲端運算。
            * **15:00 - 35:00 ｜ 現場即時示範：抓取台積電股價**
              * *中文說明*：老師現場打程式碼（或用 AI 生成），示範如何用幾行 Python 抓取台積電 (`2330.TW`) 的每日股價並畫出走勢圖。
            * **35:00 - 45:00 ｜ 連結商業與數據的價值**
              * *中文說明*：引導同學思考大一學過的經濟與會計數據，如何透過 Python 變成視覺化決策工具。
            * **45:00 - 50:00 ｜ 第二節小結**
              * *中文說明*：確認大家都看懂示範，準備進入第三節的動手實作（Lab 0）。
            """)
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts (英文授課講稿)")
            st.info("""
            * **00:00 - 15:00**: *"Let's open your web browser and go to Google Colab. We won't install any heavy software on your laptops today. Colab acts like a cloud-based notebook where Python runs instantly in your browser."*
            * **15:00 - 35:00**: *"Watch my screen. With just a few lines of Python code, we can fetch real-time daily stock prices for TSMC—ticker symbol 2330.TW—and instantly plot a visual trend chart right in front of our eyes."*
            * **35:00 - 45:00**: *"Think about what you learned in freshman Economics and Accounting. Being able to pull live financial data and turn it into charts is your very first step toward business intelligence."*
            * **45:00 - 50:00**: *"Now that you've seen how magical it is, it's time for you to try it yourself in our third session."*
            """)
            
    with tab3:
        st.subheader("🎙️ 第三節：Lab 0 實作與 AI 助教互動 (Session 3)")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **00:00 - 15:00 ｜ Lab 0 任務佈達與動手操作**
              * *中文說明*：發布第一週的實作任務，請同學打開網頁中的 Colab 連結，自己跑一次範例程式碼。
            * **15:00 - 35:00 ｜ 走動式教學與側邊欄 AI 助教介紹**
              * *中文說明*：老師在教室走動巡視。同時提醒同學如果卡關、不好意思舉手，可以隨時使用網頁側邊欄的 AI 助教提問（可匿名）。
            * **35:00 - 45:00 ｜ 彈性加碼內容：如果進度超前？**
              * *中文說明*：針對進度較快的同學，引導他們嘗試抓取兩支股票（例如 Apple 與 TSMC）並放在同一張圖表上做初步對比。
            * **45:00 - 50:00 ｜ 課堂總結與預告**
              * *中文說明*：總結今天學會了 Colab 與自然語言編程，預告下週將進入「市場數據工程：Apple 與 TSMC 的深入對比」。
            """)
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts (英文授課講稿)")
            st.info("""
            * **00:00 - 15:00**: *"Open our syllabus portal, click on the Week 1 Colab link, and try running the sample code yourself. Modify the stock ticker from TSMC to Apple (AAPL), and see what happens."*
            * **15:00 - 35:00**: *(Walking around)* *"If you run into any errors or feel shy about raising your hand, check out the **Course AI Assistant** in the sidebar. You can type your questions there—even anonymously—and get instant help."*
            * **35:00 - 45:00**: *"For those who finish early, here is your bonus challenge: try modifying the code to fetch two stocks—Apple and TSMC—and plot them on the same chart. Compare their trends side-by-side!"*
            * **45:00 - 50:00**: *"Fantastic job today! You've successfully run your first cloud Python script. Next week, we will dive deeper into Market Data Engineering, comparing Apple and TSMC side-by-side. See you next week!"*
            """)

else:
    # 2-18 週的預設提示
    st.info(f"🚧 **{selected_week} 教師專屬講稿與提示** 正在蓄勢待發中！您可以隨時告訴我該週的教學重點，我來幫您擴充這份專屬講稿內容。")
