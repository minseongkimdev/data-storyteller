
import os
import streamlit as st
import numpy as np
import pickle as pkle
import pandas as pd
from PIL import  Image
import os.path

# Custom imports
from multipage import MultiPage
from pages import page1, machine_learning, metadata, data_visualize, redundant # import your pages here

# Create an instance of the app
app = MultiPage()


def home() :
    st.title('🎉푸드천국🎉')
    st.header('당신만의 푸드설계앱 foodheaven😊')

    with st.beta_expander('서비스 소개 더보기'):
        st.write("""

    모두가 건강에 대해 걱정하지만 관심도가 낮으며, 특히 개별진단/케어 서비스는 있지만,
    원포인트/전방위 케어 서비스 부재

    만개의레시피DB + 식품영양성분DB 결합
    냉부를 부탁해 + 부족한 영양소를 진단하고 영양관리 해주는 서비스 + 영양제 판매/일일 새벽배송

         """)

    st.text("\n")
    st.text("\n")

    name = st.text_input('크루네임 입력', '크루')
    if st.button("Submit"):
        st.success(f'{name}님! 저희의 크루가 되어주셔서 감사해요💛')
    st.text("\n")
    st.text("\n")
    st.text("\n")

def common():
    time = st.selectbox('선호하는 조리시간을 선택해 주세요',
                        ('', '10분 이내', '20분 이내', '30분 이내', '60분 이내'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    choice = st.selectbox('요리 난이도 선택', ('', '상', '중', '하'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    choicetwo = st.selectbox('혹시 오늘은 먹기 싫은 것이 있나요?',
                             ('', '중식 노노해', '한식 질려', '분식 별로'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    options = st.multiselect(
    '활용하고 싶은 재료 - 냉장고에 있는 재료들을 선택해 주세요',
    ['계란', '닭고기', '파', '마늘', '소고기', '양고기', '돼지고기'])
    st.text("\n")
    st.text("\n")
    st.text("\n")

    optionstwo = st.multiselect(
    '혹시 “이건 안 들어갔으면” 하는 재료들도 있나요?',
    ['홍어', '고수', '참치', '초콜릿', '설탕'])
    st.text("\n")
    st.text("\n")

    if st.button('추천음식 보러가기(결과화면 수정필요)'):
        img = Image.open("./Img_test_omelet.jpg")
        st.image(img, width=300, caption="계란말이(5m, 하) 레시피 보러가기")
        img = Image.open("./Img_test_chicken.jpg")
        st.image(img, width=300, caption="치킨(30m, 상) 레시피 보러가기")



def tandanji(name):
    height = st.text_input(f'{name}님의 키(cm)를 입력해 주세요', '170')
    st.text("\n")
    st.text("\n")

    activity = st.selectbox(f"{name}님의 활동량을 선택하세요.",
                            ("", "많음", "보통", "적음"))
    st.write(activity, "을(를) 선택하셨습니다.")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    # st.subheader('목표 탄단지 비율과 섭취량')
    if activity == '많음':
        cal = (int(height)-100)*0.9*40
    elif activity == '보통':
        cal = (int(height)-100)*0.9*30
    else:
        cal = (int(height)-100)*0.9*25

    st.info(f'{name}님의 하루 권장 칼로리 : {cal}kcal')

    tan = cal * 0.5 / 4
    dan = cal * 0.2 / 4
    ji = cal * 0.3 / 9
    st.info(f'{name}님의 목표 탄단지 비율(하루 권장 섭취량) : 5({tan:.2f}g):2({dan:.2f}g):3({ji:.2f}g)')
    # st.info(f'{name}님 화이팅!💪')
    st.text("\n")
    st.text("\n")
    st.text("\n")

    # values = st.slider(
    # '선호하는 조리시간을 선택해 주세요',
    # 0, 180, (20, 30))
    # st.text("\n")
    # st.text("\n")
    # st.text("\n")

    common()


def gocal(name):
    # cat = st.selectbox(f"{name}님이 추구하는 식단 스타일을 골라 주세요",
    #                    ("", "고단백", "저칼로리", "고칼로리", "비건", "etc"))
    # st.write(cat, "을(를) 선택하셨습니다.")
    # st.text("\n")
    # st.text("\n")
    # st.text("\n")

    st.info(f'{name}님~ 1000칼로리 이상 감당하실 수 있으시죠?😇')
    st.text("\n")
    st.text("\n")
    st.text("\n")
    common()


def vegan(name):
    st.info(f'{name}님~ 비건식단을 추천합니다😇')
    st.text("\n")
    st.text("\n")
    st.text("\n")
    common()

def supper(name):
    st.info(f'{name}님~ 밤늦은 시각 출출하신가요~')
    supper_cat = st.selectbox(f'카테고리 선택',
                        ("", "건강한 버전", "낮은 칼로리 버전", "단백질 높은 버전",
                         "매운 버전", "자극적인 버전", "튀긴 버전"))
    st.write(supper_cat, "을(를) 선택하셨습니다.")

    st.text("\n")
    st.text("\n")
    st.text("\n")
    common()

def random(name):
    favor = st.selectbox(f'음식 카테고리 선택',
                            ("", "한식", "중식", "양식", "일식", "매운거", "안매운거"))
    st.write(favor, "을(를) 선택하셨습니다.")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    time = st.selectbox('선호하는 조리시간을 선택해 주세요',
                        ('', '10분 이내', '20분 이내', '30분 이내', '60분 이내'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    choice = st.selectbox('요리 난이도 선택', ('', '상', '중', '하'))
    st.text("\n")
    st.text("\n")
    st.text("\n")

    options = st.multiselect(
    '활용하고 싶은 재료 - 냉장고에 있는 재료들을 선택해 주세요',
    ['계란', '닭고기', '파', '마늘', '소고기', '양고기', '돼지고기'])
    st.text("\n")
    st.text("\n")
    st.text("\n")

    optionstwo = st.multiselect(
    '혹시 “이건 안 들어갔으면” 하는 재료들도 있나요?',
    ['홍어', '고수', '참치', '초콜릿', '설탕'])
    st.text("\n")
    st.text("\n")

    if st.button('추천음식 보러가기'):
        img = Image.open("./Img_test_omelet.jpg")
        st.image(img, width=300, caption="계란말이(5m, 하) 레시피 보러가기")
        img = Image.open("./Img_test_chicken.jpg")
        st.image(img, width=300, caption="치킨(30m, 상) 레시피 보러가기")

def worldcup(name):
    st.subheader('푸드월드컵')
    message = st.text_area("불편사항을 알려주세요.")
    if st.button("Click"):
        if message.title():
            st.success(f"{name}님의 소중한 의견은 서비스 개선에 적극 반영하겠습니다. 감사합니다.")
        else:
            st.error("텍스트를 입력해주세요")


pages = ['Page1','Page2','Page3']

if os.path.isfile('next.p'):
    next_clicked = pkle.load(open('next.p', 'rb'))
    if next_clicked == len(pages):
        next_clicked = 0
else:
    next_clicked = 0

if next:
    next_clicked = next_clicked+1
    if next_clicked == len(pages):
        next_clicked = 0

choice = st.sidebar.radio("목차",('Page1','Page2', 'Page3'), index=next_clicked)

pkle.dump(pages.index(choice), open('next.p', 'wb'))

name = ''
page = ''
if choice == 'Page1':
    st.title('🎉푸드천국🎉')
    st.header('당신만의 푸드설계앱 foodheaven😊')

    with st.beta_expander('서비스 소개 더보기'):
        st.write("""

    모두가 건강에 대해 걱정하지만 관심도가 낮으며, 특히 개별진단/케어 서비스는 있지만,
    원포인트/전방위 케어 서비스 부재

    만개의레시피DB + 식품영양성분DB 결합
    냉부를 부탁해 + 부족한 영양소를 진단하고 영양관리 해주는 서비스 + 영양제 판매/일일 새벽배송

         """)

    st.text("\n")
    st.text("\n")

    name = st.text_input('크루네임 입력', '크루')
    next = st.button("입력 완료")

    if next :
        st.success(f'{name}님! 저희의 크루가 되어주셔서 감사해요💛')
    st.text("\n")
    st.text("\n")
    st.text("\n")

elif choice == 'Page2':
    st.title('★원하는 서비스 선택★')
    # page = st.radio(
    #     "",
    #     ('원하는 서비스를 선택해주세요', '건강을 챙기는 으르신', '먹고죽자 치팅데이', '비건에의한 비건을위한', '밤에 출출한 야식러',
    #      '생각없는 당신을위한 랜덤', '선택장애를 위한 월드컵'))

    next = st.button("선택 완료")
    st.text("\n")

elif choice == 'Page3':
    st.title('★아래의 Form을 작성해주세요')
    print('page')
    print(page)
    if page == '건강을 챙기는 으르신':
        common()
        tandanji(f'{name}')
    elif page == '먹고죽자 치팅데이':
        common()
        gocal(f'{name}')
    elif page == '비건에의한 비건을위한':
        common()
        vegan(f'{name}')
    elif page == '밤에 출출한 야식러':
        common()
        supper(f'{name}')
    elif page == '생각없는 당신을위한 랜덤':
        common()
        random(f'{name}')
    else:
        common()
        worldcup(f'{name}')

# next = st.button('Go to next page')


# col1, col2 = st.beta_columns(2)
# col1.image(display, width = 400)
# col2.title("Data Storyteller Application")

# Add all your application here
# app.add_page("Page 1", page1.app)
# app.add_page("Change Metadata", metadata.app)
# app.add_page("Machine Learning", machine_learning.app)
# app.add_page("Data Analysis",data_visualize.app)
# app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()
