'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
전체 지하철역 승하차 인원 분석 및 저장

[주목할 점]
dpi = dots per inch
plt.figure() 에서 dpi 옵션을 넣을 수 있음
plt.savefig()   => plt 그림 저장 메서드
plt.close()     => savefig() 이후, 파일 닫기
'''

import csv
import matplotlib.pyplot as plt
import platform

max = [0] * 4   # [0] : 최대 유임승차, [1] : 최대 유임하차, [2] : 최대 무임승차, [3] : 최대 무임하차
max_station = [''] * 4
label = ['유임승차', '유임하차', '무임승차', '무임하차']
color_list = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']   # 파이 차트 컬러 값
pic_count = 0

# with 구문 : 자동으로 파일을 close() 시킴
with open('../../DATA/subwayfee.csv', encoding='utf-8-sig') as f:
    data=csv.reader(f)
    next(data)

    if(platform.system() == 'Windows'):
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic')

    for row in data:
        for i in range(4, 8):
            row[i] = int(row[i])
        print(row)
        plt.figure(dpi=100) # 저장할 그림파일의 dpi 설정
        plt.title(row[3] + ' ' + row[1])
        plt.pie(row[4:8], labels=label, colors=color_list, autopct='%.1f%%', shadow=True)
        plt.savefig('img/' + row[3] + ' ' + row[1] + '.png') # 그림 저장
        plt.close() # savefig()과 관련, 파일 닫기

        # 10개 역의 파이차트만 저장함
        pic_count += 1
        if pic_count >= 10:
            break
