# Weather-BigData-Contest
* [0613_Data.ipynb](https://github.com/jbeen2/Weather-BigData-Contest/blob/jbeen2/0613_Data.ipynb) : 최종 DataFrame 생성 코드
* [0613_Modeling.ipynb](https://github.com/jbeen2/Weather-BigData-Contest/blob/jbeen2/0613_Modeling.ipynb) : Modeling 코드 
  ```python 
  # 지역별로 모델링 할 때 데이터프레임 이렇게 붙여서 사용하시면 됩니당 
  bty_c0_1 = bty_c0.merge(region_weather('서울'), on="date", how='left')
  ```
