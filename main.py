import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)

'Done!!!!'

#left_column, right_column = st.beta_columns(2)
#button = left_column.button('右カラムに文字を表示')
#if button:
#    right_column.write('ここは右カラム')

#expander1 = st.beta_expander('問い合わせ1')
#expander1.write('問い合わせ回答')

#expander2 = st.beta_expander('問い合わせ2')
#expander2.write('問い合わせ回答')

#expander3 = st.beta_expander('問い合わせ3')
#expander3.write('問い合わせ回答')

audio_file = open('好きなこと.m4a', 'rb')
audio_bytes = audio_file.read()

st.sidebar.write('このWebページのBGMです。必ず流してください。')
st.sidebar.audio(audio_bytes, format='audio/ogg')

option = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 20000)

'あなたの趣味：',option, 'です。'
'コンディション：', condition

if st.checkbox('Show Image'):
    img = Image.open('happy_woman_color.png')
    st.image(img, caption='フレッシュさん', use_column_width=True)



#img = Image.open('happy_woman_color.png')
#st.image(img, caption='フレッシュさん', use_column_width=True)#

video_file = open('demo-video.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)



df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
df
st.table(df.style.highlight_max(axis=0))

st.map(df)

