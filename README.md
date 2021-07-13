# 2021 기상청 날씨 빅데이터 콘테스트 (수정 중 ~) 
### 민간협력형 : [날씨에 따른 소비패턴 분석](https://user-images.githubusercontent.com/43749571/125427337-41b203f1-078e-4354-a3d6-d78688f9bdaa.png) ⛅️  

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

주어진 내부 데이터는 **2018.01 ~ 2019.12** 2년 동안의 **온라인 구매이력**과 **소셜 데이터** 입니다.  
2년간의 **날씨 데이터, 외부 이슈 데이터, 지역 데이터**를 추가로 수집해 분석하였습니다.

<p align="center"><img src="https://user-images.githubusercontent.com/43749571/124492612-aaf46e00-ddef-11eb-8d38-bb1041032009.jpg"></p>
<p align="center"><img src="https://user-images.githubusercontent.com/43749571/124492616-ac259b00-ddef-11eb-9421-d378ded22269.jpg"></p>

<br> 

## 3. PROCESS  

<p align="center"><img src="https://user-images.githubusercontent.com/43749571/124492620-ad56c800-ddef-11eb-984b-2b0b9da237be.jpg"></p>

1. **`상품 필터링`** : **Correlation & 단위근 검정**   
   - Spearman Correlation 기준으로, 날씨와 상관관계 높은 상품을 선택합니다.
   - 날씨와 상관관계가 높은 상품에 대하여, 2년간의 일별 판매량 추이에 대해 ADF Test 를 통해  <br> 
     정상 (일별 판매량 변동성이 크지 않고, 계절성이 크지 않은 상품 = 시계열 분석법 사용 가능),  <br> 
     비정상 (일별 판매량 변동성이 크고, 계절에 따른 판매량 차이가 큰 상품) 시계열 상품군으로 구분합니다. 

2. **`인과관계 검정`** : **Granger Causality Test** 
   - 날씨가 상품 판매량에 영향을 미치는, 날씨변수와 인과관계가 있는 상품군을 선택하기 위한 과정입니다. 
   - 날씨・상품 판매량이 모두 정상 시계열인 경우 VAR & 그래인저 인과관계 검정을 수행하며,  
     날씨・상품 판매량 중 하나라도 비정상 시계열인 경우 VECM & 그래인저 인과관계 검정을 수행합니다. 

3. **`상품 판매량 예측`** : **LSTM / Time Series Clustering + Machine Learning** 
   - 정상 시계열 상품의 경우, 인과관계가 있는 날씨 변수를 선택하여 LSTM 을 통해 예측합니다. 
   - 비정상 시계열 상품군의 경우, 시계열 클러스터링을 통해 비슷한 추세를 가진 상품군끼리 묶은 후,    
     각 군집별로 Machine Learning 모델을 통해 상품 판매량 추세를 예측합니다.  
   - 날씨의 영향력을 파악하기 위해, 날씨 변수 별로 시간에 따른 SHAP 을 시각화하여 결과를 해석했습니다. 

4. **`Recommender System`** : **날씨를 고려한 추천시스템** 
   - item-based CF 기반으로, 해당 상품의 특성을 반영하여 다른 상품을 추천합니다.  
   - 고객 타겟층을 설정하고, 날씨(강수 여부/미세먼지)를 설정해 유사도 기반으로 상품을 추천합니다.

<br>

5. **`Dashboard`** : **AI 기반 온라인 소비패턴 분석 서비스** 
   <img src="https://user-images.githubusercontent.com/43749571/124492621-adef5e80-ddef-11eb-8497-16cc5963bd73.png"></p>
   - 고객 맞춤형 전략을 위한 날씨 빅데이터 마켓팅 플랫폼 [Dashboard](https://public.tableau.com/app/profile/bomin5781/viz/FinalDashboard_16246720253230/sheet13) 입니다. 
   - 1 상품의 특성 (날씨와의 인과관계 여부), 2 날씨와의 관계, 3 상품 분석 (성・연령별 구매건수 추이),    
     4 SNS 언급량 (상품 판매량에 유의한 lag + 언급량 추세),  5 추천시스템  으로 구성되어 있습니다.

<br> 

## 5. Members : Team 빠른이들 (일단 분신술 .. 감생감사재빈 * 3) 


<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable --> 

<table>
  <tr>
    <td align="center"><a href="https://github.com/bominkm"><img src="https://user-images.githubusercontent.com/43749571/125430192-d8a34ef9-e179-49b0-ac67-a6fa65d3b0c7.jpeg" width="150" height="150"><br /><sub><b>Bomin Kim</b></sub></td>
    <td align="center"><a href="https://github.com/yoonjong12"><img src="https://user-images.githubusercontent.com/43749571/125430192-d8a34ef9-e179-49b0-ac67-a6fa65d3b0c7.jpeg" width="150" height="150"><br /><sub><b>Jaebeen Lee</b></sub></td>
    <td align="center"><a href="https://github.com/jbeen2"><img src="https://user-images.githubusercontent.com/43749571/125430192-d8a34ef9-e179-49b0-ac67-a6fa65d3b0c7.jpeg" width="150" height="150"><br /><sub><b>Hyerin Lee</b></sub></td>
  </tr>
</table>

<br> 

## 6. File Directory 

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

