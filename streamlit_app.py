import streamlit as st
import requests

# 맨 위 앵커
st.markdown("<div id='top-anchor'></div>", unsafe_allow_html=True)

st.title("👁️ 로그 뷰어")

# 날짜 입력
date_input = st.text_input("날짜 입력 (예: 250408) (미입력 시 오늘 날짜 조회)", "", key="log_date_input")

# 토큰 입력
token_input = st.text_input("접근 토큰 입력", "", type="password", key="token_input")

# 맨 아래로 이동 링크
st.markdown("[맨 아래로 이동](#bottom-anchor)")

# 새로 불러오기 버튼
if st.button("로그 불러오기"):
    try:
        query = {}
        if date_input.strip():
            query["date"] = date_input.strip()
        if token_input.strip():
            query["token"] = token_input.strip()

        response = requests.get(st.secrets["LOG_API_URL"], params=query)
        data = response.json()

        if "content" in data:
            lines = data["content"].strip().split('\n')
            lines = [line for line in lines if line.strip()]
            for line in lines:
                st.text(line)
        else:
            st.warning("로그 내용이 없습니다.")

    except Exception as e:
        st.error(f"불러오기 실패: {e}")

# 맨 아래 앵커 + 맨 위로 이동 링크
st.markdown("<div id='bottom-anchor'></div>", unsafe_allow_html=True)
st.markdown("[맨 위로 이동](#top-anchor)")
