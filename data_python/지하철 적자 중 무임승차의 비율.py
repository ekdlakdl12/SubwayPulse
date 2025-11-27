import matplotlib.pyplot as plt
import platform

import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False

# ✅ 데이터 (단위: 억 원)
total_deficit = 6947
free_ride_loss = 4135
other_deficit = total_deficit - free_ride_loss

labels = ['무임승차 손실', '기타 적자']
sizes = [free_ride_loss, other_deficit]

# ✅ 파이 그래프
plt.figure(figsize=(6, 6))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('서울 지하철 적자 구성 비율')
plt.tight_layout()
plt.show()
