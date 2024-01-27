'''
데이터 출처 : https://jumin.mois.go.kr/index.jsp#
인구 구조 그래프 함수 구현
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def print_population(population):
    '''
    특정 지역의 인구 현황을 화면에 출력함
    :param population:
    :return: None
    '''

    for i in range(len(population)):
        print(f'{i:3d}세 {population[i]:6d}명', end=' ')
        if (i+1) & 10 == 0:
            print()

def draw_population(district_name, population_list):
    '''
    특정 지역에 대한 인구 분포를 그래프로 나타냄 (plot)
    :param district_name: 지역 이름
    :param population_list: 0~100세 이상까지 인구수 리스트
    :return: None
    '''
    # 그래프 출력
    plt.style.use('ggplot')
    plt.title('{} 인구 현황'.format(district_name))
    plt.xlabel('나이')
    plt.ylabel('인구수')

    plt.bar(range(101), population_list)
    plt.xticks(range(0, 101, 10))   # 0세 ~ 100세 이상

    plt.plot(population_list)
    plt.show()

def get_population(city):
    f = open('DATA/age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data) # 헤더 정보 건너 뜀

    population_list = []
    district_name = ''

    for row in data:
        if city in row[0]:  # 검색이 부정확 (예시: '대구' 입력했을 때 '해운대구'가 검색될 수 있음)
            district_name = row[0]
            for data in row[3:]:  # 0세부터 100세 이상까지의 데이터
                if ',' in data:
                    data = data.replace(',', '')
                population_list.append(int(data))  # 숫자로 변환
            break   # 처음으로 일치하는 도시명만 검색하기 위함
    f.close()

    print_population(population_list)
    draw_population(district_name, population_list)

city = input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요 : ')
get_population(city)
