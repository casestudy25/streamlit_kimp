import streamlit as st
import requests

# secrets.toml 에 저장된 URL 사용
log_url = st.secrets["LOG_API_URL"]

st.title("🪵 실시간 로그 뷰어")

try:
    response = requests.get(log_url)
    content = response.json()["content"]
    lines = content.strip().split('\n')
    lines.reverse()  # 최신 로그 위로

    for line in lines:
        st.text(line)

except Exception as e:
    st.error(f"불러오기 실패: {e}")
