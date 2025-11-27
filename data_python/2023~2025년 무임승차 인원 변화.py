import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

import pandas as pd
import matplotlib.pyplot as plt

# 파일 불러오기
path_free = "서울시 지하철 호선별 역별 유_무임 승하차 인원 정보.csv"

for enc in ["cp949", "utf-8-sig", "utf-8"]:
    try:
        df_free = pd.read_csv(path_free, encoding=enc)
        break
    except:
        pass

# 연도 생성
df_free["연도"] = df_free["사용월"] // 100

# 분석 연도
YEARS = [2023, 2024, 2025]
summary = {}

for y in YEARS:
    df_y = df_free[df_free["연도"] == y]
    total = df_y["무임승차인원"].sum()
    summary[y] = total

# ------------------------------
# 1) 2025년 월평균 × 12 추정
# ------------------------------
df_2025 = df_free[df_free["연도"] == 2025]
months_2025 = df_2025["사용월"].nunique()
avg_2025 = summary[2025] / months_2025
est_2025_monthly = avg_2025 * 12  # 기본 추정치

# ------------------------------
# 2) 2024 증가율 기반 추정
# ------------------------------
growth_rate = (summary[2024] - summary[2023]) / summary[2023]
est_2025_trend = summary[2024] * (1 + growth_rate)

# ------------------------------
# 3) 두 값을 결합 (가중 평균)
# ------------------------------

final_2025 = 0.5 * est_2025_monthly + 0.5 * est_2025_trend

# ------------------------------
# 최종 데이터프레임 구성
# ------------------------------

result = pd.DataFrame({
    "연도": [2023, 2024, 2025],
    "무임승차_인원": [summary[2023], summary[2024], final_2025]
})

result["무임승차_만명"] = result["무임승차_인원"] / 10000

print(result)

# ------------------------------
# 그래프 출력
# ------------------------------
plt.figure(figsize=(10,5))
plt.bar(result["연도"].astype(str), result["무임승차_만명"], color=["#4E79A7", "#59A14F", "#F28E2B"])

plt.xlabel("연도")
plt.ylabel("무임승차 인원 (만 명)")
plt.title("2023~2025년 무임승차 인원 변화 (2025년은 증가율 반영 예측)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
