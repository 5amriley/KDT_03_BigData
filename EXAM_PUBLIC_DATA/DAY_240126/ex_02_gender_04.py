'''
데이터 출처 : https://jumin.mois.go.kr/index.jsp#
서울특별시 및 5대 광역시의 남녀 인구수 비교

[주목할 점]
plt.savefig()   => 지정한 경로에 이미지 저장. (주의: 존재하지 않는 디렉토리를 자동으로 만들지 않으므로 미리 만들어야 한다.)
    - dpi 옵션 : 해상도 지정
plt.close()     => 정확히 어떤 역할인지 모르겠지만, savefig() 쓴 다음 해줘야 한다. 파일 닫기?
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('DATA/gender.csv', encoding='utf-8-sig')   # <class '_io.TextIOWrapper'>
data = csv.reader(f)    # <class '_csv.reader'>
city_list = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시']

for city in city_list:
    male_list = []      # 리스트 데이터 초기화
    female_list = []    # 리스트 데이터 초기화
    for row in data:
        if city in row[0]:
            for i in range(106, 207):
                male_list.append(int(row[i].replace(',', '')))
                female_list.append(int(row[i+103].replace(',', '')))
            break   # 도시별 하위 목록이 많음. 처음에 나오는 데이터가 전체 총합

    color = ['cornflowerblue', 'tomato']
    plt.plot(male_list, label='남성', color=color[0])
    plt.plot(female_list, label='여성', color=color[1])
    plt.title(city + ' 남녀 인구수 비교')
    plt.xlabel('나이')
    plt.ylabel('인구수')
    plt.legend()
    plt.savefig('IMG/' + city + '.png', dpi=200)
    plt.close()

f.close()
