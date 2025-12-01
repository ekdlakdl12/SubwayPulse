import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False

import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# 1️⃣ 표 4. 지하철을 이용하는 이유 (전체 %)
#    → "무료요금" 비중이 압도적이라는 걸 보여줌
# ============================================================

reasons = ["무료요금", "신속성", "정시성", "쾌적성", "노선 편리"]
# ※ 아래 수치는 논문 표4의 '전체(%)'를 옮긴 예시값이야.
#    실제 값과 다르면 숫자만 수정해서 쓰면 됨.
reason_pct = [48.8, 11.4, 5.3, 2.7, 31.8]

plt.figure(figsize=(7,5))
bars = plt.bar(reasons, reason_pct)
plt.title("표 4. 지하철을 이용하는 주된 이유(전체 % 기준)")
plt.ylabel("비율(%)")
plt.ylim(0, max(reason_pct) + 10)
plt.grid(axis='y', alpha=0.3)

# 막대 위에 수치 표시
for b, v in zip(bars, reason_pct):
    plt.text(b.get_x() + b.get_width()/2, b.get_height()+0.5, f"{v:.1f}%", 
             ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()


# ============================================================
# 2️⃣ 표 5. 지하철을 이용하여 수행하는 주요 활동
#    → '친교'가 대부분, '통근' 비율은 매우 낮음
# ============================================================

activities = ["친교", "통근", "장보기", "가족방문", "진료", "종교", "기타"]
# 마찬가지로 논문 표5의 '전체(%)' 값 기준 예시
activity_pct = [77.7, 3.2, 2.1, 7.7, 1.8, 1.3, 0.5]

plt.figure(figsize=(7,5))
bars = plt.bar(activities, activity_pct)
plt.title("표 5. 지하철을 이용하여 수행하는 주요 활동(전체 %)")
plt.ylabel("비율(%)")
plt.ylim(0, max(activity_pct) + 10)
plt.grid(axis='y', alpha=0.3)

for b, v in zip(bars, activity_pct):
    plt.text(b.get_x() + b.get_width()/2, b.get_height()+0.5, f"{v:.1f}%",
             ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()


# ============================================================
# 3️⃣ 표 7 & 표 8 & 표 10
#    - 표 7: 무임승차 폐지에 대한 견해 (반대/보통/찬성)
#    - 표 8: 폐지 시 일상생활에 미치는 영향 정도
#    - 표10: 폐지 시 적정 요금 수준
# ============================================================

# ─ 표 7. 견해
opinion_labels = ["반대", "보통", "찬성"]
opinion_pct = [71.7, 22.7, 5.6]   # 예시(논문 값 기반, 필요시 수정)

plt.figure(figsize=(6,4))
bars = plt.bar(opinion_labels, opinion_pct)
plt.title("표 7. 노인 지하철 무임승차제도 폐지에 대한 견해(전체 %)")
plt.ylabel("비율(%)")
plt.ylim(0, max(opinion_pct) + 10)
plt.grid(axis='y', alpha=0.3)
for b, v in zip(bars, opinion_pct):
    plt.text(b.get_x()+b.get_width()/2, b.get_height()+0.5, f"{v:.1f}%",
             ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.show()

# ─ 표 8. 일상생활 영향 정도
impact_labels = ["매우 큼", "큼", "영향 없음"]
impact_pct = [60.0, 28.0, 12.0]  # 예시

plt.figure(figsize=(6,4))
bars = plt.bar(impact_labels, impact_pct)
plt.title("표 8. 무임승차제가 폐지될 경우 일상생활 영향 정도(전체 %)")
plt.ylabel("비율(%)")
plt.ylim(0, max(impact_pct) + 10)
plt.grid(axis='y', alpha=0.3)
for b, v in zip(bars, impact_pct):
    plt.text(b.get_x()+b.get_width()/2, b.get_height()+0.5, f"{v:.1f}%",
             ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.show()

# ─ 표 10. 폐지 시 적정 요금 수준
fare_labels = ["일반요금", "2/3~1/2 수준\n(부분유임)", "1/2 이하"]
fare_pct = [6.3, 34.0, 59.7]  # 예시

plt.figure(figsize=(6,4))
bars = plt.bar(fare_labels, fare_pct)
plt.title("표 10. 무임승차제가 폐지될 경우 적정 요금 수준(전체 %)")
plt.ylabel("비율(%)")
plt.ylim(0, max(fare_pct) + 10)
plt.grid(axis='y', alpha=0.3)
for b, v in zip(bars, fare_pct):
    plt.text(b.get_x()+b.get_width()/2, b.get_height()+0.5, f"{v:.1f}%",
             ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.show()


# ============================================================
# 4️⃣ 표 9. 폐지 시 ‘어떤 활동’이 가장 영향을 받는가
#    → 여기도 '친교' 비중이 압도적, 통근은 매우 적음
# ============================================================

affected_acts = ["친교", "통근", "장보기", "가족방문", "진료", "종교", "기타"]
# 논문 표9 전체(%) 예시 값 – 친교가 매우 높고, 통근은 낮게
affected_pct = [83.0, 3.0, 2.0, 7.0, 3.0, 1.0, 1.0]

plt.figure(figsize=(7,5))
bars = plt.bar(affected_acts, affected_pct)
plt.title("표 9. 무임승차제 폐지 시 영향을 많이 받는 활동(전체 %)")
plt.ylabel("비율(%)")
plt.ylim(0, max(affected_pct) + 10)
plt.grid(axis='y', alpha=0.3)

for b, v in zip(bars, affected_pct):
    plt.text(b.get_x()+b.get_width()/2, b.get_height()+0.5, f"{v:.1f}%",
             ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()
