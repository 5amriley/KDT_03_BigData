'''
데이터 출처 : https://jumin.mois.go.kr/index.jsp#
투표 가능 인구수 분석 (파이 차트)
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_piechart(city_name, city_population, voting_poulation):
    '''
    전체 인구수 대비 투표 가능 인구의 파이차트 그리기
    :param city_name:
    :param city_population:
    :param voting_poulation:
    :return:
    '''
    non_voting_population = city_population - voting_poulation
    population = [non_voting_population, voting_poulation]

    color = ['tomato', 'royalblue']
    plt.pie(population, labels=['18세 미만', '투표가능인구'],
            autopct='%.1f%%', colors=color, startangle=90)
    plt.legend(loc=1)
    plt.title(city_name + '투표 가능 인구 비율')
    plt.show()


def get_voting_population(city):
    '''
    튜포 가능 인구수 분석 row[21:]
    전체 인구수 : row[1]
    :param city:
    :return: None
    '''
    f = open('DATA/age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data) # 헤더 정보 건너 뜀

    voting_number_list = []
    city_name = ''
    city_population = 0     # 도시 전체 인구수
    voting_population = 0

    for row in data:
        if city in row[0]:  # 검색이 부정확 (예시: '대구' 입력했을 때 '해운대구'가 검색될 수 있음)
            city_population = row[1]
            if ',' in city_population:
                # 도시 전체 인구수에서 천단위 콤마 제거
                city_population = city_population.replace(',', '')
            city_population = int(city_population)
            city_name = row[0]
            for data in row[21:]:   # 18세 이상
                if ',' in data:
                    data = data.replace(',', '')    # 천단위 콤마 제거
                voting_num = int(data)
                # 각 연령대별 투표 인구수를 리스트에 추가
                voting_number_list.append(voting_num)
                # 누적된 투표 가능 인구수
                voting_population += voting_num
            break
    f.close()

    print(f'{city_name}전체 인구수:{city_population:,}명,'
          f'투표 가능 인구수: {voting_population:,}명')

    draw_piechart(city_name, city_population, voting_population)


city = input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요 : ')
get_voting_population(city)
