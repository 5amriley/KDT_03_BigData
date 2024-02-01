'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
출근 시간대 지하철 이용 현황

[주목할 점]
총 2개 그래프를 하나의 창에 그림 (y축 공유)
- 출근 시간대(7~9시까지) 모든 역의 승차 인원 그래프
- 출근 시간대(7~9시까지) 승차 인원 상위 10개 역의 승차 인원의 막대 그래프
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
        row_sum = sum(row[10:15:2])         # 오전 7시, 8시, 9시 승차인원 합
        result.append(row_sum)
        if row_sum > max_num:
            max_num = row_sum
            max_station = row[3] + '(' + row[1] + ')'

print(f'최대 승차 인원역: {max_station} {max_num:,}')
result.sort(reverse=True)   # 내림차순으로 정렬

plt.figure(figsize=(10, 4))
ax1 = plt.subplot(1, 2 ,1)  # (행의 수, 열의 수, 인덱스)
plt.title('10개 역의 승차 인원수', size=12)
plt.bar(range(10), result[0:10])
plt.ylabel('승차인원수')

ax2 = plt.subplot(1, 2, 2, sharey=ax1)  # sharey: y축 label 공유4
plt.title('전체 역의 승차 인원수', size=12)
plt.bar(range(len(result)), result)

# suptitle() : subplot들의 전체 부모 타이틀
plt.suptitle('출근시간대 승차 인원 현황\n', size=20)
plt.tight_layout()
plt.show()
