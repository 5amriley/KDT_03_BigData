'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
유임승차 비율이 50% 이하인 역

[주목할 점]
파이차트는 koreanize_matplotlib 모듈 안 써도 한글 출력이 잘 된다.
'''

import csv
import matplotlib.pyplot as plt
import platform

f = open('../../DATA/subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
print(header)

min_rate = 100
mix_row = []
min_total_count = 0

for row in data:
    for i in [4, 6]:    # 왜 range(4, 6) 을 하면 에러가 나지?? i가 5일 때 무슨 일이??
        row[i] = int(row[i])
    total_count = row[4] + row[6]   # 유임승차수 + 무임승차수
    # 무임승차 인원이 없고, 총 승차인원이 1만명 이상
    if (row[6] != 0) and (total_count > 10000):
        rate = row[4] / total_count # 유임승차 비율
        if rate < 0.5:
            print(row, round(rate, 2))
            if rate < min_rate:
                min_rate = rate
                min_row = row
                min_total_num = total_count
f.close()

print()
print(f'유임승차 비율이 가장 낮은 역 : {min_row[3]}')
print(f'전체 인원 : {min_total_count:,}명, '
      f'유임승차인원 : {min_row[4]:,}명,'
      f'유임승차비율:{round(min_rate * 100, 1)}%')

if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')

plt.title(min_row[3] + '역 유, 무임 승차 비율')
label = ['유임승차', '무임승차']
values = [min_row[4], min_row[6]]   # 파이차트에 전달할 데이터 리스트
plt.pie(values, labels=label, autopct='%.1f%%')
plt.legend(loc=2)
plt.show()
