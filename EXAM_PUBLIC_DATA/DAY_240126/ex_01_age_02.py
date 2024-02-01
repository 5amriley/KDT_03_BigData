'''
데이터 출처 : https://jumin.mois.go.kr/index.jsp#
산격3동 인구 데이터 출력
'''

import csv

f = open('DATA/age.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)

result = []

for row in data:
    if '산격3동' in row[0]:
        for data in row[3:]:
            result.append(data)
print(result)
f.close()
