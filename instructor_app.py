# ==============================================================================
# [Script] Instructor-Side Secure Script & Teaching Prompt Portal
# 【教師專屬】加密講稿與課堂提示管理系統
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
st.caption("🎯 建議使用平板或第二台筆電開啟此頁面，作為上課時的口頭提示、時間掌控與互動金句備忘錄。")

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
        st.subheader("🎙️ 第一節：破冰、課程總覽與心態建立")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### 📝 口頭講稿與核心觀念")
            st.markdown("""
            * **消除焦慮**：先切換大螢幕的學生端網頁到越文與印尼文，告訴台下外籍同學：「這門課不需要程式底子，只要會問問題，就能跟我一起創造 AI 應用。」
            * **介紹「指揮家思維 (Conductor Mindset)」**：
              > *「過去學程式要記住所有艱澀的語法（Syntax），就像我們要自己學會彈奏每一顆音符；但在 AI 時代，我們扮演的是『交響樂團指揮家』。你不需要會拉小提琴，但你要知道你想聽什麼樂章、如何精準地下達指令給 AI（Claude / ChatGPT / Gemini）。」*
            * **說明評量方式**：強調每週課堂實作佔 50%，鼓勵大家不用怕犯錯，手把手跟著做就一定能過關。
            """)
        with col_b:
            st.markdown("#### ⚡ 現場操作與互動提示")
            st.warning("""
            * **黑板板書重點**：
              1. 課程名稱：Python AI Applications
              2. 老師姓名：黃可羣 (Kimiko)
              3. 核心精神：Conductor Mindset
            * **檢查點**：注意觀察班上外籍生（尤其是越南及印尼籍同學）的表情，確保他們聽得懂英文說明。
            """)
            
    with tab2:
        st.subheader("🎙️ 第二節：雲環境開箱與 LINE 社群 QR Code 導引")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### 📝 口頭講稿與工具介紹")
            st.markdown("""
            * **掃描 QR Code**：請同學拿出手機掃描大螢幕右側的 LINE QR Code 加入社群。
            * **再次強調 LINE 暱稱規範**：
              > *「請大家加入後立刻把名字改為：**學號末三碼 + 名字**（例如：`205 Huy`）。這樣老師在計算平時參與加分時才找得到人喔！」*
            * **雲端開發環境 (Google Colab)**：
              > *「我們這學期不需要在電腦安裝任何沈重的軟體，打開瀏覽器就能直接寫 Python。這就像是雲端上的筆記本，隨時隨地都能跑程式碼。」*
            * **Live Demo 現場示範**：現場開啟 Colab，花 3 分鐘示範抓取台積電 (`2330.TW`) 股價並畫出走勢圖，讓大家驚艷一下。
            """)
        with col_b:
            st.markdown("#### ⚡ 教學節奏與備忘")
            st.warning("""
            * **常見狀況處理**：部分同學如果 Google 帳號登入有問題，請隔壁同學互相協助，或引導他們先看老師示範。
            * **互動提問**：問大家「有沒有人平常會看股票或關注科技新聞？」藉此連結大一的經濟學基礎。
            """)
            
    with tab3:
        st.subheader("🎙️ 第三節：Lab 0 實作與 AI 助教互動演練")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### 📝 口頭講稿與實作引導")
            st.markdown("""
            * **發布 Lab 0 任務**：請同學打開學期網頁，點開第一週的 Colab 連結，嘗試執行第一段範例程式碼。
            * **介紹側邊欄 AI 助教**：
              > *「如果在寫程式時卡關了、或覺得不好意思舉手，可以直接使用網頁側邊欄的 **Course AI Assistant**。它可以幫你解答關於期末專案、評分或程式碼的各種問題，而且還可以選擇匿名提問喔！」*
            * **下課前的叮嚀**：確認大家都成功加入 LINE 社群，並預告下週將進入「市場數據工程：台積電與蘋果的股價對比」。
            """)
        with col_b:
            st.markdown("#### ⚡ 教室巡視重點")
            st.warning("""
            * **走動式教學**：花 15 分鐘在走道巡視，特別協助外籍生確認 Colab 帳號與執行狀態。
            * **課後記錄**：留意今天同學們在助教網頁上提出的熱門問題，作為下週調整教學節奏的參考。
            """)

else:
    # 2-18 週的預設提示
    st.info(f"🚧 **{selected_week} 教師專屬講稿與提示** 正在蓄勢待發中！您可以隨時告訴我該週的教學重點，我來幫您擴充這份專屬講稿內容。")
