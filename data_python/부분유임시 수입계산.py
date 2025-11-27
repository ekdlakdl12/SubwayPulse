import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# ============================================
# 0. CSV 불러오기
# ============================================
path_time = "서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv"
path_free = "서울시 지하철 호선별 역별 유_무임 승하차 인원 정보.csv"

def load_csv(path):
    for enc in ["cp949", "utf-8-sig", "utf-8"]:
        try:
            return pd.read_csv(path, encoding=enc)
        except:
            pass
    return pd.read_csv(path)

df_time = load_csv(path_time)
df_free = load_csv(path_free)

# 연도, 월 생성
df_time["연도"] = df_time["사용월"] // 100
df_free["연도"] = df_free["사용월"] // 100


# ============================================
# 1. 분석대상 = 2025년도 전체 추정치 사용
# ============================================

# 2025년도 무임승차 (10개월 데이터 → 12개월 추정)
df_25 = df_free[df_free["연도"] == 2025]
partial_total = df_25["무임승차인원"].sum()
months = df_25["사용월"].nunique()

monthly_avg = partial_total / months
free_2025_est = monthly_avg * 12  # 2025 전체 무임승차 추정

# ============================================
# 2. 시간대별 승차 비율 계산
# ============================================

# 피크시간
peak_hours = [7,8,9,18,19,20]

# 시간대 컬럼 (07시-08시 승차인원)
time_cols = [c for c in df_time.columns if ("승차" in c and "호선명" not in c and "지하철역" not in c)]

# 시간 추출 함수
def extract_hour(col):
    m = re.match(r"(\d{2})시", col)
    return int(m.group(1)) if m else None

df_time_25 = df_time[df_time["연도"] == 2025]

# 시간대별 전체 승차 합계
hour_total = df_time_25[time_cols].sum()
total_board = hour_total.sum()
hour_share = hour_total / total_board

# 피크시간 비율 계산
peak_share = 0
for col in time_cols:
    hour = extract_hour(col)
    if hour in peak_hours:
        peak_share += hour_share[col]

# 피크 무임승차 추정
peak_free_2025 = free_2025_est * peak_share


# ============================================
# 3. 부분유임 적용 시 추가 수입 계산
# ============================================

fares = {
    "100원": 100,
    "200원": 200,
    "300원": 300,
    "750원": 750
}

extra_revenues = {label: peak_free_2025 * fare for label, fare in fares.items()}

# 억원 단위 변환
extra_revenues_eok = {k: v / 100_000_000 for k, v in extra_revenues.items()}

print(extra_revenues_eok)


# ============================================
# 4. 막대그래프로 비교
# ============================================

plt.figure(figsize=(10,5))

labels = list(extra_revenues_eok.keys())
values = list(extra_revenues_eok.values())

plt.bar(labels, values)
plt.ylabel("추가 수입 (억원)")
plt.title("2025년 피크 시간대 부분 유임 적용 시 추가 수입 비교")
plt.grid(True, axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
