'''
데이터 출처 : https://jumin.mois.go.kr/index.jsp#
학령 인구 비율
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_piechart(city, population_list, label_list):
    plt.pie(population_list, labels=label_list, autopct='%.1f%%', startangle=90)

    plt.legend(loc=1)
    plt.title(city + ' 학령인구 비율')
    plt.show()


def get_population(row, start, end):
    population = 0

    for num in row[start:end+1]:
        if ',' in num:
            num = num.replace(',', '')
        num = int(num)
        population += num
    return population


def school_age_population(city):
    f = open('DATA/age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data) # 헤더 정보 건너 뜀

    city_population = 0
    non_school_pop = 0
    school_age_pop = 0

    label_list = ['초등학생', '중학생', '고등학생', '대학생', '비학령인구']
    population_list = []

    city_name =''

    for row in data:
        if city in row[0]:  # 검색이 부정확 (예시: '대구' 입력했을 때 '해운대구'가 검색될 수 있음)
            city_population = row[1]
            if ',' in city_population:
                # 도시 전체 인구수에서 천단위 콤마 제거
                city_population = city_population.replace(',', '')
            city_population = int(city_population)

            city_name = row[0]

            # 각 구간별 인구 계산
            elementary_pop = get_population(row, 9, 14)
            population_list.append(elementary_pop)

            middleschool_pop = get_population(row, 15, 17)
            population_list.append(middleschool_pop)

            highschool_pop = get_population(row, 18, 20)
            population_list.append(highschool_pop)

            university_pop = get_population(row, 21, 24)
            population_list.append(university_pop)

            school_age_pop = (elementary_pop + middleschool_pop +
                              highschool_pop + university_pop)

            non_school_pop = city_population - school_age_pop
            population_list.append(non_school_pop)
            break

    f.close()

    school_age_pop_rate = round((school_age_pop*100)/city_population, 1)
    print(f'전체 인구수:{city_population:,}명,'
          f'학령 인구수:{school_age_pop:,}명,'
          f'학령인구 비율: {school_age_pop_rate}%')

    draw_piechart(city_name, population_list, label_list)


city = input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요 : ')
school_age_population(city)
