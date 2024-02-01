'''
lambda를 사용한 dictionary 정렬

[주목할 점]
key 파라미터에 lambda 함수를 넘겨주면,
정렬할 요소 각각을 lambda 함수에 적용하여 나온 값을 사용하여 정렬한다.
- 사람에 빗대면 => 이름: 정렬할 요소 값, 주민등록번호: lambda 함수를 통해 나온 값
             => 그리고, 각 사람들을 이름이 아닌, 주민등록번호로 순서를 세우는 것.

** lambda 함수 (무명함수) : 기존의 함수 정의식에서, 'def 함수명' 과 'return' 을 지운 꼴
'''

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778,
         'Tom':20245, 'Michale':27115,
         'Bob':5887, 'Kelly':7855}

# key를 기준으로 정렬(기본: 오름차순)
print('[lambda] dict 정렬: key 기준 오름차순')
res = sorted(names.items(), key=(lambda x: x[0]))
print(res)
print()

# value를 기준으로 정렬, 내림차순: reverse=True
print('[lambda] dict정렬: value 기준, 내림차순')
res = sorted(names.items(), key=(lambda x: x[1]), reverse=True)
print(res)

# key에 바로 특정 값들을 넘기면 오류 발생 [TypeError: 'dict_values' object is not callable]
# test = sorted(names.items(), key=names.values())
