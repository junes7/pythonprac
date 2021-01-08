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
