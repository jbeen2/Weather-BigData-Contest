import numpy as np
import pandas as pd
import datetime as datetime

def load_buy():
    # 온라인 구매 이력
    # 날짜, 성별, 연령대, 큰 카테고리, 작은 카테고리, 구매량    
    
    buy2018_1 = pd.read_csv('../data/buy2018_1.csv', encoding='cp949')
    buy2018_2 = pd.read_csv('../data/buy2018_2.csv', encoding='cp949') 
    buy2019_1 = pd.read_csv('../data/buy2019_1.csv', encoding='cp949') 
    buy2019_2 = pd.read_csv('../data/buy2019_2.csv', encoding='cp949')

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

    sns2018_1 = pd.read_csv('../data/sns2018_1.csv', encoding='cp949') 
    sns2018_2 = pd.read_csv('../data/sns2018_2.csv', encoding='cp949') 
    sns2019_1 = pd.read_csv('../data/sns2019_1.csv', encoding='cp949') 
    sns2019_2 = pd.read_csv('../data/sns2019_2.csv', encoding='cp949')

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


def load_weather():
    # 날씨 데이터

    # 습도
    hm_2018 = pd.read_csv('../data/AWS_HR_HM_2018.csv', encoding='cp949')
    hm_2019 = pd.read_csv('../data/AWS_HR_HM_2019.csv', encoding='cp949')
    hm_2018 = hm_2018.iloc[:,1:]; hm_2019 = hm_2019.iloc[:,1:]
    hm_full = pd.concat([hm_2018, hm_2019], axis=0)

    # 일조시간
    icsr_2018 = pd.read_csv('../data/DB_AWS_ICSR_SS_DD_2018.csv', encoding='cp949') 
    icsr_2019 = pd.read_csv('../data/DB_AWS_ICSR_SS_DD_2019.csv', encoding='cp949')
    icsr_2018 = icsr_2018.iloc[:,1:]; icsr_2019 = icsr_2019.iloc[:,1:]
    icsr_full = pd.concat([icsr_2018, icsr_2019], axis=0)

    # 기압 
    prsr_2018 = pd.read_csv('../data/DB_AWS_PRSR_DD_2018.csv', encoding='cp949')
    prsr_2019 = pd.read_csv('../data/DB_AWS_PRSR_DD_2019.csv', encoding='cp949')
    prsr_2018 = prsr_2018.iloc[:,1:]; prsr_2019 = prsr_2019.iloc[:,1:]
    prsr_full = pd.concat([prsr_2018, prsr_2019], axis=0)

    return hm_full, icsr_full, prsr_full