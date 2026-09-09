# ==============================================================================
# [Script] Instructor-Side Secure Script & Teaching Prompt Portal
# 【教師專屬】講稿與課堂導引主控台（整合 LINE 公告逐條導讀與雙語講稿）
# ==============================================================================

import streamlit as st

st.set_page_config(
    page_title="Instructor Script Portal - Python AI Applications",
    layout="wide",
    page_icon="🗝️"
)

CORRECT_PASSWORD = "kimiko115"

def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    st.markdown("## 🔐 Instructor Portal Login")
    st.caption("Private teaching script portal for the instructor. Please enter password.")
    password = st.text_input("Password (教師密碼):", type="password")
    if st.button("Unlock (解鎖)"):
        if password == CORRECT_PASSWORD:
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("😕 密碼錯誤，請重新輸入。")
    return False

if not check_password():
    st.stop()

# ------------------------------------------------------------------------------
# 主控制台介面
# ------------------------------------------------------------------------------
st.title("🗝️ 教師專屬講稿與課堂提示控制台")
st.caption("🎯 課堂進程：Part 1 觀念、LINE 公告逐項解說與導覽 ➔ Part 2 雲環境與 Live Demo ➔ Part 3 Lab 0 實作與雙軌 AI")

st.markdown("---")

with st.sidebar:
    st.header("📌 導航控制台")
    selected_week = st.selectbox("選擇上課週次", [f"Week {i}" for i in range(1, 19)])
    st.markdown("---")
    st.markdown("**💡 第一節開場關鍵提醒**：")
    st.info("大螢幕投影學生端入口網頁（ai-syllabus.streamlit.app）。引導掃描右上角 LINE Chat QR 後，請帶領全班點開置頂公告，逐條說明教室、必備筆電/手機、信箱與改暱稱規則！")
    if st.button("🔒 鎖定返回登入頁"):
        st.session_state["password_correct"] = False
        st.rerun()

if selected_week == "Week 1":
    st.header("📅 Week 1: 課程導覽與自然語言編程 (Course Onboarding & Vibe Coding)")
    st.markdown("🕒 **授課時間**：09:00 - 11:50 ｜ 📍 **上課地點**：創新大樓 506 教室 (創506)")
    
    tab1, tab2, tab3 = st.tabs([
        "Part 1 ｜ 破冰、LINE 公告逐條解說與網頁導航 (09:00 - 09:50)", 
        "Part 2 ｜ 雲環境、快捷鍵與 Live Demo (10:00 - 10:50)", 
        "Part 3 ｜ Lab 0 實作與雙軌 AI (11:00 - 11:50)"
    ])
    
    # --------------------------------------------------------------------------
    # TAB 1: 第一節課（09:00 - 09:50）
    # --------------------------------------------------------------------------
    with tab1:
        st.subheader("🎙️ Part 1：破冰、LINE 社群公告逐項解說與網頁導覽 (學校第 2 節：09:00 - 09:50)")
        
        # 內嵌 LINE 公告全文供老師現場對照
        with st.expander("📋 LINE 社群置頂公告全文（現場逐條對照）", expanded=True):
            st.code("""
📌 [Python AI Applications] Course Information & Essential Links

Welcome to Python AI Applications! Please read the following key details and bookmark this post:

📍 Classroom: Innovation Building, Room 506 (創506) | Thursdays 09:00 - 11:50
🎒 Required Devices for Every Class:
   1. Laptop / Notebook (Required): Used for cloud coding with Google Colab.
   2. Smartphone: Used for LINE chat, real-time AI Q&A, and mobile app preview.
🔗 Course Portal: https://ai-syllabus.streamlit.app/
💻 In-Class Cloud Tools:
   • Google Colab: https://colab.research.google.com/
   • Google Gemini: https://gemini.google.com/
✉️ Official Contact Email: kimikohuang@mail.mcut.edu.tw
⚠️ Group Nickname Policy:
   Please set your nickname as: 👉 "Last 3 digits of Student ID + Your Name" (e.g. 205 Huy)
   *Required to verify attendance and log bonus participation points.*
            """, language="text")

        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **09:00 - 09:15 ｜ 破冰、雙 QR Code 與 LINE 置頂公告逐條導讀**
              * *操作重點*：指著大螢幕右上角的 **Portal QR** 與 **LINE Chat QR**，請全班拿手機掃描。
              * *逐條帶讀 LINE 公告*：
                1. **教室確認**：本課程固定在「創新大樓 506 教室 (創506)」。
                2. **每週必備設備**：強調每週務必攜帶 **筆電（跑 Colab 實作）** 與 **手機（LINE 與行動 App 成果預覽）**；今天未帶筆電者稍後安排 Pair Programming。
                3. **傳送門與工具**：介紹 Portal 網址、Google Colab 與 Google Gemini。
                4. **聯絡管道**：一般問題在 LINE 群直接問；隱私與成績寄至官方信箱 `kimikohuang@mail.mcut.edu.tw`。
                5. **群組暱稱規範（最重要）**：現場監督全班將暱稱改成「學號末三碼 + 名字」（如：`205 Huy`），說明這是點名出缺席與平常發問加分的唯一依據！
            * **09:15 - 09:25 ｜ 多語系切換與側邊欄 AI 助教演練**
              * *操作重點*：現場點擊 Vietnamese、Indonesian 等按鈕展示瞬切多語系。
              * *引導說明*：展開左側邊欄 **Course AI Assistant**，說明提問能拿加分，支援 7 國語言與匿名模式。
            * **09:25 - 09:35 ｜ 四大核心卡片與指揮家思維**
              * *卡片導覽*：串聯大一會計經濟、大二統計管理；50% 上機、20% 期中、30% 期末。
              * *指揮家思維*：不背語法，用自然語言 prompt 當樂團指揮家。
            * **09:35 - 09:40 ｜ 激勵亮點：展示 Streamlit 網頁力量**
              * *激勵說明*：大家手機上的整個課綱網頁與 AI 助教，都是老師用純 Python + Streamlit 做的！前幾週在 Colab 打基礎，第 10-11 週大家也能做出自己的 Web App 發布到手機上。
            * **09:40 - 09:48 ｜ 點開「18 週課綱進度總表」看全學期里程碑**
              * *操作重點*：大螢幕展開總表，指出第 9 週期中報告、第 11 週雲端部署、第 17-18 週期末成果會。
            * **09:48 - 09:50 ｜ 第一節收尾與課間休息**
              * *預告*：10:00 第二節準時開箱 Google Colab 與鍵盤快捷鍵。
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **09:00 - 09:15 (QR & LINE Pinned Notice)**:
              *"Good morning everyone, welcome to Python AI Applications! Look at the top-right of the screen. Scan the left QR code for our course portal, and scan the right one to join our LINE OpenChat right now."*
              *(Once students join)*:
              *"Everyone, please open our **Pinned Announcement** in LINE. Let's go through it together:
              1. **Classroom**: We will meet here in Innovation Building Room 506 every Thursday.
              2. **Required Devices**: Bring your **laptop** (for Colab coding) and your **smartphone** every single week. If you didn't bring a laptop today, don't worry—we will do pair programming later.
              3. **Contact Email**: For private grading or leave matters, email `kimikohuang@mail.mcut.edu.tw`.
              4. **Important Nickname Rule**: Change your LINE nickname right now to **'Last 3 digits of Student ID + Your Name'** (e.g., `205 Huy`). We use this to verify attendance and award in-class engagement bonus points!"*
            * **09:15 - 09:25**: *"Notice the language buttons below the title—clicking Vietnamese, Indonesian, or Thai changes everything instantly. In the sidebar, our Course AI Assistant is ready. Asking questions earns participation points!"*
            * **09:25 - 09:35**: *"Review our 4 cards. Adopt the **Conductor Mindset**: AI is your orchestra, and you conduct it with prompts. Grading: 50% weekly practice, 20% midterm, 30% final."*
            * **09:35 - 09:40 (Motivation)**: *"Everything you see on your phone right now was built with pure Python and **Streamlit**! In Weeks 10 & 11, you will build and launch your very own live web apps on your phones."*
            * **09:40 - 09:48**: *"Let's expand the 18-week schedule. Notice Week 9 Midterm Review, Week 11 Cloud Deployment, and Weeks 17-18 Final FinTech Showcase."*
            * **09:48 - 09:50**: *"10-minute break. At 10:00, we scroll down to open Google Colab!"*
            """)

    # --------------------------------------------------------------------------
    # TAB 2: 第二節課（10:00 - 10:50）
    # --------------------------------------------------------------------------
    with tab2:
        st.subheader("🎙️ Part 2：雲端開箱、鍵盤快捷鍵、Gemini 互補與 Pair Programming (學校第 3 節：10:00 - 10:50)")
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **10:00 - 10:15 ｜ Google 帳號、鍵盤快捷鍵暖身與 Pair Programming**
              * *鍵盤暖身*：說明打字與快捷鍵是跟 AI 高效溝通的超能力。帶大家複習 Windows (`Ctrl`) 與 Mac (`Cmd ⌘`) 的核心捷徑：
                * 複製 `Ctrl/Cmd + C`、貼上 `Ctrl/Cmd + V`、剪下 `Ctrl/Cmd + X`
                * **救命鍵（復原）**：`Ctrl/Cmd + Z`（代碼改壞或刪掉時一鍵還原）
                * **Colab 執行神鍵**：`Shift + Enter`（免按滑鼠，一鍵跑程式）
              * *Pair Programming*：若沒帶電腦，兩人一組結對協作，共同下提示詞與除錯。
            * **10:15 - 10:25 ｜ 雙軌 AI 互補機制說明 (Colab + Gemini)**
              * *引導說明*：開另一個分頁放 Google Gemini。Colab 內建 AI 額度用完或遇到複雜報錯時，用快捷鍵 `Ctrl/Cmd + C` 複製貼到 Gemini，確保實作不中斷。
            * **10:25 - 10:40 ｜ 現場 Live Demo：4 行 Python 抓取台積電股價**
              * *操作重點*：老師在講台投影 Colab，現場輸入 yfinance 抓取台積電 (`2330.TW`) 並繪圖。
            * **10:40 - 10:48 ｜ 商業數據思考與第三節任務預告**
              * *引導說明*：連結大一經濟與會計數據，預告第三節換大家親手跑程式。
            * **10:48 - 10:50 ｜ 課間緩衝與連線疑難排解**
              * *引導說明*：下課 2 分鐘，協助確認連線狀態。
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **10:00 - 10:15**: *"Welcome back! Let's unlock some keyboard superpowers:
              - **Copy / Paste**: `Ctrl + C` / `Ctrl + V` on Windows, or `Cmd ⌘ + C` / `Cmd ⌘ + V` on Mac.
              - **The Life Saver (Undo)**: `Ctrl + Z` or `Cmd ⌘ + Z` if you accidentally delete code!
              - **Colab Instant Run**: Press `Shift + Enter` to run any code cell instantly.
              If you don't have a laptop today, pair up with the classmate next to you for **Pair Programming**."*
            * **10:15 - 10:25**: *"Keep a separate tab open for **Google Gemini**. When Colab's AI hits its usage quota, copy your code with `Ctrl+C` and paste into Gemini with `Ctrl+V`!"*
            * **10:25 - 10:40**: *"Look at the main screen. With 4 lines of Python, we fetch TSMC's daily prices (`2330.TW`) and plot a trend chart."*
            * **10:40 - 10:48**: *"Think back to Economics and Accounting. In our next session, you will run this notebook yourself."*
            * **10:48 - 10:50**: *"Take a short break. Any Wi-Fi issues, come to the front desk now!"*
            """)

    # --------------------------------------------------------------------------
    # TAB 3: 第三節課（11:00 - 11:50）
    # --------------------------------------------------------------------------
    with tab3:
        st.subheader("🎙️ Part 3：Lab 0 動手實作與雙軌 AI 輔助體驗 (學校第 4 節：11:00 - 11:50)")
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **11:00 - 11:15 ｜ Lab 0 實作發布與雙軌 AI 說明**
              * *任務佈達*：每位同學在 Colab 執行台積電腳本，並嘗試將股票代號改為蘋果 (`AAPL`)。
              * *雙軌 AI 策略*：指導同學點擊網頁上的 **💡 Open Google Gemini** 放在獨立分頁。告訴大家 Colab 內建 AI 額度用完時，直接把程式碼複製到 Gemini 詢問。
            * **11:15 - 11:35 ｜ 課堂巡視與個別指導**
              * *走動巡視*：協助排除儲存格未執行或拼字錯誤等問題，鼓勵學生善用 AI 助教。
            * **11:35 - 11:45 ｜ 加碼挑戰（針對進度超前學生）**
              * *進階挑戰*：引導完成得快的同學詢問 AI：「如何把 TSMC 與 Apple 畫在同一張圖表上進行對比？」
            * **11:45 - 11:50 ｜ 全課總結與下週預告**
              * *結語說明*：嘉許全班達成第一天成功在雲端執行 Python 的里程碑，預告下週「市場數據工程：Apple 與 TSMC 的深入對比」。
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **11:00 - 11:15**: *"It's hands-on time! Run the TSMC script in Colab, then try changing `2330.TW` to Apple (`AAPL`). Keep Gemini open in a separate tab as your backup AI when Colab limits are reached."*
            * **11:15 - 11:35**: *(Walking around the classroom)* *"Great work seeing those charts appear! If you run into any red error messages, ask Gemini or our sidebar AI Assistant."*
            * **11:35 - 11:45**: *"Bonus challenge for fast learners: Ask Gemini how to plot both TSMC and Apple on the exact same graph to compare their returns!"*
            * **11:45 - 11:50**: *"Congratulations on running your first Python AI script today! Next week, we will dive deeper into Market Data Engineering. Have a great week, see you next Thursday!"*
            """)

else:
    st.info(f"🚧 **{selected_week} 教師專屬講稿與提示** 蓄勢待發中！")
