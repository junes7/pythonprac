# 2차원 리스트를 만들고 요소에 접근하기
a = [[10, 20], [30, 40], [50, 60]]
print(a)

# 가로 2, 세로 3의 2차원 리스트 만들기
b = [[10, 20],
     [30, 40],
     [50, 60]]
print(b)
print(b[0][0])
print(b[2][1])
b[0][1] = 1000
print(b[0][1])

# 톱니형 리스트
a = []
a.append([])
a[0].append(10)
a[0].append(20)
a.append([])
a[1].append(500)
a[1].append(600)
a[1].append(700)
print(a)

from pprint import pprint
a = [[10, 20], [30, 40], [50, 60]]
pprint(a, indent=1, width=20)

# for 반복문을 한 번만 사용하기
for x, y in a:
    print(x, y)

# for 반복문을 두 번 사용하기
for i in a:
    for j in i:
        print(j, end=' ')
    print()

# while 반복문을 한 번 사용하기
i = 0
while i < len(a):
    x, y = a[i]
    print(x, y)
    i += 1

# while 반복문을 두 번 사용하기
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1

# for 반복문으로 1차원 리스트 만들기
a = []
for i in range(10):
    a.append(0)
print(a)

# for 반복문으로 2차원 리스트(2 X 3) 만들기
a = []
for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)
pprint(a, indent=1, width=20)

# 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
pprint(a, indent=1, width=20)

# for 반복문을 한 번만 사용하고 싶다면
# 식 부분에서 리스트 자체를 곱해주면 됩니다.
a = [[0] * 2 for i in range(3)]
print(a)

# 톱니형 리스트 만들기
# 가로 크기를 저장한 리스트
a = [3, 1, 3, 2, 5]
b= []
for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)
print(b)

# 리스트 표현식을 활용해 톱니형 리스트 만들기
a = [[0] * i for i in a]
print(a)

students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
# 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key = lambda student: student[1]))
# 안쪽 리스트의 인덱스 2을 기준으로 정렬
print(sorted(students, key = lambda student: student[2]))
# c = [[0 for j in range(3)] for i in range(3)]
# c = [[0, 0, 0] for i in range(3)]
c = [0 for i in range(3)]
d = [[[0] for j in range(3)] for i in range(3)]
e = [[0, 0, 0] * 3]
print(c)
print(d)
print(e)

# 2차원 리스트의 할당과 복사 알아보기
a = [[10, 20], [30, 40]]
b = a
b[0][0] = 500
print(a)
print(b)

# 2차원 이상의 다차원 리스트를 완전히 복사하려면
# copy대신 copy모듈의 deepcopy함수를 사용해야 합니다.
import copy
a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)
b[1][0] = 150
print(a)
print(b)

# 연습문제: 3차원 리스트 만들기
# 높이(depth) 2, 세로 크기(row) 4, 가로 크기(col) 3인 3차원 리스트 만들기
# int를 사용하려면 range method를 사용할 것
a = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
print(a)

# 심사문제: 지뢰찾기(Minesweeper)
col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
print('입력 결과 확인:')
# 입력 결과 확인
for i in matrix:
    for j in i:
        print(j, end='')
    print()
print('값 변경 후 출력:')
# 값 변경하여 출력하기
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*':
            print(matrix[i][j], sep='', end='')
        else:
            count = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if x < 0 or y < 0 or x >= row or y >= col:
                        continue 
                    elif matrix[x][y] == '*':
                        count += 1
            print(count, sep='', end='')
    print()
