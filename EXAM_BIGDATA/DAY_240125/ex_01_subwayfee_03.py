'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
'''

import csv

f = open('../../DATA/subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)
rate=0

for	row	in data:
    for	i in range(4,8):
        row[i] = int(row[i])	# 4, 5, 6, 7 컬럼 값을 정수로 변환
    rate = row[4] / (row[4] + row[6])
    if row[6] == 0:
        print(row)
f.close()
