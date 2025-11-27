# data_loader.py

import pandas as pd
import os

def load_and_clean_data(file_path):
    """
    지정된 경로에서 데이터를 로드하고 기본적인 클리닝을 수행합니다.
    (노트북의 초기 데이터 로드/전처리 셀 코드를 통합합니다.)
    """
    if not os.path.exists(file_path):
        print(f"🚨 오류: 데이터 파일 '{file_path}'를 찾을 수 없습니다. 경로를 확인하세요.")
        # 빈 데이터프레임을 반환하여 프로그램이 멈추지 않도록 합니다.
        return None, None

    print(f"   -> 데이터 로드: {file_path}")
    df_raw = pd.read_csv(file_path)
    df_clean = df_raw.copy()

    # [여기에 기존 주피터 노트북의 데이터 클리닝/전처리 코드 삽입]
    # 예: 컬럼명 변경, 결측치 처리, 날짜 형식 변환 등
    # df_clean['Date'] = pd.to_datetime(df_clean['Date']) 
    # df_clean.dropna(inplace=True) 

    print("   -> 데이터 클리닝 완료.")
    
    # 원본과 클리닝된 데이터프레임을 모두 반환합니다.
    return df_raw, df_clean