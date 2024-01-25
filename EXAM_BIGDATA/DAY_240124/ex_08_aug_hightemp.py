import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

filename = '../../DATA/daegu-utf8.csv'
f = open(filename, encoding='utf-8-sig')
data = csv.reader(f)
next(data)
aug = []

for row in data:
    if row[-1] != '':   # 최고기온 정보가 있다면
        month = row[0].split('-')[1]
        if month == '08':
            # 8월달의 최고기온 정보만 리스트에 추가
            aug.append(float(row[-1]))  # matplotlib에서 그래프로 표시하기 위해 float로 변환
f.close()

plt.hist(aug, bins=100, color='tomato')
plt.title('대구 8월의 최고 기온 히스토그램')
plt.xlabel('Temperature')
plt.ylabel('Counts')
plt.show()
