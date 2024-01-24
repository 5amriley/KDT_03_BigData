import csv

filename = '../DATA/daegu.csv'
# encoding='utf-8-sig'로 '\ufeff' 삭제
fin = open(filename, 'r', encoding='utf-8-sig')     # 읽기용으로 파일 open
data = csv.reader(fin, delimiter=',')

newfilename = '../DATA/daegu-utf8.csv'
fout = open(newfilename, 'w', newline='', encoding='utf-8-sig')     # 쓰기용으로 파일 open
wr = csv.writer(fout)

# row 각각은 문자열 리스트 => 예시: ['2023-12-31', '143', '4.6', '1.4', '7.9']
for row in data:
    for i in range(len(row)):
        # 날짜 정보 앞의 '\t' 제거
        row[i] = row[i].replace('\t', '')
    print(row)
    wr.writerow(row)

fin.close()
fout.close()
print('파일 저장 완료')
