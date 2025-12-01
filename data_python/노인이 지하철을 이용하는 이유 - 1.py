import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

import matplotlib.pyplot as plt

# ==========================================
# 노인 지하철 이용 목적 (표 5 기반)
# ==========================================

labels = ["친교(만남·모임)", "통근(일)", "장보기", "가족방문", "진료", "종교", "기타"]
values = [77.7, 3.2, 8.0, 7.7, 2.3, 0.6, 0.5]

# ---------- 막대그래프 ----------
plt.figure(figsize=(10, 5))
plt.bar(labels, values)
plt.ylabel("비율(%)")
plt.title("노인 지하철 이용 목적 비율 (표 5 기반)")
plt.grid(axis='y', alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
