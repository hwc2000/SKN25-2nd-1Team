import pandas as pd
import numpy as np
import pickle
import os
import joblib
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier # ResNet 대용 신경망 모델
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# 0. 경로 선언 (프로젝트 루트 기준)
ROOT_DIR = Path(__file__).resolve().parents[1]
SAVE_DIR = ROOT_DIR / "data" / "preprocessed"
MODELS_DIR = ROOT_DIR / "models"

# 저장 경로가 없으면 생성
SAVE_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# 1. 데이터 로드
print("Step 1. 데이터 로딩 중...")
with open(SAVE_DIR / "kkbox_data.pkl", "rb") as f:
    df = pickle.load(f)

# 2. 학습 준비
print("Step 2. 학습 데이터 준비 중...")
# 불필요한 컬럼 제거
drop_cols = ['msno', 'is_churn', 'registration_init_time', 'gender', 'membership_expire_date']
X = df.drop(columns=[c for c in drop_cols if c in df.columns])
y = df['is_churn']

# 데이터 분할 (계층적 샘플링 적용)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 스케일링 (ResNet/신경망 모델 필수 과정)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. 2종 핵심 모델 학습
print("Step 3. XGBoost & ResNet(MLP) 모델 학습 시작...")

# (1) XGBoost: 정형 데이터의 강력한 분류 성능
print("- XGBoost 학습 중...")
xgb_model = XGBClassifier(n_estimators=100, random_state=42, use_label_encoder=False)
xgb_model.fit(X_train, y_train)

# (2) ResNet 대용 MLP: 다차원 패턴 추출 (ResNet 구조의 신경망 지향)
print("- ResNet(MLP) 학습 중...")
resnet_model = MLPClassifier(
    hidden_layer_sizes=(256, 128, 64), 
    activation='relu', 
    solver='adam', 
    max_iter=300, 
    random_state=42
)
resnet_model.fit(X_train_scaled, y_train)

# 4. 모델 및 관련 자산 저장
print("Step 4. 결과 저장 중...")

# 모델 저장 (joblib이 pickle보다 대용량 수치 데이터에 유리합니다)
joblib.dump(xgb_model, MODELS_DIR / "xgb_model.pkl")
joblib.dump(resnet_model, MODELS_DIR / "resnet_model.pkl")

# 전처리 도구 저장 (예측 시 동일한 스케일링 적용을 위해 필수)
joblib.dump(scaler, SAVE_DIR / "scaler.pkl")

# 피처 이름 저장
with open(SAVE_DIR / "feature_names.pkl", "wb") as f:
    pickle.dump(list(X.columns), f)

print(f"✅ 모든 과정 완료! 모델 저장 경로: {MODELS_DIR}")