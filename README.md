# 2021 기상청 날씨 빅데이터 콘테스트 
### 민간협력형 : [날씨에 따른 소비패턴 분석](https://user-images.githubusercontent.com/43749571/125427337-41b203f1-078e-4354-a3d6-d78688f9bdaa.png) ⛅️  

<p align="center"><img src="https://user-images.githubusercontent.com/43749571/124492604-a760e700-ddef-11eb-9896-c4e869d4c392.jpg"></p>

* **온라인 판매 데이터**로 날씨에 따른 소비패턴을 **분석**하고 **예측**하여, 날씨와 아이템 특성을 반영한 상품을 **추천**합니다. 
* **[보고서](https://drive.google.com/file/d/1HJW8l0JAg-QLCYRdD1vkn7D49VwGW0s4/view)** 를 통해 **분석 과정**에 대해 확인하실 수 있으며, 
  **Dashboard** 를 통해 **날씨 빅데이터 마케팅 플랫폼**을 경험하실 수 있습니다.


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

<p align="center"><img src="https://user-images.githubusercontent.com/43749571/128128489-b265d3f4-9cd0-45cd-b561-9894fc0d553f.jpg"></p>

<br> 

## 3. PROCESS  
분석은 다음 순서로 진행되며, 분석 과정을 **클릭**하시면 자세한 설명을 참고하실 수 있습니다. 

<p align="center"><img src="https://user-images.githubusercontent.com/43749571/128452658-261b243a-cf24-4d23-ad34-32504a897d65.jpg"></p>

<details> 
 <summary> 1. <b> <code>상품 필터링 & 분류</code> </b>  : <a href="https://github.com/jbeen2/Weather-BigData-Contest/blob/main/2-Correlation.ipynb">상관관계 분석 & 단위근 검정</a> </summary>  
   <ul> 
    <br>
    <li> <b>Spearman Correlation</b> 기준으로, 날씨와 상관관계 높은 상품을 선택합니다. </li>  
    <li> 날씨와 상관관계가 높은 상품에 대하여, 2년간의 일별 판매량 추이에 대해 <b>ADF Test</b> 를 통해  <br> 
     <b>정상</b> (일별 판매량 변동성이 크지 않고, 계절성이 크지 않은 상품),  <br> 
     <b>비정상</b> (일별 판매량 변동성이 크고, 계절에 따른 판매량 차이가 큰 상품) 시계열 상품군으로 구분합니다. </li>  <br>
    </ul>
</details>

<details> 
 <summary> 2. <b> <code>날씨와의 인과관계 검정</code> </b>  : <a href="https://github.com/jbeen2/Weather-BigData-Contest/blob/main/3-Granger-Causality-Test.ipynb">Granger Causality Test</a></summary> 
  <ul> 
   <br>
   <li> 날씨가 상품 판매량에 영향을 미치는, 날씨변수와 인과관계가 있는 상품군을 선택하기 위한 과정입니다. </li>  
   <li> 날씨・상품 판매량이 모두 정상 시계열인 경우 <b>VAR & Granger 인과관계 검정</b>을 수행하며,  <br> 
     날씨・상품 판매량 중 하나라도 비정상 시계열인 경우 <b>VECM & Granger 인과관계 검정</b>을 수행합니다. </li>  <br>
  </ul>
</details>
 
<details> 
 <summary> 3. <b> <code>상품 판매량 예측</code>  </b> : <a href="https://github.com/jbeen2/Weather-BigData-Contest/blob/main/4-LSTM.ipynb">LSTM</a> / <a href="https://github.com/jbeen2/Weather-BigData-Contest/blob/main/5-TSClustering_ML.ipynb">Time Series Clustering + Machine Learning</a> </summary> 
  <ul> 
   <br>
   <li> 정상 시계열 상품의 경우, 인과관계가 있는 날씨 변수를 선택하여 <b>LSTM</b> 을 통해 예측합니다. </li> 
   <li> 비정상 시계열 상품의 경우, <b>Time Series Clustering</b>을 통해 비슷한 추세를 가진 상품군끼리 묶은 후,  <br>    
     각 군집별로 <b>Machine Learning</b> 모델을 통해 상품 판매량 추세를 예측합니다.  </li> 
   <li> 날씨의 영향력을 파악하기 위해, 날씨 변수 별로 시간에 따른 <b>SHAP</b> 을 시각화하여 결과를 해석했습니다. </li> <br>
 </ul>
</details>

<details> 
 <summary> 4. <b> <code>날씨 기반 추천시스템</code> </b>  : <a href="https://github.com/jbeen2/Weather-BigData-Contest/blob/main/6-Recommender-System.ipynb">Recommender System</a></summary> 
  <ul> 
   <br>
   <li> <b>item-based CF</b> 기반으로, 해당 상품의 특성을 반영하여 다른 상품을 추천합니다. </li>  
   <li> <b>고객 타겟층</b>을 설정하고, <b>날씨(강수 여부/미세먼지)</b>를 설정해 유사도 기반으로 상품을 추천합니다. </li> <br>
  </ul> 
</details> 
 
<details> 
 <summary> 5. <b> <code>Dashboard</code> </b>  : 온라인 소비패턴 분석 서비스 </summary> 
   <br>
   <img src="https://user-images.githubusercontent.com/43749571/128128764-12bef478-5158-4c34-bd5d-795977c7db67.png"></p>
   <ul> 
    <li> 고객 맞춤형 전략을 위한 <b>날씨 빅데이터 마켓팅 플랫폼</b> Dashboard 입니다. </li>  
    <li> <b>1</b> 상품의 특성 (날씨와의 인과관계 여부), <b>2</b> 날씨와의 관계, <b>3</b> 상품 분석 (성・연령별 구매건수 추이), <br>     
      <b>4</b> SNS 언급량 (상품 판매량에 유의한 lag + 언급량 추세),  <b>5</b> 추천시스템  으로 구성되어 있습니다. </li>  
    <li> 서약 내용에 따라 Dashboard 링크는 제공하지 않습니다. </li>  <br> 
  </ul> 
</details> 

<br> 

## 4. Members : Team 빠른이들 


<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable --> 

<table>
  <tr>
    <td align="center"><a href="https://github.com/bominkm"><img src="https://user-images.githubusercontent.com/43749571/130727497-aa668081-4225-4852-af95-6bb3e18aec4d.JPG" width="150" height="150"><br /><sub><b>Bomin Kim</b></sub></td>
    <td align="center"><a href="https://github.com/jbeen2"><img src="https://user-images.githubusercontent.com/43749571/130727477-635610c5-09fb-4091-b930-8008fe97134e.jpg" width="150" height="150"><br /><sub><b>Jaebeen Lee</b></sub></td>
    <td align="center"><a href="https://github.com/hrlee113"><img src="https://user-images.githubusercontent.com/43749571/130727490-606f2a83-88f9-4a8a-8a7a-04148190f19c.JPG" width="150" height="150"><br /><sub><b>Hyerin Lee</b></sub></td>
  </tr>
</table>

<br> 

## 5. File Directory 

```shell
빠른이들
├── 1-Data-Preprocessing.ipynb  
├── 2-Correlation.ipynb  
├── 3-Granger-Causality-Test.ipynb 
├── 4-LSTM.ipynb 
├── 5-TSClustering_ML.ipynb
├── 6-Recommender-System.ipynb
│
├── dataload.py
├── HIVEdataload.R 		        # SQL : 날씨마루 데이터 불러오기 
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
├── 📂 최종데이터  		          # 분석 과정 중 생성된 데이터 
└── 📂 최종결과     
    ├── LSTM_result.csv  		  # 정상시계열 상품군 예측 결과 
    └── nonst_high_for_dashboard_0622.csv # 비정상시계열 상품군 예측 결과  
 

```

