'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
시간대별 가장 많이 승차하는 역 정보 분석
- 시간대 : 새벽 4시  다음날 새벽 2시
- 총 23개의 데이터
- 새벽 3시는 지하철 운행 안 함

[주목할 점]
plt.tight_layout() => 불필요한 여백 제거
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform

with open('../../DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)  # 2줄의 헤더 정보를 건너뜀
    next(data)
    result = []
    max = [0] * 23  # 새벽 3시는 지하철 운행 안 함
    max_station = ['']*23
    xtick_list = []

    for i in range(4, 27):
        n = i % 24
        xtick_list.append(str(n))

    for row in data:
        row[4:-1] = map(int, row[4:-1])
        for j in range(23):
            a = row[j * 2 + 4]  # j=0: data[0 * 2 + 4]의 값을 max[0]에 저장하기 위함
            if a > max[j]:
                max[j] = a
                max_station[j] = xtick_list[j] + '시:' + row[3]  # 4시: 구로

    for i in range(len(max)):
        print(f'[{max_station[i]}]: {max[i]:,}')

    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic')

    plt.figure(figsize=(10, 10))
    plt.title('시간대별 최대 승차역 정보')
    plt.bar(range(23), max)
    plt.xticks(range(23), labels=max_station, rotation=80)
    plt.tight_layout()  # 불필요한 여백 제거
    plt.show()
