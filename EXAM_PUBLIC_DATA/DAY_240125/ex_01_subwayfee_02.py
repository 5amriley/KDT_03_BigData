'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
'''

import csv

f = open('DATA/subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)

max_rate=0
rate=0

for	row	in	data:
    for	i in range(4,8):
        row[i] = int(row[i])	#	4,	5,	6,	7	컬럼 값을 정수로 변환
    #rate = row[4] / row[6]	 #	[6]컬럼의 값이 0인 행 확인 용도 (실행하면 오류발생)
    if rate	> max_rate:
        max_rate = rate
print(max_rate)
f.close()
