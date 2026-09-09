# ==============================================================================
# [Script] Instructor-Side Secure Script & Teaching Prompt Portal
# 【教師專屬】講稿與課堂導引主控台（100% 精準對齊學校正式教學進度表）
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
st.caption("🎯 課堂進程：Part 1 觀念、LINE 公告導讀與進度表拆解 ➔ Part 2 雲環境與 Live Demo ➔ Part 3 Lab 0 實作與雙軌 AI")

st.markdown("---")

with st.sidebar:
    st.header("📌 導航控制台")
    selected_week = st.selectbox("選擇上課週次", [f"Week {i}" for i in range(1, 19)])
    st.markdown("---")
    st.markdown("**💡 重要行事曆提醒**：")
    st.warning("⚠️ 依學校教學進度表：**第 16 週 (12/24) 即為期末成果發表會 (Demo Day)**！第 17、18 週為學校自主學習活動（觀看 FinTech 影音與彙整歷程檔案），非實體發表。")
    st.markdown("---")
    if st.button("🔒 鎖定返回登入頁"):
        st.session_state["password_correct"] = False
        st.rerun()

if selected_week == "Week 1":
    st.header("📅 Week 1: 課程導覽與自然語言編程 (Course Onboarding & Vibe Coding)")
    st.markdown("🕒 **授課時間**：09:00 - 11:50 ｜ 📍 **上課地點**：創新大樓 506 教室 (創506)")
    
    tab1, tab2, tab3 = st.tabs([
        "Part 1 ｜ 破冰、LINE 公告逐條解說與網頁導航 (09:00 - 09:50)", 
        "Part 2 ｜ 雲環境、快捷鍵與台積電 Demo (10:00 - 10:50)", 
        "Part 3 ｜ Lab 0 實作與雙軌 AI (11:00 - 11:50)"
    ])
    
    # --------------------------------------------------------------------------
    # TAB 1: 第一節課（09:00 - 09:50）
    # --------------------------------------------------------------------------
    with tab1:
        st.subheader("🎙️ Part 1：破冰、LINE 社群公告逐項解說與網頁導覽 (學校第 2 節：09:00 - 09:50)")
        
        with st.expander("📋 LINE 社群置頂公告全文（現場逐條對照）", expanded=True):
            st.code("""
📌 [Python AI Applications] Official Course Information & Essential Links

📍 Classroom: Innovation Building, Room 506 (創506) | Thursdays 09:00 - 11:50
🎒 Required Devices for Every Class:
   1. Laptop / Notebook (Required): For hands-on cloud coding with Google Colab.
   2. Smartphone: For LINE chat, real-time AI Q&A, and mobile app preview.
🗓️ Key Milestones:
   • Week 9 (Nov 05): Midterm Hands-on Review (20%)
   • Week 16 (Dec 24): Final Project Showcase & Live Web App Demo (30%)
   • Weeks 17-18: Flexible Independent Study
🔗 Course Portal: https://ai-syllabus.streamlit.app/
💻 Open Cloud Tools: Colab, Gemini, AI Studio, FRED
🕒 Office Hours: Right after class in Room 506, or by appointment via LINE
✉️ Official Email: kimikohuang@mail.mcut.edu.tw
⚠️ Group Nickname Policy: 👉 "Last 3 digits of Student ID + Your Name" (e.g. 205 Huy)
            """, language="text")

        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **09:00 - 09:15 ｜ 破冰、雙 QR Code 與 LINE 置頂公告逐條導讀**
              * *操作重點*：指著大螢幕右上角 **Portal QR** 與 **LINE Chat QR**，請同學立即掃描加入。
              * *逐條帶讀 LINE 公告*：
                1. **教室地點**：創新大樓 506 教室 (創506)。
                2. **每週必備設備**：每週帶 **筆電（跑 Colab）** 與 **手機（LINE 與行動 App 成果預覽）**；今天未帶者稍後結對實作。
                3. **三大評量里程碑**：平常實作 50%、第 9 週期中評量 20%、**第 16 週 (12/24) 期末成果發表會 30%**（特別提醒 17-18 週為彈性自主學習）。
                4. **諮詢時間 (Office Hours)**：每週四下課後直接在 506 教室面談，或隨時在 LINE 群預約校內見面；公務信箱為 `kimikohuang@mail.mcut.edu.tw`。
                5. **群組暱稱規範**：現場監督全班將暱稱改成「學號末三碼 + 名字」（如：`205 Huy`），這是平時點名加分的唯一依據！
            * **09:15 - 09:25 ｜ 多語系切換與側邊欄 AI 助教演練**
              * *操作重點*：展示點擊越南語、印尼語等多語系切換；展開左側邊欄 **Course AI Assistant**，說明發問拿平時加分與匿名模式。
            * **09:25 - 09:35 ｜ 四大核心卡片、結對專題 (Pair Project) 與指揮家思維**
              * *指揮家思維*：不用死背語法，我們是指揮家，AI 是演奏樂手，以自然語言 prompt 協同作業。
              * *評量與專題機制（重要定調）*：
                * 平常實作 50%、第 9 週期中 20%、**第 16 週 (12/24) 期末成果發表會 30%**。
                * **期末專題採「結對彈性制（原則 2 人，可 1~3 人）」**：
                  - 原則上鼓勵 2 人一組搭檔，實踐 Pair Programming 雙人協作。
                  - 充分包容：若想獨立完成可 1 人一組；若有落單或奇數情況，開放 3 人一組（上限 3 人，全員均需有分工），確保完全沒有人被孤立！
                * **第 15 週安排**：資安防護檢查（隱藏 API Key）＋ 第三節全班專案診斷與發表彩排。
            * **09:35 - 09:40 ｜ 激勵亮點：展示 Streamlit 網頁力量**
              * *激勵說明*：眼前的手機課綱與 AI 助教全是老師用純 Python + Streamlit 打造的！前幾週在 Colab 打基礎，第 10-11 週大家也能做出自己的 Web App 發布到手機上。
            * **09:40 - 09:48 ｜ 點開「18 週進度總表」看全學期課程地圖**
              * *操作重點*：展開 18 週表，指出台積電數據工程、FRED 總經、Google AI Studio、財報法說會解析，直到第 16 週發表會。
            * **09:48 - 09:50 ｜ 第一節收尾與課間休息**
              * *預告*：10:00 準時進入下方「本週實作指引」，進行 Google Colab 雲端開箱與快捷鍵暖身。
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **09:00 - 09:15 (QR & LINE Pinned Notice)**:
              *"Good morning everyone, welcome to Python AI Applications! Look at the top-right of the screen. Scan the left QR code for our portal, and the right QR code to join our LINE OpenChat right now."*
              *(After joining)*:
              *"Everyone, please open our **Pinned Announcement** in LINE:
              1. **Classroom**: Innovation Building, Room 506 every Thursday.
              2. **Required Devices**: Bring your **laptop** (for cloud coding) and **smartphone** every single week.
              3. **Milestones**: 50% weekly practice, 20% midterm in Week 9, and **30% Final Showcase in Week 16 (Dec 24)**. Weeks 17-18 will be flexible independent study.
              4. **Office Hours**: You can talk to me directly right after class in Room 506, or message in this LINE chat to set up an on-campus meeting. Email: `kimikohuang@mail.mcut.edu.tw`.
              5. **Nickname Rule**: Change your LINE nickname right now to **'Last 3 digits of Student ID + Name'** (e.g. `205 Huy`). We use this for attendance and participation points!"*
            * **09:15 - 09:25**: *"Notice the language buttons below the title—the syllabus adapts to 7 languages instantly. In the sidebar, our Course AI Assistant is ready. Asking questions earns engagement points!"*
            * **09:25 - 09:35 (Grading & Flexible Pair Teams)**:
              *"Review our grading: 50% weekly practice, 20% midterm in Week 9, and 30% Final Showcase in Week 16.
              For our Final Showcase, we encourage **Pair Projects (teams of 2)**. To ensure everyone feels supported and no one is left behind, teams can be flexible: you may work **individually (1 person)**, as a **pair (2 people)**, or form a group of **3 people maximum** if there's an odd number.
              In Week 15, right before Demo Day, our 3rd session will be a hands-on project clinic and rehearsal to ensure your app is secure and ready!"*
            * **09:35 - 09:40 (Inspiration & Streamlit Showcase)**:
              *"Everything you see on your phone right now was built with pure Python and **Streamlit**! You don't need any prior coding background. We will start gently with Google Colab, and by Weeks 10 & 11, you will build and launch your very own live web apps on your phones!"*
            * **09:40 - 09:48**: *"Let's expand the 18-week schedule. Notice Week 9 Midterm Review, Week 11 Cloud Deployment, and Week 16 Final Showcase."*
            * **09:48 - 09:50**: *"10-minute break. At 10:00, we scroll down to open Google Colab!"*
            """)

    # --------------------------------------------------------------------------
    # TAB 2: 第二節課（10:00 - 10:50）
    # --------------------------------------------------------------------------
    with tab2:
        st.subheader("🎙️ Part 2：雲端開箱、鍵盤快捷鍵、台積電 Live Demo 與 Pair Programming (學校第 3 節：10:00 - 10:50)")
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
            * **10:25 - 10:40 ｜ 現場 Live Demo：自然語言 Prompt ➔ 4 行 Python ➔ Shift+Enter 執行**
              * *操作步驟*：
                1. 老師投影大螢幕，打開學生端網頁的「Live Demo 折疊區」。
                2. 念出提示詞（Prompt）：*「請用 yfinance 抓取台積電 2330.TW 過去一年股價並畫圖」*，向同學說明這就是我們跟 AI 溝通的方式。
                3. 點擊代碼右上角「複製」，在另一個分頁打開全新的 Google Colab。
                4. 在 Colab 儲存格按 `Ctrl+V` (或 `Cmd+V`) 貼上。
                5. 雙手離開滑鼠，口頭帶全班一起大聲倒數：「按下 **Shift + Enter**！」
                6. 幾秒後折線圖跳出，全班感受成就感！隨後請全班跟著老師做一次。
            * **10:40 - 10:48 ｜ 商業數據思考、超前快手加碼挑戰 (2 Options) 與任務預告**
              * *全班引導*：連結大一經濟與會計數據，說明為何動態圖表比靜態報表更能看出營運週期。
              * *快手加碼 (Fast-finisher Options)*：針對提早跑完的同學，現場拋出 2 個延伸挑戰：
                * **Option A（改參數）**：把代碼中的 `period="1y"` 改成 `period="5y"`，或把代號改成輝達 `"NVDA"`，觀察全球 AI 晶片浪潮。
                * **Option B（問 AI 商業邏輯）**：切到 Gemini 分頁提問：「請分析台積電過去一年的關鍵成長動能」，體驗代碼結合商業分析。
              * *預告*：第三節每個人都要親自挑戰自己的 Lab 0！
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
            * **10:25 - 10:40 (Step-by-Step Live Demo)**:
              *"Look at the main screen. In our portal, we have the prompt: 'Fetch TSMC 2330.TW for 1 year and plot closing price'. That is all you say to AI!
              Now watch closely: I copy this 4-line code, switch to Google Colab, paste it in with `Ctrl+V`, and without touching the mouse, I press **Shift + Enter**!
              Look at the screen—in 3 seconds, a real financial trend chart appears. Now, open your Colab and do the exact same thing together with me!"*
            * **10:40 - 10:48 (Business Reflection & Fast-Finisher Options)**:
              *"Awesome job seeing your charts pop up! While everyone catches up, here are two quick micro-options for fast finishers:
              - **Option A (Tweak Parameters)**: Change `period='1y'` to `'5y'` to view a 5-year macro trend, or replace `'2330.TW'` with NVIDIA (`'NVDA'`).
              - **Option B (Ask Gemini)**: Switch to your Gemini tab and ask: *'Explain 3 key business factors driving TSMC's stock price over the past year.'*
              In our next session, you will officially customize this code in Lab 0!"*
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
