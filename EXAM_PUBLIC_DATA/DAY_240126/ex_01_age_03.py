'''
데이터 출처 : https://jumin.mois.go.kr/index.jsp#
산격3동 인구 분포 그래프 그리기
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('DATA/age.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)

result = []
#city = ''
city = input("지역 이름 입력(시군구동): ")

for row in data:
    if city in row[0]:  # 검색이 부정확 (예시: '대구' 입력했을 때 '해운대구'가 검색될 수 있음)
        city = row[0]
        for data in row[3:]:    # 0세부터 100세 이상까지의 데이터
            if ',' in data:
                data = data.replace(',', '')
            result.append(int(data))    # 숫자로 변환
f.close()
print(result)

plt.title(f'{city} 인구현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()
