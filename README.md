# 🎧 SKN25-2nd-1Team

### KKBOX Churn Prediction & Targeting Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange)
![ResNet](https://img.shields.io/badge/Model-ResNet-blue)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-purple)

---

# 📌 1. 팀 소개

본 프로젝트는 5명의 팀원이 참여하여 개발되었습니다:

| 이름 | 역할 | 담당 업무 |
|------|------|----------|
| 김나연 | 팀장/데이터 분석 | EDA 및 데이터 전처리 |
| 박범수 | 모델링 | XGBoost 및 ResNet 모델 개발 |
| 양예승 | 대시보드 | Streamlit UI/UX 설계 |
| 이근혁 | 백엔드 | 모델 추론 및 전략 엔진 |
| 최현우 | 프로젝트 관리 | 일정 조율 및 문서화 |

---

# 📅 2. 프로젝트 기간

2026.02.19 ~ 2026.02.24

---

# 📖 3. 프로젝트 개요

## 📕 프로젝트명

 **KeepTune**

---

## ✅ 프로젝트 배경 및 목적

* 음악 스트리밍 서비스의 사용자 이탈은 수익 감소로 직결
* 단순 예측을 넘어 **이탈 위험 사용자에 대한 전략 수립 자동화** 필요

---

## 🖐️ 프로젝트 소개

KKBox 음악 스트리밍 서비스의 구독자 이탈(Churn)을 예측하는 머신러닝 및 딥러닝 기반 웹 대시보드입니다.  
XGBoost와 ResNet 모델을 활용하여 이탈 예측을 수행하며, Streamlit을 통해 직관적인 사용자 인터페이스를 제공합니다.  
데이터 탐색, 예측, 전략 추천까지 원스톱으로 지원합니다.

---

## ❤️ 기대 효과

* 이탈 예측 정확도 향상으로 마케팅 비용 절감
* 자동화된 전략 추천으로 의사결정 시간 단축
* 고객 유지율 증가 및 수익성 개선

---

## 👤 대상 사용자

* 마케팅 전략 담당자
* CRM 팀
* 데이터 분석가
* 비즈니스 의사결정자

---

# 🛠 4. 기술 스택

### 📊 Data
![Pandas](https://img.shields.io/badge/Pandas-2.3.3-blue)
![NumPy](https://img.shields.io/badge/NumPy-2.4.2-lightblue)
![PyArrow](https://img.shields.io/badge/PyArrow-23.0.1-green)

### 🤖 Modeling
![XGBoost](https://img.shields.io/badge/XGBoost-3.2.0-orange)
![PyTorch](https://img.shields.io/badge/PyTorch-2.10.0-red)
![SHAP](https://img.shields.io/badge/SHAP-0.50.0-purple)

### 📈 Dashboard
![Streamlit](https://img.shields.io/badge/Streamlit-1.54.0-red)

### 🧠 ML Pipeline
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-1.8.0-blue)
![Imbalanced--learn](https://img.shields.io/badge/Imbalanced--learn-0.12.0-yellow)
![Optuna](https://img.shields.io/badge/Optuna-4.7.0-green)

---

# 📂 5. Repository Structure

```
SKN25-2nd-1Team/
│
├── app/                         # 📊 Streamlit 대시보드
│   ├── model_engine/            # 모델 추론 및 전략 엔진
│   ├── app_eda.py               # EDA 페이지
│   ├── app_home.py              # 홈 화면
│   ├── app_predict.py           # 예측 결과 페이지
│   ├── app_strategy.py          # 전략 추천 페이지
│   └── main.py                  # 🚀 대시보드 실행 파일
│
├── data/
│   ├── raw/                     # 원본 데이터
│   └── preprocessed/            # 전처리 데이터
│
├── ml_pipeline/
│   └── train.py                 # 🤖 전처리 및 모델 학습 실행
│
├── models/                      # 💾 학습된 모델 저장
│   ├── xgb_model.pkl           # XGBoost 모델 파일
│   └── resnet_model.pkl        # ResNet 모델 파일
│
├── notebooks/                   # 📓 실험 노트북
│   ├── EDA.ipynb
│   └── modeling_shap.ipynb
│
├── src/                         # ⚙️ 공통 모듈
│   ├── analysis_engine/
│   └── model_loader.py
│
├── requirements.txt
└── README.md
```

---

# 🚀 6. 실행 방법

## 0️⃣ 환경 설정

### Python 버전
- Python 3.12 이상 권장

### 가상환경 생성
```bash
conda create -n keeptune python=3.12
conda activate keeptune
```

### 의존성 설치
```bash
pip install -r requirements.txt
```

### 데이터 준비
프로젝트 실행 전 아래 경로에 데이터 파일이 있어야 합니다. 데이터 파일들은 용량이 크기 때문에 GitHub에 포함되지 않으며, 아래 Google Drive 링크에서 다운로드할 수 있습니다.

[데이터 다운로드 링크](https://drive.google.com/your-link-here)

```
data/kkbox_v3.parquet     ← 전처리 완료 데이터 (필수)
data/raw/*.csv            ← 원본 CSV 파일들
```

## 1️⃣ 모델 학습

```bash
python ml_pipeline/train.py
```

---

## 2️⃣ 대시보드 실행

```bash
streamlit run app.py
```

---

# 📊 7. 수행 결과

## 모델 성능 비교

| 모델 | AP Score | Precision | Recall | F1-Score |
|------|----------|-----------|--------|----------|
| XGBoost | 0.9522 | 0.8319 | 0.9452 | 0.8847 |
| ResNet | 0.9450 | 0.9514 | 0.7011 | 0.8073 |

## 주요 성과
- 2개 모델 앙상블로 예측 정확도 향상
- SHAP을 통한 모델 해석 가능성 제공
- Streamlit 대시보드로 실시간 예측 및 전략 추천

---

# 📝 8. 한 줄 회고

팀원 각자의 한 줄 회고를 여기에 작성하세요.

| 이름 | 한 줄 회고 |
|------|----------|
| 김나연 | . |
| 박범수 | . |
| 양예승 | . |
| 이근혁 | . |
| 최현우 | . |

---

*SKN 25기 2차 프로젝트 - 1팀*
