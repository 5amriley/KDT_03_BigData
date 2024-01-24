import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_graph_on_date(month, day):
    filename = '../DATA/daegu-utf8.csv'
    f = open(filename, encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)
    result=[]

    for row in data:
        if row[-1] != '':
            date_string = row[0].split('-')
            if date_string[1] == month and date_string[2] == day:
                result.append(float(row[-1]))   # 최고 기온을 실수형으로 변환 후 리스트에 추가
    f.close()

    plt.figure(figsize=(15, 2))
    plt.plot(result, 'royalblue')
    plt.rc('axes', unicode_minus = False)
    plt.rc('font', family='Malgun Gothic')
    plt.title(f'매년 {month}월 {day}일 최고 기온 변화')
    plt.show()

month, date = input('날짜(월, 일)을 입력하세요(예시: 01 01) : ').split()
draw_graph_on_date(month, date)
