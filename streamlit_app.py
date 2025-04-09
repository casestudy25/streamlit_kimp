import streamlit as st
import requests

log_url = st.secrets["LOG_API_URL"]

st.title("🪵 실시간 로그 뷰어")

# "맨 아래로" 버튼
st.markdown("[맨 아래로 이동](#bottom-anchor)")

try:
    response = requests.get(log_url)
    content = response.json()["content"]
    lines = content.strip().split('\n')
    lines = [line for line in lines if line.strip()]  # 빈 줄 제거

    for line in lines:
        st.text(line)

except Exception as e:
    st.error(f"불러오기 실패: {e}")

# 앵커: 페이지 제일 아래
st.markdown("<div id='bottom-anchor'></div>", unsafe_allow_html=True)
