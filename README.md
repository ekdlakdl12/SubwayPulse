<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=Subway%20Pulse&fontSize=90" />

## 지하철 연간 이용 및 수요도 예측 시스템

## 세부 주제 : 
목적: 데이터 분석 기술 숙련, 데이터 분석 프로젝트 경험

## 프로젝트 기간: 11/19(수) ~ 11/28(금) 8일
프로젝트 계획서 보고: 11.20(목) 19:00  
프로젝트 발표: 11.28(금) 18:00

## 필수 제출 사항
1.github 레포지토리  
2.PPT 발표 자료

## 사용 기술
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  

## 사용 라이브러리
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)  
[![Matplotlib](https://img.shields.io/badge/Matplotlib-003D5C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)    
[![Seaborn](https://img.shields.io/badge/Seaborn-3E7199?style=for-the-badge&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)  

## 머신러닝 모델링  
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)  
[![Statsmodels](https://img.shields.io/badge/Statsmodels-1A1A1A?style=for-the-badge&logo=statsmodels&logoColor=white)](https://www.statsmodels.org/stable/index.html)  
[![Prophet](https://img.shields.io/badge/Prophet-3B5998?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.github.io/prophet/)  

## 형상관리
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)  

## 🧩 프로젝트 수행 절차 (Process Flow)

프로젝트는 데이터 과학의 표준 방법론에 따라 다음과 같은 **5단계**로 진행되었습니다.

### 1. 🔍 문제 정의 (Problem Definition)
> 지하철 요금 인상 요인 분석 및 미래 요금 예측이라는 핵심 목표와 검증 기준을 설정했습니다.

### 2. 💾 데이터 수집 (Data Acquisition)
> **지하철 요금 이력, CPI 상승률, 유/무임 승하차 인원** 등 분석에 필요한 모든 데이터를 확보했습니다.
> 
> *_(사용 도구: CSV 파일, 공공데이터 포털 등)_*

### 3. 🧹 전처리 (Preprocessing)
> 수집된 데이터의 결측치 및 이상치를 처리하고, **`Years_Since_Hike`**와 **`Cumulative_CPI`** 같은 모델의 설명력을 높이는 핵심 **특징 공학(Feature Engineering)**을 수행했습니다.

### 4. 📉 모델링 및 분석 (Modeling & Analysis)
> **Scikit-learn, Statsmodels, Prophet**을 활용하여 시계열 예측 모델을 구축했습니다. 홀드아웃 검증을 통해 **R² 0.9121**이라는 높은 신뢰도를 확보했습니다.

### 5. 📈 시각화 및 보고 (Visualization & Reporting)
> **Matplotlib/Seaborn**을 사용하여 예측 결과, 무임승차 비율 분석, 그리고 호선별 특징 등을 시각화하여 최종 보고서를 완성했습니다.  


<h2 align="center">✨ 프로젝트 주요 성과 ✨</h2>
<p align="center">
  저희 모델이 달성한 핵심 지표들을 확인하세요.
</p>

| 지표 | 결과 | 의미 |
| :--- | :--- | :--- |
| **모델 신뢰도 (R²)** | **91.21 %** | 지하철 요금 변동성 예측 설명력 |
| **평균 예측 오차 (MAE)** | **25.00 원** | 실용적으로 '완전 정확' 수준의 오차율 |
| **핵심 기여 특징** | `CPI` & `Years Since Hike` | 도메인 지식을 반영한 예측 정확도 향상 |

<br>
---

<h2 align="center">📄 프로젝트 개요 (Overview)</h2>
<p align="center">
  이 프로젝트의 목표와 배경을 간략히 설명합니다.
</p>

본 프로젝트는 **서울 지하철 요금**의 인상 패턴을 분석하고, **소비자 물가 지수(CPI) 및 인상 주기** 등의 경제/정책적 요인을 반영하여 **2026년 이후의 요금을 예측**하는 시계열 모델링을 목표로 했습니다. 또한, 공사의 재정 건전성 분석을 위해 **무임승차 비율의 상세 분석**을 포함합니다.

<br>
---

<h2 align="center">💡 주요 분석 결과 및 인사이트</h2>
<p align="center">
  프로젝트를 통해 얻은 핵심적인 발견들입니다.
</p>

* **📈 요금 예측 결론:** 구축된 모델은 R² 0.9121의 신뢰도로 향후 10년간의 요금 인상 시점과 폭을 매우 정확하게 예측했습니다.
* **👴 무임승차 비중:** 분석 결과, 무임승차 인원 중 **노인(65세 이상)이 약 85%**를 차지하며, 도시철도 재정 손실의 주된 요인임을 확인했습니다.
* **🔍 특징의 중요성:** 요금 예측에 단순 시간보다 **누적된 CPI 상승 압력**과 **마지막 인상 후 경과 시간**이 결정적인 변수임을 증명했습니다.

<br>
---

<h2 align="center">🛠️ 프로젝트 핵심 기술 스택</h2>
<p align="center">
  프로젝트에 사용된 주요 기술 및 라이브러리입니다.
</p>

### 💻 데이터 분석 및 모델링 환경

[![Numpy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-003D5C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-3E7199?style=for-the-badge&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)

### 🧠 머신러닝 및 통계 모델

[![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![Statsmodels](https://img.shields.io/badge/Statsmodels-1A1A1A?style=for-the-badge&logo=statsmodels&logoColor=white)](https://www.statsmodels.org/stable/index.html)
[![Prophet](https://img.shields.io/badge/Prophet-3B5998?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.github.io/prophet/)

### 💾 버전 관리 (VCS)

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<br>



---

### ➡️ 프로세스 흐름 요약

> 🔍 문제 정의 &rarr; 💾 데이터 수집 &rarr; 🧹 전처리 &rarr; 📉 모델링/분석 &rarr; 📈 시각화 및 보고
