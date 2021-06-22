# Weather-BigData-Contest
* [0613_Data.ipynb](https://github.com/jbeen2/Weather-BigData-Contest/blob/jbeen2/0613_Data.ipynb) : 최종 DataFrame 생성 코드
* [0620_Modeling.ipynb](https://github.com/jbeen2/Weather-BigData-Contest/blob/jbeen2/0613_Modeling.ipynb) : TimeSeries Clustering + ML modeling 

--- 
* [17_LSTM_Causality.ipynb](https://github.com/jbeen2/Weather-BigData-Contest/blob/jbeen2/17_LSTM_Causality.ipynb) : SHAP 
```python
@tensorflow version : 2.0.0 
@shap version : 0.38.2

from tensorflow.compat.v1.keras.backend import get_session
tf.compat.v1.disable_v2_behavior()

!pip install git+https://github.com/janesser/shap.git@bugfix/1694
```
