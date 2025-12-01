# models.py

import pandas as pd
# from prophet import Prophet # 실제 모델 라이브러리 import 필요

def train_prediction_model(df_clean):
    """
    [PPT STEP 3] 요금 인상 예측 모델을 학습하고 결과를 반환합니다.
    """
    print("   -> 예측 모델 학습 시작 (cost_increase_Model2.ipynb 로직)...")
    
    # =========================================================
    # [여기에 기존 노트북의 모델 학습 및 예측 로직을 함수화하여 삽입]
    
    # df_clean이 None이면 오류를 방지하기 위해 빈 DataFrame을 사용합니다.
    if df_clean is None:
        df_predicted = pd.DataFrame()
    else:
        df_predicted = df_clean.head(20).copy()
        # 임시 예측 값
        df_predicted['predicted_fare'] = [1250, 1300, 1400, 1600, 1800, 1900, 2050, 2200, 2350, 2417, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950][:len(df_clean)]
        
    model = {"R2": 0.9121, "MAE": 25.00} # 모델 성능 지표 등
    # =========================================================
    
    print("   -> 예측 모델 학습 및 미래 탑승자 예측 완료.")
    
    return model, df_predicted

def analyze_loss(df_predicted):
    """
    [PPT STEP 3] 예측 결과를 바탕으로 미래 예상 적자를 계산합니다.
    """
    # =========================================================
    # [여기에 적자 분석 로직 삽입]
    # =========================================================
    return df_predicted


#python main.py <-- 메인파일만 실행