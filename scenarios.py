# scenarios.py

import pandas as pd
# NOTE: Income_Age_Segmentation_Analysis.ipynb의 연령별 분포 데이터 필요

def run_age_scenario(df_predicted):
    """
    [PPT STEP 4] 무임승차 연령 상향 정책 시뮬레이션을 실행합니다.
    (나이 상향 시뮬레이션.py 로직 통합)
    """
    print("   -> 정책 시뮬레이션: 무임승차 연령 상향 효과 분석 시작...")
    
    df_scenario = df_predicted.copy()

    # -----------------------------------------------------------
    # [여기에 연령별 인구 데이터와 정책 변경에 따른 탑승 패턴 변화 로직 삽입]
    # 1. 65세 -> 70세 상향 시, 65~69세 인원의 유임 전환 비율 계산
    # df_scenario['new_free_riders'] = df_scenario['original_free_riders'] * 0.8 # 20% 감소 가정
    # 2. 신규 수익 및 적자 감소분 계산
    
    df_scenario['revenue_increase'] = df_scenario['predicted_riders'] * 0.05 # 임의의 시뮬레이션 결과
    # -----------------------------------------------------------
    
    print("   -> 연령 상향 시나리오 실행 완료.")
    return df_scenario

def calculate_revenue(df_scenario):
    """
    [PPT STEP 4] 부분 유임 정책 시 수입 변화를 계산합니다.
    (부분유임시 수입계산.py 로직 통합)
    """
    print("   -> 정책 시뮬레이션: 부분 유임 시 수입 변화 계산 시작...")
    
    # -----------------------------------------------------------
    # [여기에 부분 유임 (예: 50% 할인) 정책에 따른 수입 증가분 계산 로직 삽입]
    # total_new_revenue = df_scenario['total_riders'] * (fare * 0.5) 
    
    total_new_revenue = df_scenario['revenue_increase'].sum() * 100 # 임시 금액
    # -----------------------------------------------------------
    
    print(f"   -> 부분 유임 정책 적용 시 예상 추가 수입: {total_new_revenue:,.0f}원 계산 완료.")
    return total_new_revenue