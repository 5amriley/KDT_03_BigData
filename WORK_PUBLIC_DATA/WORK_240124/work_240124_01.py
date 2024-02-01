"""
1. 과거 10년 동안의 대구 날씨 데이터에서 1년 중 일교차가 가장 큰 달은 각각 몇 월인지 그래프로 표시
- 기간 : 최근 10년 (2014년 ~ 2023년)
- 각 달의 일교차(최고기온 - 최저기온)를 비교하여 각 년도별 일교차가 가장 큰 달을 bar 그래프로 표시
- Pandas 또는 Python 코딩
"""

import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def main():
    filename = '../../DATA/daegu-utf8-df.csv'
    daeguDF = pd.read_csv(filename, encoding='utf-8-sig')

    # '날짜' 컬럼 datetime 객체로 형변환
    daeguDF['날짜'] = daeguDF['날짜'].astype('datetime64[ns]')

    # '일교차' 컬럼 생성
    daeguDF['일교차'] = daeguDF['최고기온'] - daeguDF['최저기온']
    years = list(range(2014, 2024))

    # 연도별 가장 일교차가 큰 달과 그 일교차 값을 저장할 딕셔너리
    biggest_temp_range = dict() # 입력값 형식 => 년도: [달, 일교차 값]

    #print(daeguDF.iloc[38496])
    for y in years:
        year_mask = daeguDF['날짜'].dt.year == y
        a_year_df = daeguDF[year_mask]
        #print(a_year_df)

        max_temp_range = 0  # 한 달중 가장 큰 일교차 평균치 값
        max_month = None
        for m in range(1, 13):
            month_mask = a_year_df['날짜'].dt.month == m
            a_year_month_df = a_year_df[month_mask]
            # 평균(avg_temp_range)을 어떻게 집계하는가에 따라 2022년의 결과가 달라진다.
            # 평균을 반올림취하지 않고 구하면 2022년의 결과는 : 5월
            # 평균을 소수 첫째자리까지 반올림하면 2022년의 결과는 : 4월
            #avg_temp_range = a_year_month_df['일교차'].mean()
            avg_temp_range = round(a_year_month_df['일교차'].sum() / len(a_year_month_df['일교차']), 1)
            if avg_temp_range > max_temp_range:
                max_temp_range = avg_temp_range
                max_month = m
        biggest_temp_range[y] = (max_month, max_temp_range)

    for k, v in biggest_temp_range.items():
        print(k, v)

    plt.figure(figsize=(10, 5))
    plt.title('지난 10년간 대구의 일교차가 가장 큰 달')
    X = [f'{k}.{v[0]}' for k, v in biggest_temp_range.items()]
    Y = [v[1] for _, v in biggest_temp_range.items()]
    plt.bar(X, Y)
    plt.xlabel('Year/Month')
    plt.ylabel('일교차')
    plt.show()


main()