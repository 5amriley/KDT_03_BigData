'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
최대 유임승차 비율 확인 (승하차인원이 10만명 넘는 역들 중)

[주목할 점]
숫자 출력시 세 자리마다 ,(콤마)가 출력되도록 문자열 포메팅하는 법
print() 함수 안에 문자열 여러 개를 넣을 때 콤마 없어도 작동한다.
'''

import csv

f = open('../../DATA/subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)

max_rate = 0
max_row = []
max_total_num = 0

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    total_count = row[4] + row[6]   # 유임승차수 + 무임승차수
    if (row[6] != 0) and (total_count > 100000):
        rate = row[4] / total_count # 유임승차 비율
        if rate > max_rate:
            max_rate = rate
            max_row = row
            max_total_num = total_count
print()
print(f'호선명 {max_row[1]}, 역이름:{max_row[3]}, 전체 인원: {max_total_num:,}명,'
    f'유임승차인원 {max_row[4]:,}, 유임승차 비율:{round(max_rate * 100, 2):,}%')
print('중간에' '콤마 안찍는데도' '이게' '되네')
