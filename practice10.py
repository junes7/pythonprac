# 중첩 루프 사용하기
for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')
# 사각형으로 별 출력하기 (5X5)
for i in range(5):
    for j in range(5):
        print('*', sep='', end='')
    print()
print()
# 사각형 모양 바꾸기 (7X4)
for i in range(4):
    for j in range(7):
        print('*', sep='', end='')
    print()
print()
# 계단식으로 별 출력하기
# 오른쪽 계단
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()
print()
# 왼쪽 계단
for i in range(1, 6):
    for j in range(5-i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
print()
# 역삼각형 왼쪽 계단

# 대각선으로 별 출력하기
for i in range(5):
    for j in range (5):
        if j==i:
            print('*', end='')
        else:
            print(' ', end='')
    print()