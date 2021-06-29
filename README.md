# 기상청 날씨 빅데이터 콘테스트 
## [민간협력형] 날씨에 따른 소비패턴 분석 

## 1. File Directory    

데이터를 다운로드 받아주시고, 가장 상위 경로에서 ipynb 파일을 순서대로 실행해 주시기 바랍니다.

```shell
빠른이들
├── 참가자 명단 서약서 공모요약서.hwp 
├── 빠른이들_최종공모안.pptx
├── 빠른이들_최종공모안.pdf
├── README.md
│
├── 1-Data-Preprocessing.ipynb
├── 2-Correlation.ipynb  
├── 3-Granger-Causality-Test.ipynb 
├── 4-LSTM.ipynb 
├── 5-TSClustering&ML.ipynb
├── 6-Recommender-System.ipynb
│
├── dataload.py
├── HIVEdataload.R 		        # 날씨마루 데이터 불러오기 (SQL) 
│
├── 기상청데이터
├── 내부데이터  		 
│   ├── buy2018_1.csv 
│   ├── ...
│   └── sns2019_2.csv  		   
│
├── 외부데이터      
│   ├── trendsearch.csv  		# 네이버 검색어 트렌드 
│   ├── trend_with_weather.csv  	# 네이버 날씨 정보 검색어 트렌드 
│   ├── 시도별_주민등록_인구현황.csv  	# 통계청 시도별 총인구수  
│   ├── 소비자심리지수_seoul_past.csv  	# 통계청 서울 소비자심리지수  
│   ├── 소비자심리지수_other_past.csv  	# 통계청 지역별 소비자심리지수  
│   │
│   ├── 2018  		                # 2018 에어코리아 미세먼지 데이터  
│   │    ├── 2018년 1분기.xlsx
│   │    └── ...  
│   └── 2019  		                # 2019 에어코리아 미세먼지 데이터  
│        ├── 2018년 1월.xlsx
│        └── ...    
│
├── 최종데이터   # [분석 과정 중 생성된 중간 결과물] 최종 분석에 사용되는 데이터 
│
└── 최종결과     
    ├── LSTM_result.csv  		  # 정상시계열 상품군 예측 결과 
    └── nonst_high_for_dashboard_0622.csv # 비정상시계열 상품군 예측 결과  
 

```


<br>


## 2. PROCESS  
1. Data Preprocessing : 분석에 사용하는 데이터를 전처리하는 과정입니다. 
2. Correlation : 상관관계 높은 상품을 선택하고, ADF Test를 통해 정상성을 검정합니다. 
3. Granger Causality Test : VAR/VECM, 그래인저 인과관계 검정을 수행합니다. 
4. LSTM : Deep Learning 모델을 통해 정상시계열 상품군의 추세를 예측합니다. 
5. TSClustering & ML : 시계열 클러스터링을 진행하고, Machine Learning 모델을 통해 비정상시계열 상품군의 추세를 예측합니다. 
6. Recommender System : 상품의 특성을 반영하여 유사한 상품을 추천합니다. 


<br>


## 3. Dashboard 
https://public.tableau.com/app/profile/bomin5781/viz/FinalDashboard_16246720253230/sheet13  <br>
해당 링크에서, AI 기반 온라인 소비패턴 분석 서비스를 경험하실 수 있습니다.  <br>
(링크가 있는 사용자만 접근 가능하며, 사용자가 데이터를 다운로드 할 수 없습니다.) 

