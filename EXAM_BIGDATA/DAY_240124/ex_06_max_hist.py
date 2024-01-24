import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

filename = '../DATA/daegu-utf8.csv'
f = open(filename, encoding='utf-8-sig')
data = csv.reader(f)
next(data)
result = []

for row in data:    # csv reader 객체에 for문
    if row[-1] != '':
        # result에 최고 기온 저장
        result.append(float(row[-1]))
f.close()

plt.figure(figsize=(10, 2))
plt.hist(result, bins=500, color='blue')
plt.rc('font', family='Malgun Gothic')

# plt.rc('axes', unicode_minus=False) 도 동일한 결과
plt.rcParams['axes.unicode_minus'] = False  # 레이블에 마이너스('-') 기호 깨지는 현상 해결
plt.title('1907년부터 2023년까지 대구 기온 히스토그램')
plt.show()
