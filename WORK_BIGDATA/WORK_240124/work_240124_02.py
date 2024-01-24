"""
2. 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고
특정 월의 최고 기온 및 최저 기온의 평균값을 구하고 그래프로 표현

대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고
특정 월의 최고 기온 및 최저 기온의 평균값을 구하고 그래프로 표현
- daegu-utf8-df.csv 파일 이용
- 데이터 구조
   ['날짜', '지점', '평균기온', '최저기온', '최고기온']
     [0]    [1]      [2]       [3]       [4]
- 화면에서 측정할 달을 입력 받아서 진행
- 해당 기간 동안 최고기온 평균값 및 최저기온 평균값 계산
    - 최고기온 및 최저기온 데이터를 이용하여 입력된 달의 각각 평균값을 구함
    - 문자열 형태의 '날짜' 열의 데이터는 datetime으로 변경함
- 하나의 그래프 안에 2개의 꺾은선 그래프로 결과를 출력
    - 마이너스 기호 출력 깨짐 방지
    - 입력된 월을 이용하여 그래프의 타이틀 내용 변경
    - 최고 온도는 빨간색, 최저 온도는 파란색으로 표시하고 각각 마커 및 legend를 표시
"""
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_two_plots(title, x_data, x1, y1, x2, y2):
    plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 출력 깨짐 방지
    plt.figure(figsize=(20,4))
    plt.plot(x1, y1, c='r', marker='s', label='최고기온')
    plt.plot(x2, y2, c='b', marker='s', label='최저기온')
    plt.xticks(x_data)
    plt.legend()
    plt.show()

def main():
    start_year = int(input('시작 연도를 입력하세요 : '))
    end_year = int(input('마지막 연도를 입력하세요 : '))
    the_month = int(input('기온 변화를 측정할 달을 입력하세요 : '))

    filename = '../../DATA/daegu-utf8-df.csv'
    daeguDF = pd.read_csv(filename, encoding='utf-8-sig')

    # '날짜' 컬럼 datetime 객체로 형변환
    daeguDF['날짜'] = daeguDF['날짜'].astype('datetime64[ns]')

    years = list(range(start_year, end_year+1))

    # 연도별 해당 월의 최저기온 평균을 저장할 리스트
    min_temps = []

    # 연도별 해당 월의 최고기온 평균을 저장할 리스트
    max_temps = []

    for y in years:
        # 해당 년도 추출
        year_mask = daeguDF['날짜'].dt.year == y
        a_year_df = daeguDF[year_mask]

        # 해당 월 추출
        month_mask = a_year_df['날짜'].dt.month == the_month
        a_year_month_df = a_year_df[month_mask]

        avg_max_temp = round(a_year_month_df['최고기온'].mean(), 1)
        avg_min_temp = round(a_year_month_df['최저기온'].mean(), 1)
        min_temps.append(avg_min_temp)
        max_temps.append(avg_max_temp)

    print(f'{start_year} 년부터 {end_year} 년까지 {the_month}월의 기온 변화')
    print(f'{the_month}월 최저기온 평균:')
    for t in min_temps:
        print(t, end=", ")
    print('\n')

    print(f'{the_month}월 최고기온 평균:')
    for t in max_temps:
        print(t, end=", ")
    print('\n')

    draw_two_plots(f'{start_year} 년부터 {end_year} 년까지 {the_month}월의 기온 변화', years,
                   years, max_temps, years, min_temps)


main()
