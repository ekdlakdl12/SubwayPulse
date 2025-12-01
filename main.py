# main.py

import os
import pandas as pd
import matplotlib.pyplot as plt

# 1단계에서 만든 모듈들을 import 합니다.
from data_loader import load_and_clean_data
# models.py에서 train_prediction_model과 analyze_loss 함수를 가져옵니다.
from models import train_prediction_model, analyze_loss 
from scenarios import run_age_scenario
from visualize import (
    plot_financial_crisis, 
    plot_time_riders, 
    plot_model_accuracy, 
    plot_fare_hike_pressure, 
    plot_operational_savings, 
    plot_mitigation_effects
)

# --- 설정 ---
# **반드시 이 경로를 실제 데이터 파일이 있는 '폴더 경로'로 수정하세요!**
# 데이터 파일들이 모여있는 폴더 이름이 '데이터셋'이 맞는지 확인하세요.
DATA_PATH = './데이터셋'
RESULTS_DIR = './results'

def run_presentation_storyline():
    """발표 PPT 순서(스토리라인)에 맞춰 프로젝트를 실행합니다."""
    print("="*50)
    print("           🚄 도시철도 적자 분석 프로젝트 실행")
    print("="*50)

    # 1. 데이터 로드 및 환경 설정
    # ----------------------------------------------------------------
    print("🚀 [STEP 1] 데이터 로드 및 환경 설정...")
    df_raw, df_clean = load_and_clean_data(DATA_PATH)
    
    if df_clean is None:
        print("❌ 데이터 로드에 실패하여 프로젝트 실행을 중단합니다.")
        return 

    # 2. 문제 정의 및 현황 분석 (시각화 1, 2)
    # ----------------------------------------------------------------
    print("📊 [STEP 2] 문제 정의 및 패턴 분석 시각화...")
    plot_financial_crisis(df_clean, os.path.join(RESULTS_DIR, '01_financial_crisis.png'))
    plot_time_riders(df_clean, os.path.join(RESULTS_DIR, '02_time_riders.png'))
    
    # 3. 모델링 및 예측 (models.py 호출 및 시각화 3)
    # ----------------------------------------------------------------
    print("🧠 [STEP 3] 요금 인상 예측 모델 학습...")
    model, df_predicted = train_prediction_model(df_clean)
    
    # analyze_loss 함수는 필요 시 여기에 호출하여 df_predicted를 업데이트 할 수 있습니다.
    # df_predicted = analyze_loss(df_predicted)
    
    # 3. 모델 검증 시각화
    plot_model_accuracy(model, os.path.join(RESULTS_DIR, '03_model_accuracy.png')) 
    
    # 4. 정책 완화 시뮬레이션 (scenarios.py 호출 및 시각화 4)
    # ----------------------------------------------------------------
    print("💡 [STEP 4] 정책 시뮬레이션 및 미래 예측...")
    scenario_df = run_age_scenario(df_predicted) 
    
    # 4. 미래 예측 시각화 (정책 미시행 vs 시행 시 요금 압박)
    plot_fare_hike_pressure(scenario_df, os.path.join(RESULTS_DIR, '04_fare_hike_pressure.png'))
    
    # 5. 최종 결론 시각화 (시각화 5, 6)
    # ----------------------------------------------------------------
    print("📈 [STEP 5] 정책 완화 효과 최종 시각화...")
    plot_operational_savings(scenario_df, os.path.join(RESULTS_DIR, '05_operational_savings.png'))
    plot_mitigation_effects(scenario_df, os.path.join(RESULTS_DIR, '06_mitigation_effects.png'))
    
    print("\n✅ 프로젝트 실행 완료. 결과는 'results' 폴더를 확인하세요.")


if __name__ == "__main__":
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
        
    run_presentation_storyline()