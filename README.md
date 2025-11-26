<h1 align="center">🚇 Deficit Chronicle: 재정 적자 분석, 인상 예측 및 완화 전략</h1>
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=3776AB&height=300&section=header&text=Deficit%20Chronicle&fontSize=70&fontAlignY=40" alt="Subway Pulse Header">
</p>

---

## 👤 프로젝트 팀원

| 역할 | 이름 |
| :--- | :--- |
| **팀원** | 최준영 |
| **팀원** | 곽태린 |

---

## 📅 프로젝트 개요 및 일정

본 프로젝트는 데이터 분석 기술 숙련 및 프로젝트 경험 축적을 목표로, 도시철도의 재정 문제 해결에 기여할 수 있는 실증적 데이터를 제공합니다.

| 카테고리 | 내용 |
| :--- | :--- |
| **주요 목적** | 데이터 분석 기술 숙련, 데이터 분석 프로젝트 경험 |
| **프로젝트 기간** | **11/19(수) ~ 11/28(금) (총 8일)** |
| **계획서 보고** | 11.20(목) 19:00 |
| **프로젝트 발표** | 11.28(금) 18:00 |
| **필수 제출 사항** | 1. GitHub 레포지토리 / 2. PPT 발표 자료 |

---

## 🚨 문제 정의 및 핵심 성과 하이라이트

| 📉 분석 목표 (Problem Definition) | 📈 모델 성과 및 정책 제언 (Mitigation Focus) |
| :--- | :--- |
| **도시철도 적자 심화**의 구조적 원인(고령화 및 복지 비용)을 정량적으로 분석하여 문제의 시급성 입증. | **모델 신뢰도 (R²):** **91.21%** 달성 (매우 우수) |
| **요금 인상 시나리오**를 예측하고, 이를 바탕으로 **교통비 급증을 억제**할 수 있는 정책적 완화 방안 모색. | **평균 예측 오차 (MAE):** **25.00원** (실질적인 인상 예측 능력 확보) |
| **무임승차 대상별 기여도** 분석을 통한 합리적인 재정 지원 방안 모색 기초 자료 제공. | **완화 전략 제시:** 예측 결과 기반의 **최적 무임승차 연령 상향 시점** 등 구체적인 방안 도출. |

---

## 🤝 업무 분담 (역할)

| 이름 | 담당 업무 |
| :--- | :--- |
| **최준영** | |
| **곽태린** | |

---

## 🧩 프로젝트 수행 절차 (Methodology)

프로젝트는 경제/정책적 분석과 고도화된 시계열 모델링을 통합하여 **문제 해결**에 중점을 두었습니다.

### 1. 🔍 문제 및 데이터 정의 (Problem & Data Definition)
> 지하철 요금 인상 요인(재정 적자, CPI 등)과 무임승차 데이터를 중심으로 **적자 완화**를 위한 분석 목표 설정.

### 2. 💾 데이터 수집 및 특징 공학 (Acquisition & Feature Engineering)
> 요금 이력, **CPI, 재정 적자 대리 변수**를 통합하고, **`Years_Since_Hike`** 등 예측 성능을 극대화할 특징을 생성.

### 3. 🧹 데이터 전처리 및 분석 (Preprocessing & Analysis)
> 데이터 정제 후, **무임승차 대상별 기여도**를 상세 분석하여 재정 손실의 주된 원인(노인 85%)을 명확히 파악.

### 4. 📉 모델링 및 검증 (Modeling & Validation)
> **Scikit-learn, Prophet**을 활용한 시계열 회귀 모델 구축. **R² 0.9121** 신뢰도를 확보하여 예측 시나리오의 기반 마련.

### 5. 💡 시나리오 예측 및 완화 전략 제언 (Prediction & Mitigation Proposal)
> 2026년~2035년 미래 요금 인상 시나리오를 제시하고, 분석된 적자 원인을 해소하기 위한 **구체적인 정책 완화 전략**을 보고서에 담아 제출.

---

## 🛠️ 기술 스택 (Technical Stack)

### 💻 데이터 분석 및 모델링 환경

[![Numpy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-003D5C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-3E7199?style=for-the-badge&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)

### 🧠 머신러닝 및 시계열 예측 모델

[![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![Statsmodels](https://img.shields.io/badge/Statsmodels-1A1A1A?style=for-the-badge&logo=statsmodels&logoColor=white)](https://www.statsmodels.org/stable/index.html)
[![Prophet](https://img.shields.io/badge/Prophet-3B5998?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.github.io/prophet/)

### 💾 버전 관리 (VCS)

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
