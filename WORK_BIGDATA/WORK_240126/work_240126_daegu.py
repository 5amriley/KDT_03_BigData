"""
2024/01/26 과제
1. 대구광역시 전체 및 8개 구, 군별 (중구, 동구, 서구, 남구, 북구, 수성구, 달서구, 달성군) 남녀 비율을 각각의 파이 차트로 구현하세요.
- subplots 를 이용하여 3x3 형태의 총 9개의 subplot을 파이차트로 구현
- gender.csv 파일 사용
"""

import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# DataFrame으로 저장
filename = '../../EXAM_BIGDATA/DAY_240126/DATA/gender.csv'
genderDF = pd.read_csv(filename, encoding='utf-8-sig', header=[0])

# '대구'에 해당하는 행만 필터링하여 daeguDF에 저장
daegu_mask = genderDF['행정기관'].str.startswith('대구')
daeguDF = genderDF[daegu_mask]

# daeguDF 중 '행정기관', '남 인구수', '여 인구수' 열만 추출
daeguDF2 = daeguDF.iloc[:, [0, 104, 207]].copy()

daeguDF2['남 인구수'] = daeguDF2['남 인구수'].str.replace(',', '')
daeguDF2['여 인구수'] = daeguDF2['여 인구수'].str.replace(',', '')
daeguDF2 = daeguDF2.astype({'남 인구수':'int32', '여 인구수':'int32'})

city_name = []
gender_population = []

for i in range(9):
    city_name.append(daeguDF2.iloc[i, 0].strip())
    gender_population.append([daeguDF2.iloc[i, 1], daeguDF2.iloc[i, 2]])

# print(city_name)
# print(gender_population)

def draw_piecharts1(rows, columns, super_title, titles, values_list):
    ''' plt.subplot() 써서 해결하는 함수 '''
    colors = ['tomato', 'royalblue']
    labels = ['남성', '여성']

    for i in range(rows * columns):
        plt.subplot(rows, columns, i + 1)
        plt.pie(values_list[i], colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title(titles[i])
    plt.suptitle(super_title)
    plt.show()

#draw_piecharts1(3, 3, '대구광역시 구별 남녀 인구 비율', city_name, gender_population)


def draw_piecharts2(rows, columns, super_title, titles, values_list):
    ''' plt.subplots() 써서 해결하는 함수 '''
    colors = ['tomato', 'royalblue']
    labels = ['남성', '여성']

    # fig => <class 'matplotlib.figure.Figure'>
    # ax  => <class 'numpy.ndarray'>
    fig, ax = plt.subplots(rows, columns, figsize=(3*rows, 3*columns))
    idx = 0
    for i in range(rows):
        for j in range(columns):
            ax[i, j].pie(gender_population[idx], colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
            ax[i, j].set_title(city_name[idx])
            idx += 1
    plt.suptitle(super_title)
    plt.show()

draw_piecharts2(3, 3, '대구광역시 구별 남녀 인구 비율', city_name, gender_population)
