# 2021 기상청 날씨 빅데이터 콘테스트 (수정 중 ~) 
### 민간협력형 : [날씨에 따른 소비패턴 분석](https://bd.kma.go.kr/contest/info_01.do) ⛅️ 

<p align="center"><img src="https://user-images.githubusercontent.com/43749571/124492604-a760e700-ddef-11eb-9896-c4e869d4c392.jpg"></p>

* **온라인 판매 데이터**로 날씨에 따른 소비패턴을 **분석**하고 **예측**하여, 날씨와 아이템 특성을 반영한 상품을 **추천**합니다. 
* **[보고서](https://drive.google.com/file/d/1HJW8l0JAg-QLCYRdD1vkn7D49VwGW0s4/view)** 를 통해 **분석 과정**에 대해 확인하실 수 있으며, 
  **[Dashboard](https://public.tableau.com/app/profile/bomin5781/viz/FinalDashboard_16246720253230/sheet13)** 를 통해 **날씨 빅데이터 마케팅 플랫폼**을 경험하실 수 있습니다.


<br> 

## 1. Goal 

- [x] 날씨에 민감한 상품군 분석
- [x] 소비패턴 트렌드 분석
- [x] 날씨에 따른 수요 예측
- [x] 결과 활용 방안 제시 

<br> 

## 2. Data

분석에 사용된 데이터는 다음과 같으며, 해당 경로에 데이터를 다운로드 받아주시길 바랍니다. 

<p align="center"><img src="https://user-images.githubusercontent.com/43749571/124492612-aaf46e00-ddef-11eb-8d38-bb1041032009.jpg"></p>
<p align="center"><img src="https://user-images.githubusercontent.com/43749571/124492616-ac259b00-ddef-11eb-9421-d378ded22269.jpg"></p>


```shell
빠른이들
├── 1-Data-Preprocessing.ipynb
├── 2-Correlation.ipynb  
├── 3-Granger-Causality-Test.ipynb 
├── 4-LSTM.ipynb 
├── 5-TSClustering&ML.ipynb
├── 6-Recommender-System.ipynb
│
├── dataload.py
├── HIVEdataload.R 		        # (SQL) 날씨마루 데이터 불러오기 
│
├── 📂 기상청데이터
├── 📂 내부데이터  		 
│   ├── buy2018_1.csv 
│   ├── ...
│   └── sns2019_2.csv  		   
│
├── 📂 외부데이터      
│   ├── trendsearch.csv  		# 네이버 검색어 트렌드 
│   ├── trend_with_weather.csv  	# 네이버 날씨 정보 검색어 트렌드 
│   ├── 시도별_주민등록_인구현황.csv  	# 통계청 시도별 총인구수  
│   ├── 소비자심리지수_seoul_past.csv  	# 통계청 서울 소비자심리지수  
│   ├── 소비자심리지수_other_past.csv  	# 통계청 지역별 소비자심리지수  
│   │
│   ├── 📂 2018  		        # 2018 에어코리아 미세먼지 데이터  
│   │    ├── 2018년 1분기.xlsx
│   │    └── ...  
│   └── 📂 2019  		        # 2019 에어코리아 미세먼지 데이터  
│        ├── 2018년 1월.xlsx
│        └── ...    
│
├── 📂 최종데이터   # [분석 과정 중 생성된 중간 결과물] 최종 분석에 사용되는 데이터 
│
└── 📂 최종결과     
    ├── LSTM_result.csv  		  # 정상시계열 상품군 예측 결과 
    └── nonst_high_for_dashboard_0622.csv # 비정상시계열 상품군 예측 결과  
 

```

<br> 

## 3. PROCESS  

<p align="center"><img src="https://user-images.githubusercontent.com/43749571/124492620-ad56c800-ddef-11eb-984b-2b0b9da237be.jpg"></p>

1. Data Preprocessing : 분석에 사용하는 데이터를 전처리하는 과정입니다. 
2. Correlation : 상관관계 높은 상품을 선택하고, ADF Test를 통해 정상성을 검정합니다. 
3. Granger Causality Test : VAR/VECM, 그래인저 인과관계 검정을 수행합니다. 
4. LSTM : Deep Learning 을 통해 정상시계열 상품군의 추세를 예측합니다. 
5. TSClustering & ML : 시계열 클러스터링을 진행하고, Machine Learning 을 통해 비정상시계열 상품군의 추세를 예측합니다. 
6. Recommender System : item-based CF 기반으로, 날씨를 고려해 상품을 추천합니다. 

<br> 

## 4. Dashboard 

<p align="center"><img src="https://user-images.githubusercontent.com/43749571/124492621-adef5e80-ddef-11eb-8497-16cc5963bd73.png"></p>


<br> 

## 5. Members : Team 빠른이들 

<br> 
