# 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))
for i in range(count):
    print('Hello, world!', i)
# 20부터 10까지 출력하는 방법
for i in range(20, 9, -1):
    print(i, end=' ')
print('\n')
for i in reversed(range(10, 21)):
	print(i, end=' ')
print('\n')
# 연습문제: 리스트의 요소에 10을 곱해서 출력하기
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
	print(i*10, end=' ')
print('\n')
# 심사문제: 구구단 출력하기
dan = int(input())
for i in range(1, 10):
    print(dan, '*', i, '=', dan*i)
# while 반복문으로 Hello, world! 100번 출력하기
# i = 0
# while i < 100:
#     print('Hello, world!', i)
#     i += 1
# 연습문제: 변수 두 개를 다르게 반복하기
i = 2
j = 5
while i <= 32 or j >= 1:
    print(i, j)
    i *= 2
    j -= 1
# 심사문제: 교통카드 잔액 출력하기
price = int(input())
while price >= 1350:
    price -= 1350
    print(price)
# for에서 break으로 반복문 끝내기
for i in range(10000):
    print(i)
    if i == 100:
        break
# 연습문제: 3으로 끝나는 숫자만 출력하기
# 0과 73 사이의 숫자 중 3으로 끝나는 숫자만 출력되게 만드세요.
i = 0
while True:
    # 3으로 끝나지 않는 숫자는 1증가하고 건너뛴다.
    if i % 10 != 3:
        i += 1
        continue
    if i > 74:  
        break
    print(i, end=' ')
    i += 1