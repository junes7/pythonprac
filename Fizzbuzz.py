# 1부터 100까지 숫자 출력하기
for i in range(1, 101):
    print(i, end=' ')
print()
# 1부터 100까지 숫자 중 3의 배수일 때와 5의 배수일 때
# 숫자 대신 'Fizz', 'Buzz' 출력하도록 처리하기
for i in range(1, 101):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
print()
# 1부터 100까지 숫자 중 3과 5의 공배수 처리하기
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
print()
# 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
print()
# 코드를 매우 단축하여 FizzBuzz 문제 풀기
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    # 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리

