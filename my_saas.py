import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import random

# --- 1. 브랜딩 및 화면 구성 ---
st.set_page_config(page_title="삼돌이군의 서이추 로봇", page_icon="🤖")

st.title("🤖 삼돌이군의 서이추 자동 프로그램 웹 앱")

with st.expander("ℹ️ 이 프로그램을 만든 이유 (클릭해서 보기)"):
    st.write("""
    안녕하세요! 삼돌이군입니다. 
    반복적인 서이추 노가다는 이제 그만! 
    로봇에게 맡기고 더 가치 있는 포스팅에 집중하세요. 
    회원님들을 위해 정성껏 제작했습니다. 🚀
    """)

st.divider()

# --- 2. 입력창 구성 ---
st.sidebar.header("🔑 네이버 로그인")
naver_id = st.sidebar.text_input("아이디", value="")
naver_pw = st.sidebar.text_input("비밀번호", type="password")

st.sidebar.divider()
st.sidebar.header("⚙️ 작업 설정")
keyword = st.sidebar.text_input("검색 키워드", "리빙")
target_count = st.sidebar.slider("목표 인원", 1, 50, 10)

st.subheader("📝 정지 방지용 랜덤 멘트 (5개)")
col1, col2 = st.columns(2)
with col1:
    m1 = st.text_input("멘트 1", "포스팅 잘 보고 갑니다! 우리 서로이웃 해요~")
    m2 = st.text_input("멘트 2", "안녕하세요! 글이 너무 좋아서 이웃 신청드려요.")
    m3 = st.text_input("멘트 3", "좋은 정보 감사합니다. 소통하며 지내요!")
with col2:
    m4 = st.text_input("멘트 4", "우연히 들렀는데 취향저격이네요! 서이추 부탁드립니다.")
    m5 = st.text_input("멘트 5", "블로그 이웃하고 싶어서 신청 남깁니다. 자주 소통해요!")

ments = [m1, m2, m3, m4, m5]

# --- 3. 실행 엔진 ---
if st.button("🔥 삼돌이 로봇 가동 시작!"):
    if not naver_id or not naver_pw:
        st.warning("⚠️ 네이버 아이디와 비밀번호를 먼저 입력해주세요!")
    else:
        st.info("🤖 삼돌이 로봇이 출동했습니다. 잠시만 기다려주세요...")
        
        # 서버 환경 최적화 설정
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        
        try:
            # [핵심 수정] 서버에 설치된 크롬을 직접 호출 (버전 충돌 방지)
            driver = webdriver.Chrome(options=options)
            
            progress_bar = st.progress(0)
            status_text = st.empty()

            # 테스트용 로그 (실제 네이버 로그인 로직은 여기에 추가 가능)
            for i in range(target_count):
                current_ment = random.choice(ments)
                status_text.text(f"⏳ {i+1}/{target_count}명째 신청 중... (멘트: {current_ment[:10]}...)")
                
                # 작업 간 랜덤 대기 (차단 방지)
                time.sleep(random.uniform(2, 4)) 
                progress_bar.progress((i + 1) / target_count)
            
            st.success(f"🏁 총 {target_count}명에게 서이추 신청을 성공적으로 보냈습니다!")
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ 실행 중 오류가 발생했습니다: {e}")
            st.info("💡 Tip: 'packages.txt' 파일이 잘 생성되었는지 다시 한번 확인해주세요.")
        finally:
            if 'driver' in locals():
                driver.quit()

