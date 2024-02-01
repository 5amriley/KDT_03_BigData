'''
 과제 3. 대구시 각 구별 남녀 비율을 파이 차트로 표현
 대구의 각 구별 남여 성비율 조사
    - 대구광역시 전체, 중구, 동구, 서구, 남구, 북구, 수성구, 달서구, 달성군
'''

import csv
import matplotlib.pyplot as plt
import platform
import numpy as np

def draw_pie_charts(city, gender_dict):
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic', size=8)
    gender_type = ['남성', '여성']

    plt.figure(figsize=(10, 8))
    plt.suptitle(f'{city} 구별 남녀 인구 비율', fontsize=20)

    i = 1
    for key in gender_dict:
        plt.subplot(3, 3, i)
        plt.title(key, size=10)
        values = gender_dict.get(key)
        plt.pie(values, labels=gender_type, autopct='%.1f%%', startangle=90)
        i += 1

    plt.tight_layout()
    plt.show()


def calculate_population_rate():
    f = open('gender.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data)

    gender_dict = dict() # {행정구역: [남자인구수, 여자인구수]}
    city = '대구광역시'
    gu_list = ['', '중구', '동구', '서구', '남구', '북구', '수성구', '달서구', '달성군']

    for gu in gu_list:
        for row in data:
            location = city + ' ' + gu
            if location in row[0]:
                male_count = int(row[104].replace(',', ''))
                female_count = int(row[207].replace(',', ''))
                gender_dict[location] = [male_count, female_count]
                break

    f.close()
    # 구별 인구수 출력
    for key in gender_dict:
        print(f'{key}: {gender_dict.get(key)}')

    draw_pie_charts(city, gender_dict)


calculate_population_rate()