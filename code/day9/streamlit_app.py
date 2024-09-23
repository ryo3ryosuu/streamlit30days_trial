import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

# データ生成
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

# データフレームの表示
st.write("DataFrame with random data")
df = chart_data.head(5)
st.write(df)

# ラインチャートの表示
st.write("Line chart with random data")
st.line_chart(chart_data)
