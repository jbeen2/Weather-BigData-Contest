# Weather-BigData-Contest
2021 기상청 날씨 빅데이터 콘테스트 

1. EDA : 온라인 구매건수, 키워드 관련 문서량 데이터 EDA
2. Time-Series-Clustering : 2018년, 2019년 날짜 기준으로 평균
3. Time-Series-Clustering-match-day: 2018년, 2019년 요일 기준으로 평균
4. CSI: 소비자심리지수 raw 데이터 전처리
5. CSI-for-Weather: 날씨 지수 생성 함수
6. Sampling: 일주일마다 랜덤한 요일 뽑아 train, test split하는 함수
7. Online-with-Weather: 주어진 데이터에 날씨 지수 데이터 추가
8. Appliance-Correlation: 대분류 냉난방가전과 상관관계가 높은 지역 선택
9. Modeling-Baseline: Machine Learning Baseline
10. Time-Series-Clustering-Scaling: 스케일링
11. Modeling-Scaling: Scaling 후 Machine Learning
12. Population-Weight: 시도별 인구수를 기반으로 한 가중치
13. Modeling-Filtering: Machine Learning 해당 소품목만
14. Final-EDA: 논리적 흐름을 위한 EDA 
17. LSTM-Causality: Causality 있는 날씨변수만 사용