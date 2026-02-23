import pandas as pd
import polars as pl
import numpy as np
import pickle
import os


# 0. root 경로 선언
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data" / "raw" #전처리 전 경로
SAVE_DIR =ROOT_DIR / "data" / "preprocessed" # 전처리 된 데이터 저장 경로

# 1. 데이터 로드
print("Step 1. 데이터를 불러오는 중입니다...")
train = pl.read_csv(DATA_DIR / "train_v2.csv").to_pandas()
members = pl.read_csv(DATA_DIR / "members_v3.csv").to_pandas()
transactions = pl.read_csv(DATA_DIR / "transactions_v2.csv").to_pandas()
user_logs = pl.read_csv(DATA_DIR / "user_logs_v2.csv", n_rows=5_000_000).to_pandas()

# 2. 데이터 병합 및 변수 생성
print("Step 2. 데이터 병합 및 변수 생성 중...")
transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'], format='%Y%m%d')
transactions['membership_expire_date'] = pd.to_datetime(transactions['membership_expire_date'], format='%Y%m%d')
transactions['membership_duration'] = (transactions['membership_expire_date'] - transactions['transaction_date']).dt.days

txn_agg = transactions.groupby('msno').agg(
    txn_cnt=('msno', 'count'),
    total_paid=('actual_amount_paid', 'sum'),
    avg_plan_days=('payment_plan_days', 'mean'),
    auto_renew_rate=('is_auto_renew', 'mean'),
    cancel_rate=('is_cancel', 'mean')
).reset_index()

log_agg = user_logs.groupby('msno').agg(
    total_secs_mean=('total_secs', 'mean'),
    num_unq_mean=('num_unq', 'mean')
).reset_index()

df = pd.merge(train, txn_agg, on='msno', how='left')
df = pd.merge(df, log_agg, on='msno', how='left')
df = pd.merge(df, members, on='msno', how='left')
df = df.fillna(0) # 결측치 처리

with open(SAVE_DIR / "kkbox_data.pkl", "wb") as f:
    pickle.dump(df, f)