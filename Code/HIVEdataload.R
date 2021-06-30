# 지역 
# [서울]108, [강릉]105, [대전]133, [청주]131, [광주]156, [대구]143, [전주]146, [부산]159, [제주]184


# 1. 기온
# 시각(일별), 지점번호, 평균기온, 최고기온, 최저기온 
temp2018 <- dbGetQuery(conn, "SELECT TMA, STN_ID, AVG_TA, MAX_TA, MIN_TA FROM db_sfc_ta_dd 
                       WHERE stn_id in (105, 184, 131, 143, 159, 108, 156, 146, 133) 
                       AND db_sfc_ta_dd.tma LIKE '2018%'")
temp2019 <- dbGetQuery(conn, "SELECT TMA, STN_ID, AVG_TA, MAX_TA, MIN_TA FROM db_sfc_ta_dd 
                       WHERE stn_id in (105, 184, 131, 143, 159, 108, 156, 146, 133)  
                       AND db_sfc_ta_dd.tma LIKE '2019%'")

# 2. 강수량 
# 시각(시간별), AWS번호, RN_DAY (누적 강수량, 마지막 23시 데이터), RN_HR1 (1시간 강수량, 일별 최대값)
rain2018 <- dbGetQuery(conn, "SELECT TM, AWS_ID, RN_DAY, RN_HR1 FROM aws_hr_rn 
                       WHERE AWS_ID in (105, 184, 131, 143, 159, 108, 156, 146, 133)
                       AND aws_hr_rn.tm LIKE '2018%'")

rain2019 <- dbGetQuery(conn, "SELECT TM, AWS_ID, RN_DAY, RN_HR1 FROM aws_hr_rn 
                       WHERE AWS_ID in (105, 184, 131, 143, 159, 108, 156, 146, 133)
                       AND aws_hr_rn.tm LIKE '2019%'")

# 3. 풍속 
# 시각(시간별), 지점번호, 평균풍속 
wind2018 <- dbGetQuery(conn, "SELECT TMA, STN_ID, AVG_WS FROM DB_SFC_WIND_DD 
                       WHERE STN_ID in (105, 184, 131, 143, 159, 108, 156, 146, 133)
                       AND DB_SFC_WIND_DD.TMA LIKE '2018%'")

wind2019 <- dbGetQuery(conn, "SELECT TMA, STN_ID, AVG_WS FROM DB_SFC_WIND_DD 
                       WHERE STN_ID in (105, 184, 131, 143, 159, 108, 156, 146, 133)
                       AND DB_SFC_WIND_DD.TMA LIKE '2019%'")

# 4. 습도 
# 시각(시간별), 지점번호, 정시습도, 과거 60분간 최고 습도 
AWS_HR_HM_2018 <- dbGetQuery(conn, "select TM, AWS_ID, HM, HM_MAX from AWS_HR_HM 
                            WHERE AWS_ID in (105, 184, 131, 143, 159, 108, 156, 146, 133) 
                            AND TM LIKE '2018%'")
AWS_HR_HM_2019 <- dbGetQuery(conn, "select TM, AWS_ID, HM, HM_MAX from AWS_HR_HM 
                            WHERE AWS_ID in (105, 184, 131, 143, 159, 108, 156, 146, 133)  
                            AND TM LIKE '2019%'")

# 5. 일조시간 
# 시각(일별), 지점번호, 합계 일조 시간 
DB_AWS_ICSR_SS_DD_2018 <- dbGetQuery(conn, "select TMA, STN_ID, SUM_SS_HR from DB_AWS_ICSR_SS_DD 
                                    WHERE STN_ID in (105, 184, 131, 143, 159, 108, 156, 146, 133) 
                                    AND TMA LIKE '2018%'")
DB_AWS_ICSR_SS_DD_2019 <- dbGetQuery(conn, "select TMA, STN_ID, SUM_SS_HR from DB_AWS_ICSR_SS_DD 
                                    WHERE STN_ID in (105, 184, 131, 143, 159, 108, 156, 146, 133) 
                                    AND TMA LIKE '2019%'")

# 6. 기압 
# 시각(시간별), 지점번호, 평균 현지기압, 최고 현지기압 
DB_AWS_PRSR_DD_2018 <- dbGetQuery(conn, "select TMA, STN_ID, AVG_PA, MAX_PA from DB_AWS_PRSR_DD 
                                  WHERE STN_ID in (105, 184, 131, 143, 159, 108, 156, 146, 133) 
                                  AND TMA LIKE '2018%'")
DB_AWS_PRSR_DD_2019 <- dbGetQuery(conn, "select TMA, STN_ID, AVG_PA, MAX_PA from DB_AWS_PRSR_DD 
                                  WHERE STN_ID in (105, 184, 131, 143, 159, 108, 156, 146, 133) 
                                  AND TMA LIKE '2019%'")