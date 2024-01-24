import csv

def get_minmax_temp(data):
    '''
    최고 / 최저 기온, 최고 / 최저 기온의 날짜 구하기
    :param data: csv reader 객체
    :return:
    '''
    header = next(data)

    min_temp = 100  # 최저 기온값을 저장할 변수 초기화 (input 값들보다 큰 값)
    min_date = ''   # 최저 기온의 날짜를 저장할 변수 초기화

    max_temp = -999 # 최고 기온값을 저장할 변수 초기화 (input 값들보다 작은 값)
    max_date = ''

    for row in data:
        if row[3] == '':
            row[3] = 100
        row[3] = float(row[3])

        if row[4] == '':
            row[4] = -999
        row[4] = float(row[4])

        # 최저 기온 계산
        if row[3] < min_temp:
            min_temp = row[3]
            min_date = row[0]   # 날짜 : index[0]

        # 최고 기온 계산
        if row[4] > max_temp:
            max_temp = row[4]
            max_date = row[0]

    print('-' * 50)
    print(f'대구 최저 기온 날짜 : {min_date}, 온도 : {min_temp}')
    print(f'대구 최고 기온 날짜 : {max_date}, 온도 : {max_temp}')

def main():
    filename = '../DATA/daegu-utf8.csv'
    f = open(filename, encoding='utf-8-sig')
    data = csv.reader(f)    # csv reader 객체 생성
    get_minmax_temp(data)
    f.close()

main()  # main 함수 호출
