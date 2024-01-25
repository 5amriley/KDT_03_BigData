'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
새벽 4시 지하철 승차 전체 인원

[주목할 점]
엑셀에서 숫자값이 세 자리마다 ,(콤마)가 찍혀있는 형식이면 map(int, row[4:-1]) 실행할 때 ValueError가 발생한다.
ValueError예시 => ValueError: invalid literal for int() with base 10: '7,812'
그러므로, int()를 적용하고 싶은 숫자 셀들의 셀 서식을 '숫자'로 변경해서 저장해 놓아야 한다.

map(int, row[4:-1]) 하는 이유 => row[-1]은 2024-01-03  9:18:00 AM 꼴이라서 int() 적용이 안 됨
'''

import csv

result = []
total_number = 0
with open('../../DATA/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)  # 2줄의 헤더 정보를 건너뜀
    next(data)
    for row in data:
        row[4:-1] = map(int, row[4:-1])     # 문자열을 숫자로 변경
        total_number += row[4]  # [4] 04:00~04:59의 승차 인원을 모두 더함
        result.append(row[4])   # result[]에 새벽 4시 승차인원을 추가

print(f'총 지하철 역의 수: {len(result)}')
print(f'새벽 4시 승차인원: {total_number:,}')
