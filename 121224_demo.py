import streamlit as st

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データのサンプル（選手の名前、打率、ホームラン数、打点など）
data = {
    '選手名': ['選手1', '選手2', '選手3', '選手4', '選手5', '選手6', '選手7', '選手8', '選手9'],
    '打率': [0.300, 0.250, 0.275, 0.310, 0.260, 0.280, 0.290, 0.240, 0.310],
    'ホームラン': [15, 8, 10, 20, 12, 7, 14, 9, 22],
    '打点': [50, 30, 35, 60, 40, 25, 45, 20, 65]
}

# データフレーム作成
df = pd.DataFrame(data)

# アプリのタイトル
st.title('野球チームの選手成績管理')

# 表示用のデータフレーム
st.dataframe(df)

# 選手名を選択するためのプルダウンメニュー
selected_player = st.selectbox('選手を選んでくれよな！', df['選手名'])

# 選択された選手のデータを表示
player_data = df[df['選手名'] == selected_player]
st.write(f"選手: {selected_player}")
st.write(f"打率: {player_data['打率'].values[0]}")
st.write(f"ホームラン数: {player_data['ホームラン'].values[0]}")
st.write(f"打点: {player_data['打点'].values[0]}")

# 選手の成績のグラフ
st.subheader(f"{selected_player}の成績")
fig, ax = plt.subplots()
ax.bar(['打率', 'ホームラン', '打点'], player_data.iloc[0, 1:])
ax.set_title(f"{selected_player}の成績")
ax.set_ylabel('数値')
st.pyplot(fig)