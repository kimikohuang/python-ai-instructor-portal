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
              * *指揮家思維*：不用死背語法，我們是指揮家，AI 則是演奏樂手，以自然語言 prompt 協同作業。
              * *課堂互動提問（啟發思考）*：
                * 現場邀請 1～2 位同學分享想法：「大家覺得在 AI 時代寫程式，是一個人自己默默做比較好，還是兩個人結對 (Pair) 協作比較好？為什麼？」
                * *老師收攏點評*：一個人單打獨鬥時，常常會陷入提示詞 (Prompt) 的思考盲點，或被一個小小符號卡住；兩個人一起，一人負責商業需求與提問邏輯 (Product Owner)，一人把關程式與介面排版 (Builder)，這種人機＋雙人協作才是企業最需要的模式！
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
            * **09:48 - 09:50 ｜ 破除恐懼的心態喊話：AI 跨越語言障礙與提問本質**
              * *精神喊話*：告訴同學現代 AI 的語音辨識與自然語言處理已經跨越了語言門檻。無論用越南語、泰語、法語或印尼語，用母語語音輸入效果都極佳。
              * *核心心法*：在 AI 時代「不需要比打字快、不需要死背語法」。最重要的是**「學會提出正確的問題、把商業邏輯定義清楚」**。用最熟悉的方式把想法說出來，AI 就是最強大的技術執行長。
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **09:00 - 09:15 (Ice-breaking & QR Code Scan)**:
              *"Good morning everyone! Welcome to Python AI Applications. Please take out your smartphones right now and scan the two QR codes on the main screen: one for our syllabus portal, and one for our official LINE group chat.
              Let's quickly review our 4 key rules on LINE:
              1. Classroom: Room 506, Innovation Building.
              2. Required devices: Laptop for cloud coding, smartphone for mobile preview.
              3. Grading: 50% weekly practice, 20% midterm, 30% final showcase in Week 16.
              4. LINE Nickname rule: Please rename yourself using 'Last 3 digits + Name', like '205 Huy'."*
            * **09:15 - 09:25 (Multilingual Portal Tour)**:
              *"Look at the top of our web portal. You can switch between 7 languages instantly using the flag buttons. Whether you prefer English, Vietnamese, Indonesian, or Traditional Chinese, you have full parallel support!"*
            * **09:25 - 09:35 (Conductor Mindset, Interactive Discussion & Pair Teams)**:
              *"Review our core cards on screen. Adopt the **Conductor Mindset**: AI is your orchestra, and you lead it using natural language prompts without memorizing syntax.
              Before we talk about teams, let me ask: *'In the era of AI, do you think it is more powerful to code alone, or to collaborate in pairs? Any thoughts?'*
              (Invite 1-2 students to share briefly)
              *Exactly! When coding alone, you can easily get tunnel vision with your prompts. In a pair, one acts as the Product Owner focusing on business logic, while the other inspects the code and UI. Two human minds leading one AI create the best results!*
              That's why our grading is: 50% weekly practice, 20% midterm in Week 9, and 30% Final Showcase in Week 16.
              For our Final Showcase, we encourage **Pair Projects (teams of 2)**. To ensure everyone feels supported and no one is left behind, teams are flexible: you may work **individually (1 person)**, as a **pair (2 people)**, or form a group of **3 people maximum** if there's an odd number.
              In Week 15, right before Demo Day, our 3rd session will be a hands-on project clinic and rehearsal to ensure your app is secure and ready!"*
            * **09:35 - 09:50 (Portal Showcase & Mindset Hype)**:
              *"Take a look at this portal you are viewing right now—it was built entirely by me using Python and Streamlit! You will learn to build your own web apps just like this by Week 10.
              Before we take a short break and open our laptops for Session 2, remember: **AI has completely crossed the language barrier.** 
              Whether your native language is Vietnamese, Thai, French, or Indonesian, modern AI understands your voice effortlessly. 
              **You do not need to fear coding anymore.** The most valuable skill in the AI era is **knowing how to ask the right questions and defining your problems clearly.** 
              Speak your mind, and let AI handle the heavy lifting!"*
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
            * **10:00 - 10:15 ｜ 雲端環境開箱、透通式耳機、AI 語音輸入密技與 Pair Programming**
              * *黑科技分享（語音輸入）*：引導同學示範用「嘴巴說」來代替打字。介紹 **透通式耳機 (Transparency Earphones)** 的好處——戴著它可以跟 Gemini 語音對話（小聲說微氣音 Micro-whisper），同時又能聽見老師講課與隔壁戰友的討論，實現最高效的人機協作！
              * *鍵盤暖身*：說明打字與快捷鍵是跟 AI 高效溝通的超能力。帶大家複習 Windows (`Ctrl`) 與 Mac (`Cmd ⌘`) 的核心捷徑：
                * 複製 `Ctrl/Cmd + C`、貼上 `Ctrl/Cmd + V`、剪下 `Ctrl/Cmd + X`
                * **救命鍵（復原）**：`Ctrl/Cmd + Z`（代碼改壞或刪掉時一鍵還原）
                * **Colab 執行神鍵**：`Shift + Enter`（免按滑鼠，一鍵跑程式）
              * *Pair Programming*：若沒帶電腦，兩人一組結對協作，共同下提示詞與除錯。
            * **10:15 - 10:25 ｜ 雙軌 AI 互補機制說明 (Colab + Gemini)**
              * *引導說明*：開另一個分頁放 Google Gemini。Colab 內建 AI 額度用完或遇到複雜報錯時，用快捷鍵 `Ctrl/Cmd + C` 複製貼到 Gemini，確保實作不中斷。
            * **10:25 - 10:40 ｜ 現場 Live Demo：自然語言 Prompt ➔ 4 行 Python ➔ Shift+Enter 執行**
              * *操作步驟*：
                1. 老師投影大螢幕，打開學生端網頁的錄影或「Live Demo 折疊區」。
                2. 念出提示詞（Prompt）：*「請用 yfinance 抓取台積電 2330.TW 過去一年股價並畫圖」*，向同學說明這就是我們跟 AI 溝通的方式。
                3. 點擊代碼右上角錄影「複製」，在另一個分頁打開全新的 Google Colab。
                4. 在 Colab 儲存格按 `Ctrl+V` (或 `Cmd+V`) 貼上。
                5. 雙手離開滑鼠，口頭帶全班一起大聲倒數：「按下 **Shift + Enter**！」
                6. 幾秒後折線圖跳出，全班感受成就感！隨後請全班跟著老師做一次。
            * **10:40 - 10:48 ｜ 商業數據思考、【課堂互動提問：台積電與經濟學】與快手加碼**
              * *課堂互動提問（啟發思考）*：
                * 指著大螢幕上台積電一路飆升的走勢問全班：「看到這條曲線，如果用大家在大一【經濟學】學過的供需理論或景氣循環，背後反映了什麼全球商業訊號？」
                * *老師收攏點評*：生成式 AI 爆發帶來了全球對頂尖算力的巨大需求衝擊（Demand Shock），供不應求讓晶圓代工龍頭直接受惠。圖表不只是程式畫出來的線，而是真實資本市場的經濟脈動！
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
            * **10:00 - 10:15 (Cloud Setup, Transparency Earphones & Voice Prompting)**:
              *"Welcome back! Before we code, let's unlock the ultimate AI productivity hack: **Voice Prompting**. 
              If you have **transparency-mode earphones**, wear them now! You can micro-whisper your prompts directly to Gemini without typing, saving tons of time, while still hearing my lecture and your partner's ideas clearly.
              Now let's review our core keyboard shortcuts:
              - **Copy / Paste**: `Ctrl + C` / `Ctrl + V` on Windows, or `Cmd ⌘ + C` / `Cmd ⌘ + V` on Mac.
              - **The Life Saver (Undo)**: `Ctrl + Z` or `Cmd ⌘ + Z` if you accidentally delete code!
              - **Colab Instant Run**: Press `Shift + Enter` to run any code cell instantly.
              If you don't have a laptop today, pair up with the classmate next to you for **Pair Programming**."*
            * **10:15 - 10:25**: *"Keep a separate tab open for **Google Gemini**. When Colab's AI hits its usage quota, copy your code with `Ctrl+C` and paste into Gemini with `Ctrl+V`!"*
            * **10:25 - 10:40 (Step-by-Step Live Demo)**:
              *"Look at the main screen. In our portal, we have the prompt: 'Fetch TSMC 2330.TW for 1 year and plot closing price'. That is all you say to AI!
              Now watch closely: I copy this 4-line code, switch to Google Colab, paste it in with `Ctrl+V`, and without touching the mouse, I press **Shift + Enter**!
              Look at the screen—in 3 seconds, a real financial trend chart appears. Now, open your Colab and do the exact same thing together with me!"*
            * **10:40 - 10:48 (Economics Reflection, Interactive Q&A & Fast-Finisher Options)**:
              *"Look at this soaring curve of TSMC. Connecting back to your freshman Economics: what market signals or supply-and-demand shifts explain this massive rally?
              (Encourage 1-2 hands)
              Spot on! Generative AI created an unprecedented demand shock for computing power.
              For fast teams: tweak `period='1y'` to `'5y'` to view the multi-year cycle, or ask Gemini to outline 3 macro catalysts behind this chart!"*
            * **10:48 - 10:50**: *"Take a short break. Any Wi-Fi issues, come to the front desk now!"*
            """)

    # --------------------------------------------------------------------------
    # TAB 3: 第三節課（11:00 - 11:50）
    # --------------------------------------------------------------------------
    with tab3:
        st.subheader("🎙️ Part 3：Lab 0 動手實作、雙軌 AI 除錯與首週成就收尾 (學校第 4 節：11:00 - 11:50)")
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("#### ⏱️ 時間軸與中文授課導引")
            st.markdown("""
            * **11:00 - 11:15 ｜ Lab 0 實作發布與標準 AI 除錯流程**
              * *任務發布 (Lab 0)*：
                1. 每組在自己的 Colab 建立新 Notebook。
                2. 將代碼中的台積電 (`2330.TW`) 改為蘋果 (`AAPL`) 或自選知名企業（如星巴克 `SBUX`、微軟 `MSFT`）。
              * *除錯演練 (SOP)*：提醒同學若遇到紅色報錯，不用驚慌，三步驟除錯：
                * 選取紅字 ➔ `Ctrl/Cmd + C` 複製 ➔ 切換至 Gemini 貼上詢問：「請修正此錯誤並給我正確代碼」。
            * **11:15 - 11:30 ｜ 課堂巡視、個別排解與參與記錄**
              * *走動指導*：協助排解 Wi-Fi 斷線或括號遺漏問題；觀察 Pair Programming 兩人的分工互動。
              * *課堂參與*：跑出圖表即代表完成 Lab 0 初體驗，鼓勵透過網站側邊欄 AI 助教提出心得或問題換取加分。
            * **11:30 - 11:40 ｜ 【課堂互動提問：會計營收結構】與快手加碼 (TSMC vs. Apple)**
              * *課堂互動提問（啟發思考）*：
                * 現場邀請換成蘋果 (`AAPL`) 或星巴克 (`SBUX`) 的同學抬頭分享：「誰的走勢圖跟台積電長得截然不同？從大家學過的【會計與商業模式】來看，B2B 晶圓代工與 B2C 消費終端的營收結構有何本質差異？」
                * *老師收攏點評*：台積電是賣武器給淘金客的企業（B2B 資本支出），受惠於雲端與科技巨頭的算力建置；而消費品直接面對一般大眾（B2C 消費支出），會受通膨與大眾消費意願牽動。圖表不只是程式，更是企業會計與獲利體質的鏡子！
              * *快手加碼 (Bonus Challenge)*：
                * 引導進度超前的同學向 AI 下進階 Prompt：「如何用 Python 同時繪製 TSMC 與 Apple 過去一年的走勢對比？」，體驗多資產比較的視覺威力。
            * **11:40 - 11:50 ｜ 首日總結、側邊欄打卡繳交與 Office Hours**
              * *肯定成果*：恭喜全班在第一天就成功使用自然語言跑出雲端數據圖表。
              * *側邊欄打卡叮嚀*：提醒同學下課前務必在網頁左側的 **Course AI Assistant（AI 助教欄位）** 輸入學號與今日跑出的股票心得（例如 AAPL / SBUX），作為今日出勤與 Lab 0 完成的平時成績依據。
              * *選修說明*：提醒同學們本課程不限系所與年級，歡迎將網頁轉發給其他想學 AI 的外系好朋友一起來加退選。
              * *下課諮詢*：老師留在 506 教室接受個別諮詢。
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **11:00 - 11:15 (Lab 0 Mission & Error Recovery)**:
              *"Now it's time for **Lab 0**! In your Colab notebook, take the 4-line script and customize it: replace TSMC (`'2330.TW'`) with Apple (`'AAPL'`) or any global brand you like, such as Starbucks (`'SBUX'`).
              If you see a scary red error message, follow our 3-step reflex:
              1. Copy the red text with `Ctrl/Cmd + C`.
              2. Switch to Gemini and paste with `Ctrl/Cmd + V`.
              3. Ask: *'Fix this error and give me working code.'* Never worry about bugs—AI has your back!"*
            * **11:15 - 11:30 (Hands-on Walkthrough)**:
              *(Walking around)* *"Fantastic charts! Look at those prices updating in real time. If you have questions or want bonus engagement points, drop a question in our Course AI Assistant in the sidebar."*
            * **11:30 - 11:40 (Interactive Q&A: Accounting & Business Models)**:
              *"Who changed their ticker to Apple or Starbucks? Does your trend look very different from TSMC? Connecting to Accounting: *'Why do B2B infrastructure firms behave so differently from B2C consumer giants in their revenue models?'*
              (Invite a student to share briefly)
              *Brilliant observation! TSMC sells the infrastructure to enterprises (B2B capex), whereas consumer brands depend directly on consumer sentiment and inflation (B2C). Our charts are the living reflection of corporate financial realities!*
              For teams who already finished: ask Gemini: *'How can I plot both TSMC and Apple on the same chart using yfinance?'* See if you can visualize who outperformed over the past 12 months!"*
            * **11:40 - 11:50 (Wrap-up, Sidebar Check-in & Office Hours)**:
              *"Big round of applause to everyone! You officially ran your first cloud Python program today without getting stuck in syntax.
              Before you leave, **please submit your Lab 0 check-in** via the **Sidebar AI Assistant** on our portal by typing your student ID and stock ticker insight. This records your attendance and practical milestone!
              Also, remember that this course is open to **ALL majors and year levels across the university**—feel free to share our syllabus portal with friends from other departments during the add/drop week.
              I will be right here in Room 506 after class. Have a wonderful week!"*
            """)

else:
    st.info(f"🚧 **{selected_week} 教師專屬講稿與提示** 蓄勢待發中！")
