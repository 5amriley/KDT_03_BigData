'''
    파이썬 홀수차 마방진 소스 코드

'''


#--------------------------------------------------------------------------
# 마방진 계산 함수
#--------------------------------------------------------------------------
def magicsquare(size):
    i = 0
    j = size//2;

    next_i = 0
    next_j = 0
    num = 1
    print("Magic Square ({0}x{1})".format(size, size))
    matrix = [[0]*size for i in range(size)]

    for x in range(size*size):
        matrix[i][j] = num      # (0, 2)에 1을 대입
        # 대각선 위쪽 방향으로 이동함
        next_i = i - 1
        next_j = j + 1

        # y축 방향으로 배열의 범위가 벗어난 경우, 마지막 행으로 이동 (size-1, y+1)
        if next_i < 0:
            next_i = size-1

        # x축 방향으로 배열의 범위가 벗어난 경우, 첫번째 열로 이동 (x-1, 0)
        if next_j >= size:
            next_j = 0

        # 이동하려는 위치에 이미 값이 있는 경우
        if matrix[next_i][next_j] != 0:
            i += 1
        else:
            i = next_i;
            j = next_j;

        num += 1
        #print(matrix)

    print_matrix(matrix, size)


#--------------------------------------------------------------------------
#  배열 출력 함수
#--------------------------------------------------------------------------
def print_matrix(matrix, size):
    for i in range(size):
        for j in range(size):
            print("{0:2d}".format(matrix[i][j]), end=" ")
        print()


def main():

    size = int(input("홀수차 배열의 크기를 입력하세요: "))
    if size % 2 == 1 and size > 0:
        magicsquare(size)
    else:
        print("짝수를 입력하였습니다. 다시 입력하세요.")




main()