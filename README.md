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

## 프로젝트 수행 절차  
문제정의 --> 데이터수집 --> 전처리 --> 모델링/분석 --> 시각화 및 보고


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

---

### ➡️ 프로세스 흐름 요약

> 🔍 문제 정의 &rarr; 💾 데이터 수집 &rarr; 🧹 전처리 &rarr; 📉 모델링/분석 &rarr; 📈 시각화 및 보고
