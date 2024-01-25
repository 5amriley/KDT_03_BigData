import csv
import matplotlib.pyplot as plt

filename = '../../DATA/daegu-utf8.csv'
f = open(filename, encoding='utf-8-sig')    # 'utf-8-sig' 생략가능
data = csv.reader(f)

header = next(data)
result = []

for row in data:
    if row[4] != '':    # 최고 기온 데이터 값이 있으면, 데이터에 저장
        result.append(float(row[4]))

print(len(result))
f.close()

plt.figure(figsize=(10, 2))
plt.plot(result, 'r')
plt.show()