"""
모듈 정의
"""

import streamlit as st
import read_number as read_number # 숫자 한글로 읽기
import pyperclip # 클립보드


# 딕셔너리의 value를 입력 받아 key로 반환하는 함수
def convert_values_to_keys(value:str, dictionary:dict)->list:
    """
    딕셔너리에서 value를 입력 받아 key로 반환하는 함수
    """
    return {v: k for k, v in dictionary.items()}.get(value)


# 연계 지출 카테고리 필터링 함수
def set_selectbox_elements(init_value:str, expn_category:list)->list:
    """
    연계 지출 카테고리 필터링 함수
    """
    selectbox_elements = [x for x in expn_category if x.startswith(init_value)]
    return selectbox_elements


def create_expn_selectbox(dicts:list):

    # key_list 정의
    key_list = [list(dict.keys()) for dict in dicts] # 딕셔너리(key) 리스트

    # 셀렉트 박스 정리
    col = st.columns(len(dicts))

    # 셀렉트 박스 기록(이전 값 저장)
    record = []

    for i in range(len(dicts)):
        if i == 0:
            with col[i]:
                select = st.selectbox("분류1", list(dicts[i].values()))
                select = convert_values_to_keys(select, dicts[i])
                record.append(select)
        else:
            with col[i]:
                select = st.selectbox(f"분류{i+1}", [dicts[i][x] for x in set_selectbox_elements(select, key_list[i])], )
                select = convert_values_to_keys(select, dicts[i])
                record.append(select)

    if select:
        final_result = dicts[len(dicts)-1][select]
    else:
        select = record[-2]
        final_result = dicts[-2][select]

    # 테스트
    # st.write(record) # 붙임파일

    return final_result


# TODO: 지출항목별 유니크값 뭐있는지 확인하고 그부분은 하드코딩해야 함
# TODO: 금액 읽는 부분 조정
# 지출항목 입력시 항목을 입력받아 그에 맞는 입력폼을 제공하는 함수
def create_input_form(item:str):
    
    if item == "관련":
        col = st.columns(3)
        with col[0]:
            depart = st.text_input("부서", placeholder="중등교육과")
        with col[1]:
            num = st.text_input("문서번호", placeholder="0000")
        with col[2]:
            date = st.text_input("문서날짜", placeholder="20240101")
        link_paper = f"{depart}-{num}({date[:4]}. {date[4:6]}. {date[6:]})"
        return link_paper

    elif item == "금액":
        cost= st.number_input("금액", min_value=0)
        cost_kor = read_number.readnumber(cost)
        st.write(f'금 :orange[{cost_kor}]원')
        cost = f'금{cost:,}원(금{cost_kor}원)'

        return cost
    
    elif item == "내역":
        return st.text_input("내역")
    
    elif item == "일시":
        return st.date_input("일시")
    
    elif item == "장소":
        return st.text_input("장소")
    
    elif item == "대상":
        return st.text_input("대상")
    
    elif item == "기간":
        col_test = st.columns(2)
        with col_test[0]:
            start = st.date_input("시작일")
        with col_test[1]:
            end = st.date_input("종료일")
        return start, end
    
    elif item == "구분":
        return st.text_input("구분")
    
    elif item == "품목":
        return st.text_input("품목")
    else:
        return None


# 체크박스 생성 후 체크여부 리스트에 저장하는 함수 
def create_checkbox(items:list):

    # 결과값 저장 딕셔너리
    result_dict = {}

    # 체크박스 컬럼 생성, 체크값 딕셔너리 저장
    checkbox_col = st.columns(len(items)) # 체크박스 컬럼 생성

    for i in range(len(items)):

        with checkbox_col[i]:

            result = st.checkbox(items[i])

            if result:
                result_dict[items[i]] = True # 체크된 항목만 딕셔너리에 저장
            else:   
                pass

    return result_dict


# 지출항목 입력 함수
def create_expenditure_items(result_dict:dict):

    # 지출항목 입력
    with st.expander("지출항목 입력", expanded=False):
    
        # 품의명 입력
        title = st.text_input("품의명")
        
        # 지출항목 아이템 저장
        for item in result_dict:
            input_value = create_input_form(item)
            result_dict[item] = input_value

    return title, result_dict


# TODO: 함수 설명 주석 추가
# 본문 생성하는 함수
def create_paper(title:str, result_dict:dict) -> str:
    """
    :return: 품의서(str)
    """
    
    result_paper = f'{title}\n\n'

    for n, item in enumerate(result_dict):
        if result_dict[item]:
            result_paper += f'{n+1}. {item} : {result_dict[item]}\n'

    return result_paper


# TODO: 함수 설명 주석 추가
# 품의서 출력
def print_paper(result_paper:str):
    """
    :param result_paper: 품의서 내용
    """
    
    with st.expander("품의서 작성", expanded=False):
        paper = st.text_area("출력", result_paper, height=300)

        # 클립보드 복사 버튼 처리
        if st.button('복사'):
            pyperclip.copy(paper)
            st.success('품의서 내용이 클립보드에 저장되었습니다 (Ctrl+V)')


# 붘임파일 작성
def create_attachment_file():
    """
    붙임파일 작성
    """
    pass
