'''
[ 홀수차 마방진 ]
- 마방진 원리
    - 시작 위치 : 첫 행의 가운데 열에서 시작함(x1=0, y1=1)
    - 다음 위치는 오른쪽 대각선 방향으로 이동 (x2=x1-1, y2=y1+1)
    - x축 방향으로 범위가 벗어난 경우, x는 마지막 행(size-1)으로 이동
    - y축 방향으로 범위가 벗어난 경우, y는 첫 번째 열(0)으로 이동
    - 다음 이동 위치에 이미 값이 있는 경우, x는 x+1
    - x축 방향으로도, y축 방향으로도 범위가 벗어난 경우, 이동하기 전 위치에서 아래로 이동 (x2=x1+1)
'''


def get_odd_number() -> int:
    """ 홀수를 입력 받아 반환 """
    while True:
        n = input('홀수차 배열의 크기를 입력하세요: ')
        if n.isdecimal():
            if int(n) % 2 == 1:
                return n
            else:   # 짝수일 때
                print('짝수를 입력하였습니다. 다시 입력하세요.')
                continue
        else: print('잘못된 입력입니다. 홀수를 입력하세요.')


def print_2darray(square: list):
    """ 2차원 리스트 출력 """
    for i in range(len(square)):
        for j in range(len(square[i])):
            print(f'{square[i][j]:<3d}', end='')
        print()
    print()


def magic_square(n: int):
    """ n x n 크기의 마방진 생성, 출력 """
    square = [[0 for col in range(n)] for row in range(n)]
    i = 1
    x, y = 0, n // 2

    while i <= n ** 2:
        if x < 0 and y > n - 1:
            # x축, y축 모두 벗어난 경우
            x, y = x+2, y-1
        elif x < 0:
            # x축만 벗어난 경우
            x = n-1
        elif y > n-1:
            # y축만 벗어난 경우
            y = 0
        elif square[x][y] > 0:
            # 이동 위치에 이미 값이 있는 경우
            x, y = x+2, y-1
        else:
            # 아무 이상 없는 경우
            square[x][y] = i
            i += 1
            x, y = x-1, y+1

    print(f'Magic Square ({n}x{n})')
    print_2darray(square)


def magic_square2(n: int):
    """ n x n 크기의 마방진 생성, 출력 (나머지 연산자 % 사용 ver.) """
    square = [[0 for col in range(n)] for row in range(n)]
    x, y = 0, n // 2

    for i in range(1, n**2+1):
        square[x][y] = i
        if square[(x-1)%n][(y+1)%n] > 0:
            # 이동 위치에 이미 값이 있는 경우
            x = x + 1
        else:
            # x축, y축을 벗어날 때 이동하는 것도 처리가능
            x = (x-1) % n
            y = (y+1) % n

    print(f'Magic Square ({n}x{n})')
    print_2darray(square)


def main():
    n = get_odd_number()    # 변경가능 (키보드 입력)
    magic_square2(int(n))    # n x n 마방진 생성, 출력


main()
