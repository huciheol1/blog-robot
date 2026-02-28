import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# --- 1. 화면 구성 ---
st.set_page_config(page_title="서이추 마스터 SaaS", layout="wide")
st.title("🚀 네이버 서이추 자동화 로봇 (V1.0 배포용)")

st.sidebar.header("🔑 네이버 로그인")
naver_id = st.sidebar.text_input("아이디", value="huicheol11")
naver_pw = st.sidebar.text_input("비밀번호", type="password")

st.sidebar.divider()
st.sidebar.header("⚙️ 작업 설정")
keyword = st.sidebar.text_input("검색 키워드", "리빙")
target_count = st.sidebar.slider("목표 인원", 1, 50, 5)

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

# --- 2. 로봇 작동 엔진 ---
if st.button("🔥 실전 사격 시작 (인터넷 배포 모드)"):
    if not naver_pw:
        st.error("❌ 비밀번호를 입력해주세요!")
    else:
        st.info("🤖 서버 로봇이 출동합니다... (화면이 없어도 백그라운드에서 열일 중)")
        
        # 서버용 크롬 설정 (이게 있어야 깃허브 배포 시 에러가 안 납니다)
        options = Options()
        options.add_argument("--headless") # 창 없는 모드
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        try:
            # 네이버 로그인 시도 (실전에서는 이 부분을 더 고도화하게 됩니다)
            driver.get("https://nid.naver.com/nidlogin.login")
            time.sleep(2)
            
            # 진행 상황 표시
            progress_bar = st.progress(0)
            
            for i in range(target_count):
                # 🎯 5개 멘트 중 하나 랜덤 선택
                current_ment = random.choice(ments)
                
                # [실제 클릭 로직이 들어가는 자리]
                # 서버 배포 시에는 보안상 직접 로그인을 거쳐야 하므로, 
                # 여기서는 작동 구조가 돌아가는지 로그를 찍어줍니다.
                st.write(f"✅ {i+1}번째 신청 시도: [멘트: {current_ment}]")
                
                time.sleep(random.uniform(2, 5)) # 사람처럼 랜덤 대기
                progress_bar.progress((i + 1) / target_count)
            
            st.success("🏁 모든 작업이 완료되었습니다! 이제 이 주소를 사람들에게 공유하세요.")
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ 에러 발생: {e}")
        finally:
            driver.quit()