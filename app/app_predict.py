# 0. 루트 경로 선언
import os
import sys

from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st
from src.model_loader import predict_churn

def run_predict():
    st.title("🔍 실시간 이탈 진단 및 다각도 방어 전략")
    st.markdown("---")
    
    # 1. 세션 상태 관리 (생략 가능하나 이전 코드 유지 권장)
    if 'predict_done' not in st.session_state:
        st.session_state.predict_done = False
    if 'result_data' not in st.session_state:
        st.session_state.result_data = None

    # 2. 데이터 입력 섹션 (근혁님 기존 코드 유지)
    col1, col2 = st.columns(2)
    with col1:
        auto_renew = st.radio("💳 자동 결제 여부 (1:설정, 0:해지)", [1, 0], key="input_auto")
        total_secs = st.number_input("🎧 일평균 청취 시간(초)", 0, 86400, 5000, key="input_secs")
    with col2:
        cancel_rate = st.slider("⚠️ 과거 해지 시도 비율", 0.0, 1.0, 0.1, key="input_cancel")
        txn_cnt = st.number_input("💰 총 결제 횟수", 1, 100, 10, key="input_txn")

    input_data = {'auto_renew_rate': auto_renew, 'total_secs_mean': total_secs, 'cancel_rate': cancel_rate, 'txn_cnt': txn_cnt}

    if st.button("🚀 종합 진단 및 전략 시뮬레이션 실행", use_container_width=True):
        p1, p2, p3, avg_p = predict_churn(input_data)
        st.session_state.predict_done = True
        st.session_state.result_data = {'avg_p': avg_p, 'input': input_data}

    # 3. 진단 결과 및 구체적 액션 플랜
    if st.session_state.predict_done:
        res = st.session_state.result_data
        avg_p = res['avg_p']
        data_dict = res['input']

        # 위험도 상단 바 (생략 가능하나 가독성 위해 유지)
        risk_score = avg_p * 100
        st.markdown(f"### 현재 유저 이탈 위험도: **{risk_score:.1f}%**")
        st.progress(avg_p)

        st.markdown("---")
        st.subheader("📋 전략별 상세 실행 가이드 (How-to)")

        # 각 전략별 시뮬레이션 계산
        def get_p(d): _, _, _, p = predict_churn(d); return p
        
        # 전략 데이터 생성
        s1 = data_dict.copy(); s1['auto_renew_rate'] = 1.0
        s2 = data_dict.copy(); s2['cancel_rate'] = max(0, data_dict['cancel_rate'] - 0.5)
        s3 = data_dict.copy(); s3['total_secs_mean'] += 7200

        p_s1, p_s2, p_s3 = get_p(s1), get_p(s2), get_p(s3)

        # 구체적인 방법론 배치
        tab1, tab2, tab3 = st.tabs(["💳 자동결제 유도", "🛡️ 심리 케어", "🎧 몰입도 강화"])

        with tab1:
            c1, c2 = st.columns([1, 2])
            c1.metric("이탈률 변화", f"{p_s1*100:.1f}%", f"{(p_s1-avg_p)*100:.1f}%p", delta_color="inverse")
            with c2:
                st.markdown("**[실행 방법]**")
                st.write("1. 자동결제 전환 시 '첫 달 100원' 또는 '영구 10% 할인' 프로모션 노출")
                st.write("2. 간편 결제(KakaoPay, ApplePay) 연동을 통한 결제 허들 제거")
                st.write("3. 구독 만료 3일 전 갱신 실패 알림 및 전환 혜택 푸시 발송")

        with tab2:
            c1, c2 = st.columns([1, 2])
            c1.metric("이탈률 변화", f"{p_s2*100:.1f}%", f"{(p_s2-avg_p)*100:.1f}%p", delta_color="inverse")
            with c2:
                st.markdown("**[실행 방법]**")
                st.write("1. 해지 페이지 진입 시 '해지 방어용' 특별 혜택(구독 연장권 등) 팝업 제공")
                st.write("2. 이탈 징후 고객 대상 1:1 불만 접수 설문 및 VIP 전담 상담 연결")
                st.write("3. 서비스 중단 시 사라지는 데이터(플레이리스트 등)를 강조하여 손실 회피 심리 자극")

        with tab3:
            c1, c2 = st.columns([1, 2])
            c1.metric("이탈률 변화", f"{p_s3*100:.1f}%", f"{(p_s3-avg_p)*100:.1f}%p", delta_color="inverse")
            with c2:
                st.markdown("**[실행 방법]**")
                st.write("1. 유저 선호 장르 기반의 '이번 주 신곡' 개인화 큐레이션 강화")
                st.write("2. 일간/주간 스트리밍 미션 달성 시 포인트 지급 (게이미피케이션 요소)")
                st.write("3. 커뮤니티 기능(댓글, 공유) 유도로 서비스 내 인간적 유대감 형성")