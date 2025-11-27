#main
# main.py

import os
import pandas as pd
# 1단계에서 만든 모듈들을 import 합니다.
from data_loader import load_and_clean_data
from models import train_prediction_model, analyze_loss
from scenarios import run_age_scenario, calculate_revenue
from visualize import plot_time_pattern, plot_mitigation_results

# --- 설정 ---
# 참조 데이터셋 경로 변경 (프로젝트 루트 경로 기준)
DATA_PATH = './data/subway_dataset.csv'
RESULTS_DIR = './results'

def run_presentation_storyline():
    """발표 PPT 순서(스토리라인)에 맞춰 프로젝트를 실행합니다."""
    print("="*50)
    print("           🚄 도시철도 적자 분석 프로젝트 실행")
    print("="*50)

    # 1. 문제 정의 및 데이터 로드 (PPT 초기 슬라이드)
    # ----------------------------------------------------------------
    print("🚀 [STEP 1] 데이터 로드 및 환경 설정...")
    df_raw, df_clean = load_and_clean_data(DATA_PATH)
    
    # 2. 핵심 분석 결과 시각화 (PPT 중간 슬라이드)
    # ----------------------------------------------------------------
    print("📊 [STEP 2] 무임승차 패턴 및 비용 분석 시각화...")
    # 예: 시간대별 무임승차 비율 (이전에 작업했던 그래프)
    plot_time_pattern(df_clean, save_path=os.path.join(RESULTS_DIR, '01_time_pattern.png'))
    
    # 3. 모델링 및 예측 (PPT 모델링 슬라이드)
    # ----------------------------------------------------------------
    print("🧠 [STEP 3] 요금 인상 예측 모델 학습...")
    model, df_predicted = train_prediction_model(df_clean)
    
    # 4. 정책 완화 시뮬레이션 (PPT 정책 제언 슬라이드)
    # ----------------------------------------------------------------
    print("💡 [STEP 4] 나이 상향 및 부분유임 시뮬레이션 실행...")
    
    # 예: 나이 상향 시나리오 실행 (Income_Age_Segmentation_Analysis 결과 활용)
    scenario_df = run_age_scenario(df_predicted) 
    
    # 예: 부분 유임 시 수입 변화 계산
    final_revenue = calculate_revenue(scenario_df) 
    
    # 5. 시뮬레이션 결과 시각화 (PPT 결론 슬라이드)
    # ----------------------------------------------------------------
    print("📈 [STEP 5] 정책 시뮬레이션 결과 시각화...")
    plot_mitigation_results(scenario_df, save_path=os.path.join(RESULTS_DIR, '02_mitigation_results.png'))
    
    print("\n✅ 프로젝트 실행 완료. 결과는 'results' 폴더를 확인하세요.")
    


# main.py (수정된 부분)

# ... (함수 정의는 그대로)

if __name__ == "__main__":
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
        
    # 'run_project'를 'run_presentation_storyline'으로 수정
    run_presentation_storyline()