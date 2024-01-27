import pandas as pd

filename = 'DATA/daegu-utf8.csv'
weather_df = pd.read_csv(filename, encoding='utf-8-sig')
print(weather_df.columns)
print(weather_df['날짜'].dtype)   # 날짜 컬럼은 object 타입

# 특수 문자 (℃) 제거
weather_df.columns = ['날짜', '지점', '평균기온', '최저기온', '최고기온']
print(weather_df.columns)

# '날짜' 컬럼의 데이터 타입을 datetime 타입으로 변경
weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
print(weather_df['날짜'].dtype)

# 누락값 개수 구하기
print(weather_df.head(5))
print(weather_df.shape)
num_rows = weather_df.shape[0]  # shape => (row, col), shape[0] : row의 개수
num_missing = num_rows - weather_df.count()     # count() : 정상값의 개수
print(num_missing)

# 누락값(NaN) 처리
weather_df = weather_df.dropna(axis=0)  # axis=0 : NaN이 포함된 행 제거 (진행방향 : 아래쪽)
print(weather_df.count())
print(weather_df.head())

# csv 파일로 저장
savefile = 'DATA/daegu-utf8-df.csv'
weather_df.to_csv(savefile, index=False, mode='w', encoding='utf-8-sig')    # 해당 엑셀 파일을 열어두었다면 PermissionError가 발생한다.

# 특정 년도와 달의 최고, 최저 기온의 평균값 계산
year_df = weather_df[weather_df['날짜'].dt.year == 2023]
month_df = year_df[year_df['날짜'].dt.month == 8]
print(month_df.head())

# 특정 년도와 달의 최저 기온 및 최고 기온의 평균 계산
max_temp_mean = round(month_df['최고기온'].mean(), 1)
min_temp_mean = round(month_df['최저기온'].mean(), 1)

print(f'2023년 8월 최저기온 평균: {min_temp_mean}, 최고기온 평균 : {max_temp_mean}')
