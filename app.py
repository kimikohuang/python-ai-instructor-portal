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
   💡 Recommended (Optional): A headset with a microphone (for voice interaction).
🎓 Eligibility & Audience: Open to ALL majors, year levels, and graduate/undergraduate students across the university (Local & International students are all warmly welcomed!).
💬 Language & Support Note: Taught primarily in English (ideal for international students), with supplementary Chinese guidance (課程主要以英文講授，並輔以中文說明). If you need support for any specific national language, please feel free to leave a message in the TA section (若有需要增加國家語言，也歡迎在助教區留言).
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
                2. **每週必備設備**：每週帶 **筆電（跑 Colab）** 與 **手機（LINE 與行動 App 成果預覽）**；耳機麥克風建議自備（Optional）。
                3. **三大評量里程碑**：平常實作 50%、第 9 週期中評量 20%、**第 16 週 (12/24) 期末成果發表會 30%**（特別提醒 17-18 週為彈性自主學習）。
                4. **選課對象與語言通融**：全校跨系所、各年級與研究所皆可修；英文講授為主、中文輔助，若需要增加其他國家語言支援，隨時在助教區提出。
                5. **群組暱稱規範**：現場監督全班將暱稱改成「學號末三碼 + 名字」（如：`205 Huy`），這是平時點名加分的依據！
            * **09:15 - 09:25 ｜ 多語系切換與側邊欄 AI 助教演練**
              * *操作重點*：展示點擊越南語、印尼語等多語系切換；展開左側邊欄 **Course AI Assistant**，說明發問拿平時加分與匿名模式。
            * **09:25 - 09:35 ｜ 四大核心卡片、結對專題 (Pair Project) 與指揮家思維**
              * *指揮家思維*：不用死背語法，我們是指揮家，AI 則是演奏樂手，以自然語言 prompt 協同作業。
              * *課堂互動提問（啟發思考）*：
                * 現場邀請 1～2 位同學分享想法：「大家覺得在 AI 時代寫程式，是一個人自己默默做比較好，還是兩個人結對 (Pair) 協作比較好？為什麼？」
                * *老師收攏點評*：一個人單打獨鬥容易陷在思考盲點；兩個人一起，一人負責商業需求與提問邏輯 (Product Owner)，一人把關程式與排版 (Builder)，這種人機＋雙人協作才是企業最需要的模式！
              * *期末專題機制*：採「結對彈性制（原則 2 人，可 1~3 人）」，充分包容、沒有人被孤立。
            * **09:35 - 09:40 ｜ 激勵亮點：展示 Streamlit 網頁力量**
              * *激勵說明*：眼前的課綱與 AI 助教全是老師用純 Python + Streamlit 打造的！第 10-11 週大家也能做出自己的 Web App 發布到手機上。
            * **09:40 - 09:48 ｜ 點開「18 週進度總表」看全學期課程地圖**
              * *操作重點*：展開下方「18-Week Teaching Scripts & Breakdown」，逐週為同學勾勒整學期學習輪廓。
            * **09:48 - 09:50 ｜ 破除恐懼的心態喊話：AI 跨越語言障礙與提問本質**
              * *核心心法*：現代 AI 跨越了語言門檻。最重要的是**「學會提出正確的問題、把商業邏輯定義清楚」**，AI 就是最強大的執行長。
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **09:00 - 09:15 (Ice-breaking & QR Code Scan)**:
              *"Good morning everyone! Welcome to Python AI Applications. Please take out your smartphones right now and scan the two QR codes on the main screen: one for our syllabus portal, and one for our official LINE group chat.
              Let's quickly review our key rules:
              1. Classroom: Room 506, Innovation Building.
              2. Required devices: Laptop for cloud coding, smartphone for mobile preview. Headsets are optional but recommended.
              3. Grading: 50% weekly practice, 20% midterm, 30% final showcase in Week 16.
              4. Open Eligibility: Open to all majors, levels, and graduate students. Local and international students are both warmly welcomed!
              5. LINE Nickname rule: Please rename yourself using 'Last 3 digits + Name', like '205 Huy'."*
            * **09:15 - 09:25 (Multilingual Portal Tour)**:
              *"Look at the top of our web portal. You can switch between 7 languages instantly using the flag buttons. Whether you prefer English, Vietnamese, Indonesian, or Traditional Chinese, you have full parallel support! Also, check out our sidebar AI Assistant for real-time Q&A."*
            * **09:25 - 09:35 (Conductor Mindset, Interactive Discussion & Pair Teams)**:
              *"Review our core cards on screen. Adopt the **Conductor Mindset**: AI is your orchestra, and you lead it using natural language prompts without memorizing syntax.
              Before we talk about teams, let me ask: *'In the era of AI, do you think it is more powerful to code alone, or to collaborate in pairs? Any thoughts?'*
              (Invite 1-2 students to share briefly)
              *Exactly! When coding alone, you can easily get tunnel vision with your prompts. In a pair, one acts as the Product Owner focusing on business logic, while the other inspects the code and UI. Two human minds leading one AI create the best results!*
              For our Final Showcase, we encourage **Pair Projects (teams of 1-3)** so that no one is left behind."*
            * **09:35 - 09:40 (Portal Showcase)**:
              *"Take a look at this portal you are viewing right now—it was built entirely by me using Python and Streamlit! You will learn to build your own web apps just like this and deploy them to your phone by Week 10."*
            * **09:40 - 09:48 (18-Week Roadmap)**:
              *"Let's check our 18-week roadmap: from TSMC data engineering and FRED macro data, all the way to our final showcase in Week 16."*
            * **09:48 - 09:50 (Mindset Hype: AI Crosses Language Barriers)**:
              *"Remember: **AI has completely crossed the language barrier.** The most valuable skill in the AI era is **knowing how to ask the right questions and defining your problems clearly.** Speak your mind, and let AI handle the heavy lifting!"*
            """)

        # ----------------------------------------------------------------------
        # 18 週逐週口播備忘稿完整模組
        # ----------------------------------------------------------------------
        with st.expander("🗓️ 18-Week Teaching Scripts & Breakdown (18週進度逐週講稿備忘)", expanded=False):
            st.caption("💡 課堂導覽大表格時，可逐週點擊對照中英文口播台詞與作業摘要：")
            
            scripts_18w = [
                {
                    "week": "Week 1", "topic": "Course Onboarding & Vibe Coding",
                    "en_prog": "We kick off with the Conductor Mindset—learning how to direct AI using natural language prompts without memorizing syntax.",
                    "zh_prog": "建立指揮家思維，以自然語言提示詞引導 AI，零語法負擔無痛入門。",
                    "en_lab": "Lab 0: In-class fun exploration — Complete a hands-on Colab notebook and submit digital check-in.",
                    "zh_lab": "Lab 0: 課堂趣味實作探索 — 完成 Colab 筆記本並透過側邊欄打卡記錄出勤。",
                    "en_sum": "A stress-free introduction to Google Colab, basic workflow, and prompt-driven programming.",
                    "zh_sum": "Google Colab 雲端環境建置與無痛程式初體驗。"
                },
                {
                    "week": "Week 2", "topic": "Market Data Engineering: Apple & TSMC",
                    "en_prog": "During this add/drop period, we fetch real-world stock market data for giants like Apple and TSMC using Python.",
                    "zh_prog": "加退選期間，運用 Python 串接蘋果與台積電真實歷史行情。",
                    "en_lab": "In-class live practice — Follow along to pull raw numbers into DataFrames and plot your first price chart.",
                    "zh_lab": "課堂即時實作與練習 — 跟隨課堂示範整理行情表格並繪製走勢圖。",
                    "en_sum": "Hands-on data ingestion and visual trend plotting designed to onboard newcomers gently.",
                    "zh_sum": "友善入門的資料擷取與基礎視覺化工程。"
                },
                {
                    "week": "Week 3", "topic": "Global EV Trends: Tesla vs. Worldwide Market Leaders",
                    "en_prog": "With our roster finalized, we compare global EV pioneers like Tesla against international supply chain leaders.",
                    "zh_prog": "正式名單確定，聚焦特斯拉與全球電動車供應鏈龍頭對比。",
                    "en_lab": "Lab 1: EV market trends notebook — Calculate daily percentage returns and basic risk indicators.",
                    "zh_lab": "Lab 1: 電動車市場趨勢筆記本 — 計算各車廠日報酬率與簡易波動風險。",
                    "en_sum": "Connecting corporate competitive strategy with empirical market return calculations.",
                    "zh_sum": "結合商業競爭策略與實質資產報酬運算。"
                },
                {
                    "week": "Week 4", "topic": "Quantitative Trading Strategies",
                    "en_prog": "We explore rule-based trading concepts, specifically Moving Average crossovers like the 20MA and 60MA.",
                    "zh_prog": "探討量化規則交易，以 20MA 與 60MA 均線交叉為核心策略。",
                    "en_lab": "Lab 2: Moving average strategy report — Backtest a classic strategy against Buy & Hold.",
                    "zh_lab": "Lab 2: 移動平均線策略報告 — 評估交易策略相較於長期持有的績效與安全性。",
                    "en_sum": "Evaluating algorithmic performance, trade safety, and annualized risk metrics.",
                    "zh_sum": "透過量化數據客觀評估交易法則與安全界限。"
                },
                {
                    "week": "Week 5", "topic": "Macro Economy & Global Currencies",
                    "en_prog": "We bridge economics to code by connecting directly to the Federal Reserve's FRED database.",
                    "zh_prog": "串接聖路易斯聯準會 FRED 資料庫，將總體經濟指標實體化。",
                    "en_lab": "Lab 3: Economic trends & FX report — Extract interest rate benchmarks, inflation, and FX rates.",
                    "zh_lab": "Lab 3: 總經趨勢與匯率觀測報告 — 分析基準利率、通膨走勢與匯率連動。",
                    "en_sum": "Understanding how central bank policies and macroeconomic shifts influence global markets.",
                    "zh_sum": "剖析央行貨幣政策與匯率波動對跨國市場的實質衝擊。"
                },
                {
                    "week": "Week 6", "topic": "Corporate Health & Global Industry Champions",
                    "en_prog": "We dive into fundamental analysis, reading balance sheets and income statements of industry leaders.",
                    "zh_prog": "進入基本面分析，解析各領域龍頭企業的公開資產負債與損益表。",
                    "en_lab": "Lab 4: Automated company health tool — Automate calculations for DuPont ROE and debt ratios.",
                    "zh_lab": "Lab 4: 自動化企業健康診斷工具 — 開發自動化健檢工具，計算杜邦指標與財務槓桿。",
                    "en_sum": "Transforming accounting principles into an automated financial diagnostic pipeline.",
                    "zh_sum": "將大一會計基礎轉化為程式化財務健康評估系統。"
                },
                {
                    "week": "Week 7", "topic": "Google AI Studio: Virtual Analyst",
                    "en_prog": "We harness Google AI Studio to define system instructions and architect a specialized business copilot.",
                    "zh_prog": "操作 Google AI Studio，設定系統角色指令，打造專屬虛擬分析師。",
                    "en_lab": "Lab 5: AI prompt tuning practice — Tune prompts that turn messy corporate filings into sharp briefings.",
                    "zh_lab": "Lab 5: AI 提示詞微調實作練習 — 讓 AI 自動摘要商業新聞與公告重點。",
                    "en_sum": "Mastering system persona configuration and structured output engineering.",
                    "zh_sum": "掌握系統角色指引與結構化商業輸出技巧。"
                },
                {
                    "week": "Week 8", "topic": "Multilingual News Sentiment",
                    "en_prog": "We integrate the Gemini API to analyze market sentiment across global multilingual news headlines.",
                    "zh_prog": "串接 Gemini API，即時解析多國語系財經新聞的市場多空情緒。",
                    "en_lab": "Lab 6: Market sentiment dashboard — Classify news commentary into sentiment scores.",
                    "zh_lab": "Lab 6: 市場情緒即時監控儀表板 — 建構即時新聞情緒監控分類看板。",
                    "en_sum": "Quantifying market sentiment and public opinion through modern multimodal LLMs.",
                    "zh_sum": "運用大型語言模型將市場新聞量化為客觀情緒指標。"
                },
                {
                    "week": "Week 9", "topic": "Midterm Examination Week",
                    "en_prog": "Official Midterm Week: We conduct our hands-on in-class practical review.",
                    "zh_prog": "期中評量週：進行上機核心實務總複習與實測。",
                    "en_lab": "Midterm Practical Review — Demonstrate financial calculations and core AI prompts (20%).",
                    "zh_lab": "期中上機實務總複習與評量 — 上機評量核心程式撰寫與 AI 提示詞操作，佔 20%。",
                    "en_sum": "Consolidating all prompt engineering and data extraction fundamentals learned so far.",
                    "zh_sum": "全面驗證前半學期的資料工程與提示詞指揮能力。"
                },
                {
                    "week": "Week 10", "topic": "Interactive Web Apps with Streamlit",
                    "en_prog": "We turn standalone Python scripts into live interactive web applications using Streamlit.",
                    "zh_prog": "使用 Streamlit 將資料分析腳本封裝為互動式 Web 應用。",
                    "en_lab": "Lab 7: Web app interface script — Assemble an interface with dropdowns, sliders, and buttons.",
                    "zh_lab": "Lab 7: 互動網頁介面開發腳本 — 加入下拉選單、數值滑桿與互動按鈕。",
                    "en_sum": "Bridging back-end data logic to front-end interactive UI design effortlessly.",
                    "zh_sum": "無縫串接後端運算邏輯與前端網頁互動介面。"
                },
                {
                    "week": "Week 11", "topic": "Cloud Deployment & Mobile UI",
                    "en_prog": "We publish our Streamlit apps to the cloud for free, optimizing the layout specifically for smartphones.",
                    "zh_prog": "將應用程式發布至雲端永久運行，並針對手機端進行排版優化。",
                    "en_lab": "Lab 8: Deploy app to the web — Deploy your app live and test responsive layouts on your phone.",
                    "zh_lab": "Lab 8: 雲端 Web 應用正式發布上線 — 完成上線發布並使用個人手機實機驗證。",
                    "en_sum": "Making your software instantly accessible to anyone, anywhere via a web link.",
                    "zh_sum": "掌握無伺服器雲端快速部署與跨裝置無障礙發布流程。"
                },
                {
                    "week": "Week 12", "topic": "Earnings Call & Annual Report Reader",
                    "en_prog": "We direct AI to digest dense quarterly earnings transcripts and 10-K filings.",
                    "zh_prog": "指揮 AI 深度解析企業法說會逐字稿與季度財報檔案。",
                    "en_lab": "Lab 9: Automated risk summary report — Extract corporate risk factors and catalyst highlights.",
                    "zh_lab": "Lab 9: 自動化企業風險摘要報告 — 一鍵提取財報中的潛在營運風險與成長動能。",
                    "en_sum": "Accelerating qualitative fundamental research using automated document intelligence.",
                    "zh_sum": "利用生成式文件智慧大幅縮減專業財報研讀時間。"
                },
                {
                    "week": "Week 13", "topic": "Multimodal AI: Smart Receipt Scanner",
                    "en_prog": "We deploy Gemini Vision to parse image-based financial receipts, invoices, and physical records.",
                    "zh_prog": "運用 Gemini Vision 影像多模態模型辨識單據、發票與出入庫憑證。",
                    "en_lab": "Lab 10: Receipt scanner project — Upload receipt photos and generate journal entries automatically.",
                    "zh_lab": "Lab 10: 智慧單據辨識專題 — 拍照上傳單據並自動轉換為標準會計分錄。",
                    "en_sum": "Merging computer vision and enterprise accounting workflows seamlessly.",
                    "zh_sum": "融合電腦視覺技術與企業日常會計記帳流程。"
                },
                {
                    "week": "Week 14", "topic": "Dynamic Charts: Interactive Visuals",
                    "en_prog": "We level up our visuals by crafting professional interactive candlestick charts.",
                    "zh_prog": "進階動態視覺化實作，打造高階互動式 K 線圖表。",
                    "en_lab": "Project Sprint: Pro candlestick charts — Implement zoomable price candles and hover tooltips.",
                    "zh_lab": "專案衝刺：專業動態 K 線圖表 — 加入動態縮放、數值浮動卡與成交量疊加。",
                    "en_sum": "Polishing the user experience and visual depth of your project interface.",
                    "zh_sum": "強化期末專案在手機與網頁端的資訊深度與視覺質感。"
                },
                {
                    "week": "Week 15", "topic": "AI Ethics, Data Privacy & Security",
                    "en_prog": "We cover essential industry standards: digital ethics, prompt injection defense, and API key management.",
                    "zh_prog": "講授企業級資安防護：提示詞注入防禦、API 金鑰隔離與數位隱私。",
                    "en_lab": "Lab 11: Prompt defense & key safety — Audit your app to hide API credentials in cloud secrets.",
                    "zh_lab": "Lab 11: 提示詞防禦與金鑰資安實作 — 將私密金鑰移入雲端環境變數中保護。",
                    "en_sum": "Ensuring your deployed business tools are compliant, reliable, and production-safe.",
                    "zh_sum": "確保對外發布的 Web 應用符合資訊安全與合規準則。"
                },
                {
                    "week": "Week 16", "topic": "Final Project Showcase",
                    "en_prog": "The grand finale: Our in-class Live Web App Demonstration and peer feedback session.",
                    "zh_prog": "重頭戲登場：課堂現場專題成果發表與同儕互動觀摩。",
                    "en_lab": "Final Deliverable: Live Web App — Pitch and demonstrate your app live to the room (30%).",
                    "zh_lab": "期末交付成果：上線運作 Web App — 上台展示可點擊運作的雲端 Web 應用實機，佔 30%。",
                    "en_sum": "Celebrating the transition from AI beginners to fully functional tool creators.",
                    "zh_sum": "展現一學期跨領域學習成果，將商業洞察化為實用工具。"
                },
                {
                    "week": "Week 17", "topic": "Independent Study: FinTech Multimedia",
                    "en_prog": "In accordance with school policy, this week is dedicated to self-directed, flexible learning.",
                    "zh_prog": "依學校彈性自主學習規範，同學自主安排線上學習活動。",
                    "en_lab": "Independent project enhancement — Review video materials and polish your project code or UI.",
                    "zh_lab": "自主專案程式優化與精進 — 觀看 FinTech 業界多媒體教學，持續精進應用架構。",
                    "en_sum": "Autonomous learning focused on advanced engineering tutorials and UI polish.",
                    "zh_sum": "自主強化專案細節與進階工程技術探索。"
                },
                {
                    "week": "Week 18", "topic": "Independent Study: Case Studies & Portfolio",
                    "en_prog": "The final stage of self-directed study: Reflecting on broader AI enterprise implementations.",
                    "zh_prog": "自主學習第二週：研讀國際 AI 商業落地案例並自我回顧。",
                    "en_lab": "Final portfolio submission — Assemble and submit your complete semester learning portfolio.",
                    "zh_lab": "學期學習歷程檔案最終交付 — 整理個人專案成果與 GitHub 連結，完成學期總繳交。",
                    "en_sum": "Consolidating your semester accomplishments into a permanent professional portfolio.",
                    "zh_sum": "將全學期 18 週實作歷程轉化為求職與升學的數位成果作品集。"
                }
            ]
            
            for item in scripts_18w:
                with st.expander(f"📍 {item['week']}: {item['topic']}", expanded=False):
                    col_l, col_r = st.columns(2)
                    with col_l:
                        st.markdown("**🇹🇼 中文授課導引與要點：**")
                        st.markdown(f"- **教學進度**：{item['zh_prog']}")
                        st.markdown(f"- **作業實作**：{item['zh_lab']}")
                        st.markdown(f"- **本週摘要**：{item['zh_sum']}")
                    with col_r:
                        st.markdown("**🇺🇸 English Teaching Scripts:**")
                        st.markdown(f"- **Progress**: *\"{item['en_prog']}\"*")
                        st.markdown(f"- **Lab / HW**: *\"{item['en_lab']}\"*")
                        st.markdown(f"- **Summary**: *\"{item['en_sum']}\"*")

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
              * *黑科技分享（語音輸入）*：引導同學示範用「嘴巴說」來代替打字。介紹 **透通式耳機 (Transparency Earphones)** 的好處——戴著它可以跟 Gemini 語音對話（小聲說微氣音 Micro-whisper），同時又能聽見老師講課與同伴討論！
              * *鍵盤暖身*：帶大家複習 Windows (`Ctrl`) 與 Mac (`Cmd ⌘`) 的核心捷徑：
                * 複製 `Ctrl/Cmd + C`、貼上 `Ctrl/Cmd + V`、剪下 `Ctrl/Cmd + X`
                * **救命鍵（復原）**：`Ctrl/Cmd + Z`（代碼改壞時一鍵還原）
                * **Colab 執行神鍵**：`Shift + Enter`（免按滑鼠直接跑程式）
              * *Pair Programming*：若沒帶電腦，兩人一組結對協作。
            * **10:15 - 10:25 ｜ 雙軌 AI 互補機制說明 (Colab + Gemini)**
              * *引導說明*：開另一個分頁放 Google Gemini，遇報錯時複製貼到 Gemini 提問。
            * **10:25 - 10:40 ｜ 現場 Live Demo：自然語言 Prompt ➔ 4 行 Python ➔ Shift+Enter 執行**
              * *操作步驟*：念出提示詞 ➔ 複製 ➔ 貼到 Colab ➔ 按下 `Shift + Enter` ➔ 呈現折線圖。
            * **10:40 - 10:48 ｜ 商業數據思考、【課堂互動提問：台積電與經濟學】與快手加碼**
              * *課堂提問*：台積電飆升反映了生成式 AI 帶來的巨大需求衝擊（Demand Shock）。
              * *快手加碼*：改參數（`period="5y"`）或問 Gemini 分析台積電成長動能。
            * **10:48 - 10:50 ｜ 課間緩衝與連線疑難排解**
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **10:00 - 10:15 (Cloud Setup, Transparency Earphones & Voice Prompting)**:
              *"Welcome back! If you have **transparency-mode earphones**, wear them now! You can micro-whisper your prompts directly to Gemini without typing, while still hearing my lecture and your partner's ideas clearly.
              Now let's review our core shortcuts: `Ctrl/Cmd + C` (Copy), `Ctrl/Cmd + V` (Paste), `Ctrl/Cmd + Z` (Undo), and `Shift + Enter` (Run Cell)."*
            * **10:15 - 10:25**: *"Keep a separate tab open for **Google Gemini** as our backup assistant."*
            * **10:25 - 10:40 (Step-by-Step Live Demo)**:
              *"Watch closely: I copy this 4-line script, switch to Google Colab, paste it in, and press **Shift + Enter**! Look at the screen—a real financial chart appears in 3 seconds!"*
            * **10:40 - 10:48 (Economics Reflection & Fast-Finisher Options)**:
              *"Connecting back to freshman Economics: this rally reflects an unprecedented AI demand shock. Fast teams: tweak `period='1y'` to `'5y'` to view the multi-year cycle!"*
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
              * *任務發布 (Lab 0)*：將代碼中的台積電改為蘋果 (`AAPL`) 或星巴克 (`SBUX`)。
              * *除錯 SOP*：選取紅字 ➔ 複製 ➔ 貼到 Gemini 詢問修復代碼。
            * **11:15 - 11:30 ｜ 課堂巡視、個別排解與參與記錄**
              * 協助排解問題；跑出圖表即完成 Lab 0 初體驗。
            * **11:30 - 11:40 ｜ 【課堂互動提問：會計營收結構】與快手加碼 (TSMC vs. Apple)**
              * *課堂提問*：比較台積電 B2B 晶圓代工與蘋果/星巴克 B2C 消費終端的營收本質差異。
            * **11:40 - 11:50 ｜ 首日總結、側邊欄打卡繳交與 Office Hours**
              * 提醒同學下課前在 **Course AI Assistant** 輸入學號與心得打卡。
              * 提醒課程不限系所與年級，歡迎轉發給朋友在加退選期間選修。
            """)
            
        with col_b:
            st.markdown("#### 🗣️ English Teaching Scripts")
            st.info("""
            * **11:00 - 11:15 (Lab 0 Mission & Error Recovery)**:
              *"Now it's time for **Lab 0**! Customize the script: replace TSMC with Apple (`'AAPL'`) or Starbucks (`'SBUX'`). If you hit an error, copy the red text, paste it into Gemini, and ask it to fix the bug!"*
            * **11:15 - 11:30 (Hands-on Walkthrough)**:
              *(Walking around)* *"Fantastic charts! Drop any questions in our Course AI Assistant in the sidebar to earn bonus participation points."*
            * **11:30 - 11:40 (Interactive Q&A: Accounting & Business Models)**:
              *"Why do B2B firms like TSMC behave so differently from B2C brands in their revenue models? One sells computing infrastructure, while the other faces direct consumer spending!"*
            * **11:40 - 11:50 (Wrap-up, Sidebar Check-in & Office Hours)**:
              *"Congratulations! You officially ran your first cloud Python program today.
              Before you leave, **submit your Lab 0 check-in** via the **Sidebar AI Assistant**.
              Remember this course is open to **ALL majors across the university**—invite your friends during add/drop week!
              I will be right here in Room 506 after class. Have a wonderful week!"*
            """)

else:
    st.info(f"🚧 **{selected_week} 教師專屬講稿與提示** 蓄勢待發中！")
