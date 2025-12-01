# visualize.py

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import os

# 폰트 설정 (통일)
plt.rcParams['font.family'] = 'Malgun Gothic' 
plt.rcParams['axes.unicode_minus'] = False 

# --- 시각화 함수 1: 구조적 재정 악화 심각성 ---
def plot_financial_crisis(df_data, save_path):
    print(f"   -> 시각화 생성: 구조적 재정 악화 분석 저장 ({save_path})")
    
    # =========================================================
    # [재정 악화 및 노인 비율 통합 분석] 그래프 코드 삽입
    # 임시 데이터 (실제 데이터로 대체 필요)
    labels = ['총 당기순손실', '무임승차 손실']
    values = [5173, 3663] # 억 원
    loss_contribution = 0.708 # 무임승차 손실 비중 70.8%
    elderly_utilization = 0.849 # 노인 이용 비중 84.9%

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(labels, values, color=['lightgray', '#E95460'])
    ax.set_title('구조적 재정 악화의 심각성: 무임승차 손실 비중 및 노인 비율 (2023년)', fontsize=14, pad=15)
    ax.set_ylabel('손실 금액 (억 원)')

    for i, v in enumerate(values):
        ax.text(i, v + 100, f'{v:,}억 원', ha='center', fontsize=11, weight='bold')

    ax.text(1.5, values[1] * 1.5, f'노인 이용 비중: {elderly_utilization:.1%}', color='green', fontsize=10, weight='bold')
    ax.text(1.5, values[1] * 1.3, f'무임승차 손실 비중: {loss_contribution:.1%}', color='red', fontsize=10, weight='bold')
    
    # =========================================================
    plt.savefig(save_path)
    plt.close(fig)

# --- 시각화 함수 2: 시간대별 탑승 패턴 분석 ---
def plot_time_riders(df_data, save_path):
    print(f"   -> 시각화 생성: 시간대별 탑승 패턴 분석 저장 ({save_path})")
    
    # =========================================================
    # [2025년 시간대별 전체 탑승 vs 무임승차 인원(만, 추정)] 그래프 코드 삽입
    # 이 함수는 이전에 구현했던 시간대별 바 플롯을 생성합니다.
    # (코드 생략, 실제 구현 필요)
    # =========================================================
    plt.savefig(save_path)
    plt.close()

# --- 시각화 함수 3: 모델 검증 및 신뢰도 ---
def plot_model_accuracy(model_info, save_path):
    print(f"   -> 시각화 생성: 모델 검증 및 신뢰도 입증 저장 ({save_path})")

    # =========================================================
    # [지하철 요금 예측 모델 적합도 (Actual vs. Predicted)] 그래프 코드 삽입
    # model_info는 models.py에서 반환한 딕셔너리({R2: 0.9121, MAE: 25.00})를 사용합니다.
    
    # 임시 데이터
    actual = [1250, 1240, 1260, 1250, 1400, 1390, 1400, 1500, 1500]
    predicted = [1265, 1245, 1270, 1255, 1430, 1380, 1405, 1530, 1505]
    years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, predicted, 'r--', marker='o', alpha=0.6, label='모델 예측선')
    ax.scatter(years, actual, label='실제 요금 데이터', zorder=5)

    ax.text(years[0], 1500, f"모델 신뢰도 (R²): {model_info['R2']:.4f}\n평균 절대 오차 (MAE): {model_info['MAE']:.2f}원", 
            bbox=dict(boxstyle="round,pad=0.5", fc="lightgreen", alpha=0.5), fontsize=12)

    # =========================================================
    plt.savefig(save_path)
    plt.close(fig)

# --- 시각화 함수 4: 미래 요금 인상 압박 예측 ---
def plot_fare_hike_pressure(df_scenario, save_path):
    print(f"   -> 시각화 생성: 요금 인상 압박 예측 비교 저장 ({save_path})")
    
    # =========================================================
    # [정책 시나리오별 미래 요금 인상 압박 예측] 그래프 코드 삽입
    # df_scenario에는 'non_policy_fare', 'policy_fare' 컬럼이 있다고 가정합니다.
    
    fig, ax = plt.subplots(figsize=(10, 6))
    years = np.arange(2025, 2025 + len(df_scenario))
    
    ax.plot(years, df_scenario['non_policy_fare'], 'r-o', alpha=0.8, label='정책 미시행 시나리오 (현재 추이)')
    ax.plot(years, df_scenario['policy_fare'], 'g-s', alpha=0.8, label='정책 시행 시나리오 (인상 압박 완화)')

    ax.text(years[-1], df_scenario['non_policy_fare'].iloc[-1], f"{df_scenario['non_policy_fare'].iloc[-1]:,.0f}원", 
            color='red', fontsize=12, ha='right')
    ax.text(years[-1], df_scenario['policy_fare'].iloc[-1], f"{df_scenario['policy_fare'].iloc[-1]:,.0f}원", 
            color='green', fontsize=12, ha='right')

    # =========================================================
    plt.savefig(save_path)
    plt.close(fig)

# --- 시각화 함수 5: 연간 운영비 절감 효과 ---
def plot_operational_savings(df_scenario, save_path):
    print(f"   -> 시각화 생성: 연간 추가 운영비 절감 효과 저장 ({save_path})")
    
    # =========================================================
    # [정책 시나리오별 연간 추가 운영비 절감 효과] 그래프 코드 삽입
    # 임시 데이터
    scenarios = ['70세 상향', '75세 상향', '80세 상향']
    savings = [df_scenario['op_saving_70'].iloc[0], df_scenario['op_saving_75'].iloc[0], df_scenario['op_saving_80'].iloc[0]]

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(scenarios, savings, color=['#3C9BE9', '#4CAF50', '#FFC107'])
    ax.set_ylabel('추가 절감액 (억 원)')

    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, 
                f'{bar.get_height():.1f}억 원', ha='center', fontsize=11, color=bar.get_facecolor(), weight='bold')

    # =========================================================
    plt.savefig(save_path)
    plt.close(fig)

# --- 시각화 함수 6: 누적 적자 완화 및 사회적 효과 ---
def plot_mitigation_effects(df_scenario, save_path):
    print(f"   -> 시각화 생성: 누적 적자 완화 및 사회적 효과 저장 ({save_path})")
    
    # =========================================================
    # [정책 시나리오별 재정 및 사회적 효과 분석] 그래프 코드 삽입
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # 좌측: 장기 누적 적자 완화
    scenarios = ['70 상향', '75 상향', '80 상향']
    revenues = [df_scenario['revenue_70'].iloc[0], df_scenario['revenue_75'].iloc[0], df_scenario['revenue_80'].iloc[0]]

    ax1.bar(scenarios, revenues, color=['#3C9BE9', '#4CAF50', '#FFC107'])
    ax1.set_title('① 장기 누적 적자 완화 효과 (2025~2050년)')
    ax1.set_ylabel('누적 절감 금액 (억 원)')

    # 우측: 첨두시간 혼잡률 완화 효과 (임시 데이터)
    ax2.bar(['정책 미시행', '75세 상향 시행'], [160, 139.2], color=['gray', '#4CAF50'])
    ax2.set_title('② 75세 상향 시 첨두시간 혼잡률 완화 효과')
    ax2.set_ylabel('혼잡률 (%)')
    
    # =========================================================
    plt.savefig(save_path)
    plt.close(fig)