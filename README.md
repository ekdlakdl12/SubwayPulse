<h1 align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=3776AB&height=350&section=header&text=Deficit%20Chronicle&fontSize=80&fontColor=ffffff&fontAlign=center&animation=twinkling&desc=재정%20적자%20분석,%20인상%20예측%20및%20완화%20전략&descAlign=center&descPosition=70" alt="Deficit Chronicle Header">
</h1>

<div align="center">

[![GitHub Repo stars](https://img.shields.io/github/stars/YOUR_USERNAME/YOUR_REPO_NAME?style=social)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/YOUR_REPO_NAME?style=flat-square&logo=github)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/commits/main)
[![Project Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME)
[![Analysis Focus](https://img.shields.io/badge/Focus-Urban%20Railway%20Deficit-3776AB?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLW1ldHJvIj48cGF0aCBkPSJNOSAxNmg2Ii8+PHBhdGggZD0iTTcgMTB2NG0xMCAwVjEwIi8+PHBhdGggZD0iTTIgMTdsMjAtNlM0IDE3IDIgMTd6Ii8+PC9zdmc+&logoColor=white)](#)

</div>

---

## 👤 핵심 프로젝트 팀 (Team & Role)

<div align="center">
  
| 이름 | 역할 | 담당 업무 (Code Focus) |
| :---: | :---: | :left |
| **최준영** | 🧑‍💻 **팀원** | `cost_increase_Model2.ipynb`, `cost_of_Free_Ride_Loss.ipynb`, `free_Ride_Ratio.ipynb`, `front_Explamation.ipynb`, `design_Improvement.ipynb` |
| **곽태린** | 🧑‍💻 **팀원** | `2023~2025 무임승차 인원 변화.py`, `나이 상향 시뮬레이션.py`, `노인이 지하철을 이용하는 이유1.py`, `노인이 지하철을 이용하는 이유2.py`, `부분유임시 수입계산.py` |

</div>

<br>

---

## 📅 프로젝트 개요 및 일정 (Overview)

| 카테고리 | 내용 |
| :---: | :--- |
| **주요 목적** | **데이터 분석 기술 숙련** 및 도시철도 **재정 문제 해결**을 위한 실증적 데이터 제공 |
| **프로젝트 기간** | **11/19(수) ~ 11/28(금) (총 8일)** |
| **발표 및 제출** | **11.28(금) 18:00 발표** (GitHub Repo & PPT 제출) |

---

## 🚨 문제 정의 및 핵심 성과 하이라이트 (Key Achievements)

<details>
<summary><b>🔥 클릭하여 주요 성과 및 문제 정의 확인</b></summary>
<br>

| 📉 분석 목표 (Problem Definition) | 📈 모델 성과 및 정책 제언 (Mitigation Focus) |
| :--- | :--- |
| **도시철도 적자 심화**의 구조적 원인(고령화 및 복지 비용)을 정량적으로 분석하여 문제의 **시급성 입증**. | **모델 신뢰도 (R²):** <span style="color: #4CAF50; font-weight: bold;">91.21%</span> 달성 (매우 우수) |
| **요금 인상 시나리오**를 예측하고, 이를 바탕으로 **교통비 급증을 억제**할 수 있는 정책적 **완화 방안 모색**. | **평균 예측 오차 (MAE):** <span style="color: #FF9800; font-weight: bold;">25.00원</span> (실질적인 인상 예측 능력 확보) |
| **무임승차 대상별 기여도** 분석을 통한 합리적인 재정 지원 방안 모색 **기초 자료 제공**. | **완화 전략 제시:** 예측 결과 기반의 **최적 무임승차 연령 상향 시점** 등 **구체적인 정책 제언** 도출. |

</details>

---

## 🧩 프로젝트 수행 절차 (Methodology Flow)

프로젝트는 경제/정책적 분석과 고도화된 시계열 모델링을 통합하여 **실질적인 문제 해결**에 중점을 두었습니다.

<div align="center">

| Step | 🔍 과정 | ✨ 주요 Output / Focus |
| :---: | :--- | :--- |
| **1** | **문제 및 데이터 정의** | 적자 완화를 위한 요금 인상 요인(재정 적자, CPI 등)과 무임승차 데이터 중심 목표 설정 |
| **2** | **데이터 수집 및 특징 공학** | 요금 이력, **CPI, 재정 적자 대리 변수** 통합 / **`Years_Since_Hike`** 등 예측 성능 극대화 특징 생성 |
| **3** | **데이터 전처리 및 분석** | 데이터 정제 / **무임승차 대상별 기여도 상세 분석** (노인 85%의 재정 손실 기여 명확화) |
| **4** | **모델링 및 검증** | Scikit-learn, **Prophet** 활용 시계열 회귀 모델 구축 / **R² 0.9121** 신뢰도 확보 |
| **5** | **시나리오 예측 및 제언** | 2026년~2035년 미래 요금 인상 시나리오 제시 / 적자 해소를 위한 **구체적인 정책 완화 전략** 보고서 제출 |

</div>

---

## 🛠️ 기술 스택 (Technical Stack)

<h3 align="left">💻 데이터 분석 및 모델링 환경</h3>
<div align="left">
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Matplotlib-003D5C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib"/>
  <img src="https://img.shields.io/badge/Seaborn-3E7199?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn"/>
</div>

<h3 align="left">🧠 머신러닝 및 시계열 예측 모델</h3>
<div align="left">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn"/>
  <img src="https://img.shields.io/badge/Statsmodels-1A1A1A?style=for-the-badge&logo=statsmodels&logoColor=white" alt="Statsmodels"/>
  <img src="https://img.shields.io/badge/Prophet-3B5998?style=for-the-badge&logo=facebook&logoColor=white" alt="Prophet"/>
</div>

<h3 align="left">💾 버전 관리 (VCS)</h3>
<div align="left">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</div>

---

<h2 align="center">📜 Conclusion: 지속 가능한 도시철도 재정을 위하여</h2>
<div align="center">
  <img src="https://img.shields.io/badge/Thank%20You%20for%20Your%20Interest-Visit%20Our%20Repository-007ACC?style=for-the-badge&logo=github&logoColor=white">
</div>
