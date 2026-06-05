import streamlit as st

st.title("🎢 놀이기구 탑승 가능 여부 확인")

# 키 입력 받기 (기본값 150, 최소 50, 최대 250)
height = st.number_input('키를 입력하세요 (cm):', min_value=50, max_value=250, value=150)

# 결과 확인 버튼
if st.button('탑승 여부 확인'):
    if height < 100:
        st.error('❌ 탑승 불가')
    elif 100 <= height < 130:
        st.warning('⚠️ 보호자 동행 시 탑승 가능')
    elif 130 <= height < 195:
        st.success('✅ 탑승 가능')
    elif height >= 195:
        st.error('❌ 탑승 불가')