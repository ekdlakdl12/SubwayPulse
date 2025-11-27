import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# ----------------------------
# 1. 데이터 로드
# ----------------------------
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

# 연도 컬럼 추가
df_time["연도"] = df_time["사용월"] // 100
df_free["연도"] = df_free["사용월"] // 100

# -----------------------------
# 2. 시간대별 승차 컬럼 찾기
# -----------------------------
time_cols = [
    c for c in df_time.columns
    if ("승차" in c) and ("사용월" not in c)
    and ("호선명" not in c) and ("지하철역" not in c)
]

def extract_hour(col):
    m = re.match(r"(\d{2})시", col)
    return int(m.group(1)) if m else None

peak_hours = [7, 8, 9, 18, 19, 20]

# -----------------------------
# 3. 연도별 계산 + 2025는 연간 ‘추정’
# -----------------------------
YEARS = [2023, 2024, 2025]

# 연도별 기본요금 설정
fare_map = {2023: 1250, 2024: 1250, 2025: 1550}

rows = []

for year in YEARS:
    df_t = df_time[df_time["연도"] == year]
    df_f = df_free[df_free["연도"] == year]

    if df_t.empty or df_f.empty:
        continue

    # 이 연도에 포함된 '사용월' 개수 (데이터가 몇 개월치인지)
    months_covered = df_f["사용월"].nunique()
    if months_covered == 0:
        continue

    # 스케일링 팩터: 연간 추정용 (12개월 기준)
    scale = 12 / months_covered

    # 총 무임승차 인원 (현재 데이터 기준, partial)
    total_free_raw = df_f["무임승차인원"].sum()
    total_free_est = total_free_raw * scale  # 연간 추정

    # 시간대별 전체 탑승 (partial 기준)
    hour_total = df_t[time_cols].sum()
    total_board = hour_total.sum()
    hour_share = hour_total / total_board

    # 피크 시간대 비율 & 피크 무임승차
    peak_ratio = 0
    for col in time_cols:
        h = extract_hour(col)
        if h in peak_hours:
            peak_ratio += hour_share[col]

    peak_free_raw = total_free_raw * peak_ratio
    peak_free_est = peak_free_raw * scale  # 연간 추정

    # 손실액 계산 (기본 운임 × 무임승차 인원)
    fare = fare_map[year]
    total_loss_raw = total_free_raw * fare
    peak_loss_raw = peak_free_raw * fare

    total_loss_est = total_loss_raw * scale
    peak_loss_est  = peak_loss_raw * scale

    rows.append({
        "연도": year,
        "포함된_개월수": months_covered,
        "스케일(12/개월수)": scale,
        "전체 무임승차(명)_부분": total_free_raw,
        "전체 무임승차(명)_연간추정": total_free_est,
        "전체 손실액(원)_부분": total_loss_raw,
        "전체 손실액(원)_연간추정": total_loss_est,
        "피크 무임승차(명)_부분": peak_free_raw,
        "피크 무임승차(명)_연간추정": peak_free_est,
        "피크 손실액(원)_부분": peak_loss_raw,
        "피크 손실액(원)_연간추정": peak_loss_est,
    })

result = pd.DataFrame(rows)

# 억 단위로 변환
result["전체 손실액(억원)_연간추정"] = result["전체 손실액(원)_연간추정"] / 100_000_000
result["피크 손실액(억원)_연간추정"] = result["피크 손실액(원)_연간추정"] / 100_000_000

# -----------------------------
# 4. 현실 데이터 기반 보정
# -----------------------------
# (1) 기사에서 주어진 값 / 가정 (단위: 억 원, "무임승차로 인한 손실액")
#  - 2024년: 기사에 나온 무임승차 손실액 4,135억
#  - 2023년: 전체 적자 5,173억의 약 60%가 무임이라고 가정 → 3,104억
real_free_loss = {
    2023: 5173 * 0.6,   # ≒ 3,104억 (가정)
    2024: 4135          # 기사 수치
}
# 2025년은 공식 수치가 없어서, 2024년과 같은 보정계수를 적용한다고 가정

result["보정계수"] = 1.0

for idx, row in result.iterrows():
    year = int(row["연도"])
    if year in real_free_loss:
        # 보정계수 = (현실 무임손실) / (모형이 계산한 무임손실)
        factor = real_free_loss[year] / row["전체 손실액(억원)_연간추정"]
        result.loc[idx, "보정계수"] = factor

# 2025년은 2024년과 같은 계수 사용 (동일한 과대추정 패턴이라고 가정)
if 2025 in result["연도"].values and 2024 in result["연도"].values:
    factor_2024 = float(result.loc[result["연도"] == 2024, "보정계수"])
    result.loc[result["연도"] == 2025, "보정계수"] = factor_2024

# 보정된 무임손실액(억 원)
result["보정 전체 손실액(억원)"] = result["전체 손실액(억원)_연간추정"] * result["보정계수"]
result["보정 피크 손실액(억원)"] = result["피크 손실액(억원)_연간추정"] * result["보정계수"]

print("=== 연도별 무임승차 손실액 (연간 추정치 + 현실 보정) ===")
print(result[[
    "연도", "포함된_개월수", "스케일(12/개월수)",
    "전체 손실액(억원)_연간추정", "보정 전체 손실액(억원)",
    "피크 손실액(억원)_연간추정", "보정 피크 손실액(억원)"
]])

# -----------------------------
# 5. 그래프 (보정값 기준)
# -----------------------------
years = result["연도"].astype(str)

plt.figure(figsize=(12,5))

# (1) 전체 무임 손실액 (보정)
plt.subplot(1, 2, 1)
plt.bar(years, result["보정 전체 손실액(억원)"])
plt.title("연도별 전체 무임승차 손실액 (현실 데이터 보정, 억원)")
plt.xlabel("연도")
plt.ylabel("손실액(억원)")
plt.grid(True, axis="y", alpha=0.3)

# (2) 피크 시간대 무임 손실액 (보정)
plt.subplot(1, 2, 2)
plt.bar(years, result["보정 피크 손실액(억원)"], color="gray")
plt.title("연도별 피크시간대 무임승차 손실액 (현실 데이터 보정, 억원)")
plt.xlabel("연도")
plt.ylabel("손실액(억원)")
plt.grid(True, axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
