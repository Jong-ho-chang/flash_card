import streamlit as st
import pandas as pd

# 엑셀 파일 경로
excel_path = "flash_card.xlsx"

# 엑셀 파일 읽기
df = pd.read_excel(excel_path)

# 회차 목록 추출
rounds = df['1회차'].unique()

# 회차별 데이터 분리
rounds_dict = {
    round_name: df[df['1회차'] == round_name][['영단어', '뜻']].reset_index(drop=True)
    for round_name in rounds
}

st.title("📘 영어 단어 플래시카드 - 회차별 학습")

# 회차 선택
selected_round = st.selectbox("회차를 선택하세요:", list(rounds_dict.keys()))

# 선택된 회차 데이터 가져오기
df_selected = rounds_dict[selected_round]

st.write(f"### {selected_round} 단어 학습")

# 카드 형태로 단어 출력
for idx, row in df_selected.iterrows():
    with st.expander(f"단어 {idx+1}: {row['영단어']}"):
        st.write(f"뜻: {row['뜻']}")

st.info("각 단어를 눌러 뜻을 확인해보세요!")
