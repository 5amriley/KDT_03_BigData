'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
승하차 인원이 가장 많은 역은?

[주목할 점]
row[4] ~> max[0], row[5] ~> max[1]
row[6] ~> max[2], row[7] ~> max[3]
그래서 max[i-4] = row[i]
'''

import csv

max = [0] * 4   # [0] : 최대 유임승차, [1] : 최대 유임하차, [2] : 최대 무임승차, [3] : 최대 무임하차
max_station = [''] * 4
label = ['유임승차', '유임하차', '무임승차', '무임하차']

# with 구문 : 자동으로 파일을 close() 시킴
with open('../../DATA/subwayfee.csv', encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)

    for row in data:
        for i in range(4, 8):
            row[i] = int(row[i])
            if row[i] > max[i-4]:
                max[i-4] = row[i]
                max_station[i-4] = row[3] + ' ' + row[1]    # '역이름 지하철노선' 추가

for i in range(4):
    print(f'{label[i]}: {max_station[i]} {max[i]:,}명')
