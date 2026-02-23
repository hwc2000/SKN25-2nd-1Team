import pandas as pd
import polars as pl
import numpy as np
import lightgbm as lgb
import pickle
import os
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 0. root 경로 선언
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
SAVE_DIR =ROOT_DIR / "data" / "preprocessed" # 전처리 된 데이터 저장 경로
MODELS_DIR = ROOT_DIR / "models" # 모델 저장 경로

with open(SAVE_DIR / "kkbox_data.pkl", "rb") as f:
    df = pickle.load(f)

# 3. 학습 준비
print("Step 3. 학습 데이터 준비 중...")
drop_cols = ['msno', 'is_churn', 'registration_init_time', 'gender', 'membership_expire_date']
X = df.drop(columns=[c for c in drop_cols if c in df.columns])
y = df['is_churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. 5종 모델 학습 및 저장
print("Step 4. 5종 모델 학습 및 저장 중...")
models = {
    'xgb': XGBClassifier(n_estimators=100, random_state=42),
    'lgbm': lgb.LGBMClassifier(n_estimators=100, random_state=42, verbosity=-1),
    'rf': RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
    'gbm': GradientBoostingClassifier(n_estimators=100, random_state=42),
    'mlp': MLPClassifier(hidden_layer_sizes=(128, 64, 32), random_state=42)
}

import pickle

# ==============================
# 모델 저장
# ==============================
for name, model in models.items():
    if name == 'mlp':
        model.fit(X_train_scaled, y_train)
    else:
        model.fit(X_train, y_train)

    # 모델 저장
    with open(MODELS_DIR / f"{name}_model.pkl", "wb") as f:
        pickle.dump(model, f)


# 데이터 저장
with open(SAVE_DIR / "kkbox_data.pkl", "wb") as f:
    pickle.dump(df, f)

# feature 이름 저장
with open(SAVE_DIR / "feature_names.pkl", "wb") as f:
    pickle.dump(list(X.columns), f)

print("모든 모델 pickle 저장 완료!")