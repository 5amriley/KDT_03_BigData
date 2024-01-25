'''
데이터 출처 : https://pay.tmoney.co.kr/ncs/pct/ugd/ReadTrcrStstList.dev
출퇴근 시간대 이용 현황
- pandas에서 엑셀 파일 읽기
'''

import pandas as pd

filename = '../../DATA/subway.xls'
df = pd.read_excel(filename, sheet_name='지하철 시간대별 이용현황', header=[0, 1])
print(df.head())

# 나머지는 주피터 노트북으로 함
# => base 환경에서 xlrd가 설치 안되는 오류 때문에
# => 주피터 노트북에서 My_38 환경으로 실행했음.
# ==> 결국 base 에 xlrd 설치 끝냈음. (Anaconda Powershell prompt 관리자 권한으로 실행해서 설치 성공!)
