import csv

filename = '../../DATA/daegu-utf8.csv'
f = open(filename, 'r', encoding='utf-8-sig')     # 쓰기용으로 파일 open
data = csv.reader(f, delimiter=',')

# next 함수 : 첫 번째 데이터 행을 읽어오면서 데이터의 탐색 위치를 다음으로 이동시킨다.
header = next(data)
print(header)

i = 1
for row in data:
    print(row)
    if i >= 5:
        break
    i += 1
f.close()
