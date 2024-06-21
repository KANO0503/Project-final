import streamlit as st
import google.generativeai as genai

# Google AI API 키 설정
GOOGLE_API_KEY = "AIzaSyBYBIHvllOkdFzTD_AwGsAtIZ1QUBJ5afk"
genai.configure(api_key=GOOGLE_API_KEY)

# 생성 모델 초기화
model = genai.GenerativeModel('gemini-pro')

# CSS 스타일 주입
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f0f0;
        font-family: 'Arial', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        overflow-y: auto; /* 세로 스크롤바 표시 */
    }
    .header {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
        margin-top: 100px;
        width: 100%;
        background-color: #4CAF50;
        padding: 10px 0;
    }
    .header img {
        width: 100px;
        margin-right: 20px;
    }
    .header h1 {
        color: white;
        margin: 0;
    }
    .input-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 20px;
    }
    .stTextInput > div > div > input {
        padding: 10px;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        width: 50%;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        margin-left: 130px; /* 전송 버튼을 입력 필드의 오른쪽으로 */
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stMarkdown {
        font-size: 18px;
    }
    .menu-container {
        margin-top: 20px;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 페이지 상단에 배너 이미지 추가
st.markdown('<div class="header"><img src="3.jpeg"><h1>현지 데이터 기반 로컬 맛집</h1></div>', unsafe_allow_html=True)

# 일본 지역 목록
japan_regions = [
    "신주쿠", "시부야 스크램블 교차로", "하라주쿠", "도쿄 타워", "시모키타자와", "아키하바라", "스카이트리",  
    "도쿄 디즈니랜드", "아사쿠사", "메이지 신궁",
    "긴자", "우에노 공원", "롯폰기 힐즈" 
]

# 목적지 입력 받기
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="input-container">', unsafe_allow_html=True)
destination_input = st.selectbox("도쿄 내 여행지를 선택해주세요", japan_regions, key="destination_input")
st.markdown('</div>', unsafe_allow_html=True)

# "메뉴를 선택해주세요" 출력
st.markdown('<div class="menu-container">', unsafe_allow_html=True)
st.markdown('<p>메뉴를 선택후 체크해주세요</p>', unsafe_allow_html=True)

# 메뉴 체크박스 추가 
st.markdown('<div class="menu-container">', unsafe_allow_html=True)
menu_options = ["라멘", "스시", "오코노미야키", "돈카츠"]
selected_menus = []
for menu in menu_options:
    selected = st.checkbox(menu)
    if selected:
        selected_menus.append(menu)
# 사용자 입력을 위한 텍스트 필드 추가
custom_menu = st.text_input("이외에 원하는 메뉴가 있다면 직접 입력 해보세요")
if custom_menu:
    selected_menus.append(custom_menu)
st.markdown('</div>', unsafe_allow_html=True)

# 사용자 입력 및 버튼 클릭 처리
if st.button("전송"):
    destination = st.session_state.destination_input
    menu_query = ", ".join(selected_menus)
    query = f"\"{menu_query}\" {destination} tabelog.com/tokyo 사이트를 기반으로 입력된 도쿄 지역에 유명 명소 근처에 위치한 현재 영업중이고 Tabelog 별 점수가 5점에 가까운 랭킹 1위~5위 맛집을 추천해줘, 가게 리뷰, 가게 정보(가게명은 일본어(한국어)로 둘다표기, 주소, 전화번호, 영업시간, 가격대) 함께 알려주세요"
    
    # "로컬 찐 맛집을 찾고 있어요. 조금만 기다려주세요" 문구 출력
    loading_text = st.empty()
    loading_text.markdown("로컬 찐 맛집을 찾고 있어요. 조금만 기다려주세요...")
    
    # spin.gif 이미지 출력
    spinner = st.image("spin.gif", width=200)
    
    # 모델에 사용자 입력 전달하여 응답 생성
    response = model.generate_content(query)
    # 생성된 응답 출력 (스크롤 가능한 텍스트 상자에)
    response_text = response.candidates[0].content.parts[0].text
    
    # 응답을 표시하기 전에 loading_text를 클리어합니다.
    loading_text.empty()
    spinner.empty()
    
    st.markdown('<div class="response-container">', unsafe_allow_html=True)
    st.text_area("쩝쩝박사gemini의 답변입니다", value=response_text, height=400)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # main div 마감
