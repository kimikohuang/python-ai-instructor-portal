# ==============================================================================
# [Script] Instructor-Side Secure Script & Teaching Prompt Portal
# 【教師專屬】講稿與課堂導引主控台（整合網頁逐區導覽與 Part 1/2/3 節次）
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
st.caption("🎯 課堂進程：Part 1 觀念與網頁導覽 ➔ Part 2 雲端環境與 Live Demo ➔ Part 3 Lab 0 實作與 AI 互動")

st.markdown("---")

with st.sidebar:
    st.header("📌 導航控制台")
    selected_week = st.selectbox("選擇上課週次", [f"Week {i}" for i in range(1, 19)])
    st.markdown("---")
    st.markdown("**💡 第一節開場提醒**：")
    st.info("請確認教室大螢幕投影的是學生端網頁（ai-syllabus.streamlit.app），依序從雙 QR Code、多語系、四大卡片逐區帶領同學瀏覽。")
    if st.button("🔒 鎖定返回登入頁"):
        st.session_state["password_correct"] = False
        st.rerun()

if selected_week == "Week 1":
    st.header("📅 Week 1: 課程導覽與自然語言編程 (Course Onboarding & Vibe Coding)")
    st.markdown("🕒 **授課時間**：09:00 - 11:50 ｜ 📍 **實體教室**")
    
    tab1, tab2, tab3 = st.tabs([
        "Part 1 ｜ 破冰與網頁逐區導航 (09:00 - 09:50)", 
        "Part 2 ｜ 雲環境與 Live Demo (10:00 - 10:50)", 
        "Part 3 ｜ Lab 0 實作與雙軌 AI (11:00 - 11:50)"
    ])
    
    # --------------------------------------------------------------------------
    # TAB 1: 第一節課（09:00 - 09:50）
    # --------------------------------------------------------------------------
    with tab1:
        st.subheader("🎙️ Part 1：破冰、學生端網頁逐區拆解導覽與評量說明 (學校第 2 節：09:00 - 09:50)")
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **09:00 - 09:12 ｜ 破冰與頂部雙 QR Code 引導**
              * *操作重點*：指著大螢幕右上角的兩個 QR Code。
              * *引導說明*：請大家拿出手機或筆電，掃描左邊 **Portal QR** 收藏本學期互動課綱；掃描右邊 **LINE Chat** 加入課程專屬社群。
            * **09:12 - 09:20 ｜ 多語系切換與側邊欄 AI 助教介紹**
              * *操作重點*：大螢幕示範點擊切換越南語、印尼語、泰語等按鈕。
              * *引導說明*：強調本課程全面支援多語系；接著展開左側邊欄 **Course AI Assistant**，說明無論用任何語言提問都會被記錄在試算表中算平常參與加分，也能選「Anonymous」匿名提問。
            * **09:20 - 09:35 ｜ 拆解四大核心卡片與指揮家思維**
              * *卡片 1 (目標)*：串聯大一會計與經濟，為大二統計、行銷與管理做數據支撐。
              * *指揮家思維*：強調不需要死背 Python 語法，把 AI 當成整個交響樂團，我們當負責下提示詞指令的「指揮家」。
              * *卡片 2 (評量)*：每週上機 50%、期中 20%、期末 30%，無壓力步驟化學習。
              * *卡片 3 & 4 (教材與規範)*：全雲端 Colab 免安裝；提醒 LINE 暱稱設為「學號末三碼 + 名字」（如 205 Huy）。
            * **09:35 - 09:45 ｜ 點開「18 週課綱進度總表」宏觀瀏覽**
              * *操作重點*：在大螢幕點開 18 週折疊表，帶學生看全學期里程碑。
              * *引導說明*：重點指出第 9 週期中進度報告、第 11 週發布手機 Web App、第 17-18 週期末成果發表。
            * **09:45 - 09:50 ｜ 第一節收尾與下課休息**
              * *引導說明*：解答疑問。預告 10:00 準時進入下方「本週實作指引」，進行 Google Colab 雲端開箱。
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **09:00 - 09:12**: *"Good morning everyone, welcome to Python AI Applications! Please look at the top-right corner of our screen. Take out your smartphones or laptops: scan the left QR code to save our course portal, and scan the right one to join our class LINE group."*
            * **09:12 - 09:20**: *"Notice the language buttons below the title. If you click Vietnamese, Indonesian, or Thai, the entire syllabus adapts instantly. Also, in the left sidebar, we have our Course AI Assistant. Asking questions here earns you engagement points, and anonymous mode is always available."*
            * **09:20 - 09:35**: *"Let's look at the four core cards. In this class, you don't need to memorize coding syntax. Instead, adopt the **Conductor Mindset**: AI is your orchestra, and your job is to guide it with clear business prompts. Our grading: 50% weekly practice, 20% midterm, and 30% final showcase."*
            * **09:35 - 09:45**: *"Let's expand the 18-week schedule. Notice our key milestones: Week 9 Midterm Review, Week 11 Cloud App Deployment to smartphones, and Weeks 17-18 for the Final FinTech Showcase."*
            * **09:45 - 09:50**: *"We will take a 10-minute break. When we return at 10:00, we will scroll down to our Weekly Agenda and open Google Colab together!"*
            """)

    # --------------------------------------------------------------------------
    # TAB 2: 第二節課（10:00 - 10:50）
    # --------------------------------------------------------------------------
    with tab2:
        st.subheader("🎙️ Part 2：雲端環境開箱與台積電 Live Demo (學校第 3 節：10:00 - 10:50)")
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **10:00 - 10:15 ｜ Google 帳號與 Colab 傳送門點擊**
              * *引導說明*：請全班將學生端網頁往下滑到「課堂實作步驟」，點擊綠色的 **🚀 Open Google Colab**。確認 Google 帳號登入順利。若沒帶筆電，啟動 Pair Programming（結對編程）共用螢幕。
            * **10:15 - 10:35 ｜ 現場 Live Demo：4 行 Python 抓取台積電股價**
              * *操作重點*：老師在講台投影 Colab，現場輸入 yfinance 抓取台積電 (`2330.TW`) 並繪圖。
              * *示範說明*：展示不需在電腦安裝龐大軟體，只要雲端 4 行代碼就能即時抓取全球市場數據並產生走勢圖。
            * **10:35 - 10:45 ｜ 商業數據思考與第三節任務預告**
              * *引導說明*：引導同學思考大一經濟與會計數據，說明為何動態即時圖表能協助商業洞察。
            * **10:45 - 10:50 ｜ 課間緩衝與連線疑難排解**
              * *引導說明*：下課 10 分鐘，邀請剛才 Colab 開不起來或連不上 Wi-Fi 的同學到台前排除問題。
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **10:00 - 10:15**: *"Welcome back! Scroll down to our Weekly Agenda section and click the button: **🚀 Open Google Colab**. Make sure you are signed into your Google account. If you don't have a laptop today, please pair up with the classmate next to you."*
            * **10:15 - 10:35**: *"Look up at the main screen. With just 4 lines of Python in the cloud, we connect to market data and fetch TSMC's daily prices (ticker `2330.TW`), instantly plotting a visual trend."*
            * **10:35 - 10:45**: *"Think back to freshman Economics and Accounting. Instead of static tables, Python empowers you to observe market volatility dynamically. In our next session, you will run this notebook yourself."*
            * **10:45 - 10:50**: *"Take a 10-minute break. If anyone has Wi-Fi or Google login issues, come to the front desk now so we can solve it before our hands-on lab at 11:00."*
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
            * **11:00 - 11:15**: *"It's hands-on time! Run the TSMC script in your Colab, then try changing `2330.TW` to Apple (`AAPL`). Notice the button next to Colab: **💡 Open Google Gemini**. Keep Gemini open in a separate tab. When Colab's built-in AI reaches its quota, paste your code into Gemini for instant troubleshooting."*
            * **11:15 - 11:35**: *(Walking around the classroom)* *"Great work seeing those charts appear! If you run into any red error messages, ask Gemini or our sidebar AI Assistant."*
            * **11:35 - 11:45**: *"Bonus challenge for fast learners: Ask Gemini how to plot both TSMC and Apple on the exact same graph to compare their returns!"*
            * **11:45 - 11:50**: *"Congratulations on running your first Python AI script today! Next week, we will dive deeper into Market Data Engineering. Have a great week, see you next Thursday!"*
            """)

else:
    st.info(f"🚧 **{selected_week} 教師專屬講稿與提示** 蓄勢待發中！")
