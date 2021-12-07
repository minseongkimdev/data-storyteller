import os
import streamlit as st
import numpy as np
import pandas as pd
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import page1, machine_learning, metadata, data_visualize, redundant # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('Logo.png')
display = np.array(display)

st.title('🎉푸드천국🎉')
st.header('당신만의 푸드설계앱 foodheaven😊')

# with st.expander('서비스 소개 더보기'):
#     st.write("""
#
# 모두가 건강에 대해 걱정하지만 관심도가 낮으며, 특히 개별진단/케어 서비스는 있지만,
# 원포인트/전방위 케어 서비스 부재
#
# 만개의레시피DB + 식품영양성분DB 결합
# 냉부를 부탁해 + 부족한 영양소를 진단하고 영양관리 해주는 서비스 + 영양제 판매/일일 새벽배송
#
#      """)
# st.text("\n")
# st.text("\n")

name = st.text_input('크루네임 입력', '크루')
if st.button("Submit"):
    st.success(f'{name}님! 저희의 크루가 되어주셔서 감사해요💛')
st.text("\n")
st.text("\n")
st.text("\n")

# col1, col2 = st.beta_columns(2)
# col1.image(display, width = 400)
# col2.title("Data Storyteller Application")

# Add all your application here
app.add_page("Page 1", page1.app)
app.add_page("Change Metadata", metadata.app)
app.add_page("Machine Learning", machine_learning.app)
app.add_page("Data Analysis",data_visualize.app)
app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()
