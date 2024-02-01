'''
데이터 출처 : https://jumin.mois.go.kr/index.jsp#
특정 지역의 남녀 인구 비율 예제
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('DATA/gender.csv', encoding='utf-8-sig')   # <class '_io.TextIOWrapper'>
data = csv.reader(f)    # <class '_csv.reader'>
population = []
city = input('찾고 싶은 지역의 이름을 입력하세요: ')
male_count = 0
female_count = 0

for row in data:
    if city in row[0]:
        male_count = int(row[104].replace(',', ''))
        female_count = int(row[207].replace(',', ''))
        break   # 도시별 하위 목록이 많음. 처음에 나오는 데이터가 전체 총합

print(f'{city} 남자 인구수: {male_count:,}명, 여자 인구수: {female_count:,}명')

population = [male_count, female_count]

color = ['cornflowerblue', 'tomato']
plt.pie(population, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90)
plt.title(city + '남녀 성별 비율')
plt.show()
