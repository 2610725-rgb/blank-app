import streamlit as st

st.title("구구단 앱 🔢")

# 2단부터 9단까지 반복
for i in range(2, 10):
    st.header(f"🔹 {i}단") # 각 단의 제목
    
    # 1부터 9까지 곱하기
    for j in range(1, 10):
        # 기존 코드의 더하기(+)를 곱하기(*)로 수정했습니다!
        st.write(f"{i} × {j} = {i * j}")
        
    st.divider() # 단 사이에 구분선 넣기