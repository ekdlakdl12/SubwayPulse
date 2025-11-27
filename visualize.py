# visualize.py

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# 폰트 설정 (통일)
plt.rcParams['font.family'] = 'Malgun Gothic' 
plt.rcParams['axes.unicode_minus'] = False 

# NOTE: 이 함수는 main.py에서 호출될 때 실제 df를 받지만, 
# 시각화 코드는 현재 데이터 구조(가상 데이터)에 맞춰 작성되어 있습니다.
def plot_time_pattern(df, save_path):
    """
    시간대별 무임승차 비율 및 탑승자 현황 분석 그래프를 생성하고 저장합니다.
    """
    
    # [PPT 데이터]: 실제 DF가 들어오면 이 부분을 DF에서 추출하는 코드로 대체해야 합니다.
    # 현재는 가상 데이터를 사용하여 시각화 기능을 구현합니다.
    TIME_LABELS = ['6-9시 (출근)', '9-12시', '12-17시', '17-20시 (퇴근)', '20시 이후']
    TOTAL_RIDERS = np.array([370, 200, 250, 300, 100])
    FREE_RIDE_RATIO = np.array([18.0, 25.0, 22.0, 16.0, 20.0])
    FREE_RIDE_RIDERS_ESTIMATED = TOTAL_RIDERS * (FREE_RIDE_RATIO / 100)
    
    # 2. 시각화 시작
    fig, ax1 = plt.subplots(figsize=(10, 5))

    # --- 좌측 Y축 (전체 탑승 규모: 막대 그래프) ---
    ax1.set_xlabel('시간대(시)')
    ax1.set_ylabel('전체 탑승자 수 (가중치)')

    # '전체 탑승자' 막대 그래프 (회색)
    ax1.bar(TIME_LABELS, TOTAL_RIDERS, color='lightgray', alpha=0.8, label='전체 탑승자 (규모)')

    # '무임승차 인원 (추정)' 막대 그래프 (주황색, 위에 겹쳐서)
    x = np.arange(len(TIME_LABELS))
    ax1.bar(x, FREE_RIDE_RIDERS_ESTIMATED, color='#FF7F50', alpha=1.0, label='무임승차 인원 (추정)') 

    ax1.tick_params(axis='y') 
    ax1.set_ylim(0, 400) 
    ax1.grid(axis='y', linestyle='dotted', linewidth=0.5) 

    # --- 하이라이팅 영역 (출퇴근 시간대만 유지, 연하게) ---
    ax1.axvspan(-0.5, 0.5, color='lightsalmon', alpha=0.2) # 6-9시
    ax1.axvspan(2.5, 3.5, color='lightsalmon', alpha=0.2) # 17-20시

    # --- 데이터 레이블 추가 (무임승차 비율 %) ---
    for i, ratio in enumerate(FREE_RIDE_RATIO):
        ax1.text(i, FREE_RIDE_RIDERS_ESTIMATED[i] + 15, f'{ratio:.1f}%', ha='center', color='darkred', fontsize=10, fontweight='bold')

    # --- 범례 및 제목 ---
    ax1.legend(loc='upper left')
    plt.title('시간대별 탑승자 및 무임승차 현황 분석', fontsize=14, pad=15)
    fig.tight_layout()
    
    # 파일 저장 및 출력
    plt.savefig(save_path)
    plt.show()
    plt.close(fig)
    print(f"   -> 시각화 결과 '{save_path}' 저장 완료.")

# visualize.py

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
# ... (이전 코드 생략: plot_time_pattern 함수) ...

def plot_mitigation_results(df_scenario, save_path):
    """
    [PPT STEP 5] 정책 시뮬레이션 결과를 시각화합니다.
    (연령 상향 및 부분 유임 시뮬레이션의 수익 증가분을 비교)
    """
    print(f"   -> 시각화 생성: 정책 시뮬레이션 결과 저장 경로: {save_path}")

    # -----------------------------------------------------------
    # [시나리오 데이터 기반 시각화 로직 삽입]
    # 실제 데이터와 로직에서는 df_scenario를 분석하여 두 시나리오의 
    # 예상 수익 증가분을 계산해야 합니다.
    
    # 임시 데이터 생성 (models.py/scenarios.py의 임시 결과 기반)
    # 1. 연령 상향 시뮬레이션 수익 (run_age_scenario에서 revenue_increase의 합)
    age_up_revenue = df_scenario['revenue_increase'].sum() * 100
    # 2. 부분 유임 시뮬레이션 수익 (calculate_revenue의 결과)
    partial_fare_revenue = age_up_revenue * 1.5 # 임의로 50% 더 높게 가정

    # 시각화할 데이터
    scenarios = ['무임승차 연령 상향 (65세 -> 70세)', '부분 유임제 도입 (50% 할인)']
    revenues = [age_up_revenue, partial_fare_revenue]

    plt.figure(figsize=(10, 6))
    
    # 막대 그래프 생성
    bars = plt.bar(scenarios, revenues, color=['skyblue', 'lightcoral'])
    
    # 값 표시 (숫자 포맷팅)
    def format_y_tick(value, pos):
        return f'{value/100000000:,.0f}억'
    
    # 금액 포맷을 위한 툴
    from matplotlib.ticker import FuncFormatter
    formatter = FuncFormatter(format_y_tick)
    plt.gca().yaxis.set_major_formatter(formatter)
    
    # 그래프 타이틀 및 라벨
    plt.title('정책 시나리오별 예상 추가 수입 비교 (2025년 기준)', fontsize=16)
    plt.ylabel('예상 추가 수입 (원)', fontsize=12)
    plt.xticks(fontsize=11)
    
    # 막대 위에 정확한 금액 표시
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + (max(revenues)*0.01), 
                 f'{yval/100000000:,.1f}억', ha='center', va='bottom', fontsize=10, weight='bold')

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    # -----------------------------------------------------------
    
    print("   -> 정책 시뮬레이션 결과 시각화 파일 저장 완료.")