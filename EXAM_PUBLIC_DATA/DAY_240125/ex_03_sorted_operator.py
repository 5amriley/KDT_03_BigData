'''
operator 패키지를 사용한 dictionary 정렬

[주목할 점]
key 파라미터에 operator.itemgetter()를 넘겨서 정렬할 수도 있다.
'''
import operator

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778,
         'Tom':20245, 'Michale':27115,
         'Bob':5887, 'Kelly':7855}

# key를 기준으로 정렬(기본: 오름차순)
print('[operator] dict 정렬: key 기준 오름차순')
sorted_x = sorted(names.items(), key=operator.itemgetter(0))
print(sorted_x)
print()

# value를 기준으로 정렬, 내림차순: reverse=True
print('[operator] dict정렬: value 기준, 내림차순')
sorted_x = sorted(names.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_x)
