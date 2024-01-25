import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

def draw_lowhigh_graph(start_year, month, day):
    filename = '../../DATA/daegu-utf8.csv'
    f = open(filename, encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)
    high_temp = []  # 최고 기온을 저장할 리스트
    low_temp = []   # 최저 기온을 저장할 리스트
    x_year = []     # x축 연도를 저장할 리스트

    for row in data:
        if row[-1] != '':
            date_string = row[0].split('-')
            if int(date_string[0]) >= start_year:
                if int(date_string[1]) == month and int(date_string[2]) == day:
                    high_temp.append(float(row[-1]))
                    low_temp.append(float(row[-2]))
                    x_year.append(date_string[0])   # 연도 저장
    f.close()

    plt.figure(figsize=(20, 4))
    plt.plot(x_year, high_temp, 'hotpink', marker='o', label='최고기온')
    plt.plot(x_year, low_temp, 'royalblue', marker='s', label='최저기온')

    if platform.system() == 'Windows':
        # 간단히 맑은 고딕으로 설정
        plt.rc('font', family='Malgun Gothic', size=8)
    else:
        # 한글 폰트 사용 For Mac OS
        plt.rc('font', family='AppleGothic', size=8)

    plt.rcParams['axes.unicode_minus'] = False  # 음수(-)가 깨지는 것 방지
    plt.title(f'{start_year}년 이후 {month}월 {day}일의 온도 변화 그래프', size=16)

    plt.legend(loc=2)
    plt.xlabel('year')
    plt.ylabel('temperature')
    plt.show()


draw_lowhigh_graph(2000, 12, 24)
