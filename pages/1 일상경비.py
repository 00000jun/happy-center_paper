"""
일상경비 페이지

현재 가장 완성도가 높은 페이지
[2024-04-20 22:00]
"""

# 모듈
import streamlit as st
import sys # 파일경로
import pages.module as module # 함수모듈
import pages.category_variable as category_var # 전역변수
import pages.checkbox_variable as checkbox_var # 전역변수
import pages.read_number as read_number # 숫자 한글로 읽기
import pyperclip # 클립보드


# 헤더
st.header("일상경비", divider="rainbow")

# 지출 분류 셀렉트박스 생성 및 최종 셀렉트박스 항목 반환
category_dicts = [category_var.category_dict_1, category_var.category_dict_2, category_var.category_dict_3] # 지출항목 딕셔너리 가져오기 -> 변수 정의
final_category = module.create_expn_selectbox(category_dicts)

# 각 분류에 해당하는 지출항목 체크박스 생성
items = checkbox_var.test_checkbox[final_category] # 전역변수에서 해당 분류에 해당하는 항목 가져오기 : list
items_bool = [] # 지출항목 : 체크여부 리스트

# 체크박스 생성 후 체크여부 리스트에 저장
result_dict = module.create_checkbox(items)

# 지출항목 입력
title, result_dict = module.create_expenditure_items(result_dict)

# 본문 생성
result_paper = module.create_paper(title, result_dict)

# 품의서 출력
module.print_paper(result_paper)
