'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
새벽 4시 지하철 이용 인원 수 (그래프)
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)  # 2줄의 헤더 정보를 건너뜀
    next(data)
    result = []
    total_number = 0
    max_num = -1
    max_station = ''

    for row in data:
        row[4:-1] = map(int, row[4:-1])     # 문자열을 숫자로 변경
        total_number += row[4]  # [4] 04:00~04:59의 승차 인원을 모두 더함
        result.append(row[4])
        if row[4] > max_num:
            max_num = row[4]
            max_station = row[3]

print('새벽 4시 승차 인원수: {0:,}'.format(total_number))
print('최대 승차역: {0}, 인원수:{1:,}'.format(max_station, max_num))
result.sort()   # 오름차순으로 정렬
plt.figure(dpi=100)
plt.bar(range(len(result)), result)
plt.title('새벽 4시 지하철 승차인원 현황')
plt.show()
