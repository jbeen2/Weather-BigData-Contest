import numpy as np
import pandas as pd
import datetime as datetime

def load_buy():
    # 온라인 구매 이력
    # 날짜, 성별, 연령대, 큰 카테고리, 작은 카테고리, 구매량    
    
    buy2018_1 = pd.read_csv('내부데이터/buy2018_1.csv', encoding='cp949')
    buy2018_2 = pd.read_csv('내부데이터/buy2018_2.csv', encoding='cp949') 
    buy2019_1 = pd.read_csv('내부데이터/buy2019_1.csv', encoding='cp949') 
    buy2019_2 = pd.read_csv('내부데이터/buy2019_2.csv', encoding='cp949')

    buy2018_1 = buy2018_1.iloc[:,1:]
    buy2018_2 = buy2018_2.iloc[:,1:]
    buy2019_1 = buy2019_1.iloc[:,1:]
    buy2019_2 = buy2019_2.iloc[:,1:]

    buy2018_1.columns = ['date', 'sex', 'age', 'big_cat', 'sm_cat', 'qty']
    buy2018_2.columns = ['date', 'sex', 'age', 'big_cat', 'sm_cat', 'qty']
    buy2019_1.columns = ['date', 'sex', 'age', 'big_cat', 'sm_cat', 'qty']
    buy2019_2.columns = ['date', 'sex', 'age', 'big_cat', 'sm_cat', 'qty']

    buy_full = pd.concat([buy2018_1, buy2018_2, buy2019_1, buy2019_2], axis=0)
    buy_full = buy_full.reset_index(drop=True)
    # buy_full['date'] = buy_full['date'].apply(lambda x : pd.to_datetime(str(x), format='%Y-%m-%d'))
    return buy_full


def load_sns():
    # 소셜 데이터 
    # 날짜, 큰 카테고리, 작은 카테고리, 구매량

    sns2018_1 = pd.read_csv('내부데이터/sns2018_1.csv', encoding='cp949') 
    sns2018_2 = pd.read_csv('내부데이터/sns2018_2.csv', encoding='cp949') 
    sns2019_1 = pd.read_csv('내부데이터/sns2019_1.csv', encoding='cp949') 
    sns2019_2 = pd.read_csv('내부데이터/sns2019_2.csv', encoding='cp949')

    sns2018_1 = sns2018_1.iloc[:,1:]
    sns2018_2 = sns2018_2.iloc[:,1:]
    sns2019_1 = sns2019_1.iloc[:,1:]
    sns2019_2 = sns2019_2.iloc[:,1:]

    sns2018_1.columns = ['date', 'big_cat', 'sm_cat', 'cnt']
    sns2018_2.columns = ['date', 'big_cat', 'sm_cat', 'cnt']
    sns2019_1.columns = ['date', 'big_cat', 'sm_cat', 'cnt']
    sns2019_2.columns = ['date', 'big_cat', 'sm_cat', 'cnt']

    sns_full = pd.concat([sns2018_1, sns2018_2, sns2019_1, sns2019_2], axis=0)
    # sns_full['date'] = sns_full['date'].apply(lambda x : pd.to_datetime(str(x), format='%Y-%m-%d'))
    return sns_full


def load_weather(val_name):
    # 날씨 데이터
    
    # 기온
    temp2018 = pd.read_csv('기상청데이터/temp2018.csv', encoding='cp949').iloc[:,1:]
    temp2019 = pd.read_csv('기상청데이터/temp2019.csv', encoding='cp949').iloc[:,1:]
    temp = pd.concat([temp2018, temp2019], axis=0)
    
    # 강수
    rain2018 = pd.read_csv('기상청데이터/rain2018.csv', encoding='cp949').iloc[:,1:]
    rain2019 = pd.read_csv('기상청데이터/rain2019.csv', encoding='cp949').iloc[:,1:]
    rain = pd.concat([rain2018, rain2019], axis=0)
    
    # 풍속
    wind2018 = pd.read_csv('기상청데이터/wind2018.csv', encoding='cp949').iloc[:,1:]
    wind2019 = pd.read_csv('기상청데이터/wind2019.csv', encoding='cp949').iloc[:,1:]
    wind = pd.concat([wind2018, wind2019], axis=0)
    
    # 습도
    humid2018 = pd.read_csv('기상청데이터/humid2018.csv', encoding='cp949').iloc[:,1:]
    humid2019 = pd.read_csv('기상청데이터/humid2019.csv', encoding='cp949').iloc[:,1:]
    humid = pd.concat([humid2018, humid2019], axis=0)

    # 일조시간
    sun2018 = pd.read_csv('기상청데이터/sun2018.csv', encoding='cp949').iloc[:,1:] 
    sun2019 = pd.read_csv('기상청데이터/sun2019.csv', encoding='cp949').iloc[:,1:]
    sun = pd.concat([sun2018, sun2019], axis=0)

    # 기압 
    press2018 = pd.read_csv('기상청데이터/DB_AWS_PRSR_DD_2018.csv', encoding='cp949').iloc[:,1:]
    press2019 = pd.read_csv('기상청데이터/DB_AWS_PRSR_DD_2019.csv', encoding='cp949').iloc[:,1:]
    press = pd.concat([press2018, press2019], axis=0)
    
    # 예보

    if val_name == '습도':
        return humid
    
    elif val_name == '일조시간':
        return sun
    
    elif val_name == '기압':
        return press
    
    elif val_name == '풍속':
        return wind
    
    elif val_name == '강수':
        return rain
    
    elif val_name == '기온':
        return temp
        