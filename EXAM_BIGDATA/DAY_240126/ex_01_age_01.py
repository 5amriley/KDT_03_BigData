'''
데이터 출처 : https://jumin.mois.go.kr/index.jsp#
대구 산격3동 인구 현황
'''

import csv

f = open('DATA/age.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)
print(header)
# row[0] : 행정기관

for row in data:
    if '산격3동' in row[0]:
        print(row)
f.close()
