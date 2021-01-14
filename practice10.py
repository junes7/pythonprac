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
for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print()
# 역삼삭형 오른쪽 계단
for i in range(5):
    for j in range(5):
        if i <= j:
            print('*', end='')
    print()
print()
# 대각선으로 별 출력하기
for i in range(5):
    for j in range (5):
        if j==i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()
# 정사각형 모양으로 별 출력하기
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()
print('-------')
# 심사문제: 산 모양으로 별 출력하기
height = int(input())
blank = height - 1
# 세로 방향
for i in range(height):
# 가로 방향
    for j in range(height+i):
# 공백 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
        if j < blank:
            print(' ', end='')
# 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
        else:
            print('*', end='')
# 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
    print()
# 밑으로 갈 수록 공백이 하나씩 줄어들도록 한다.
    blank-=1
# 연습문제: 역삼각형 모양으로 별 출력하기
# 세로방향
for i in range(5):
# 가로방향
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()