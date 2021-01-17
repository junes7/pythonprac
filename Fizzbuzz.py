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
print('-------------------')
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
# 1부터 100까지 숫자 중 5와 10의 공배수 처리하기
for i in range(1, 101):
    if i % 5 == 0 and i % 10 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 10 == 0:
        print('Buzz')
    else:
        print(i)
print('-------------------')

# 연습문제: 2와 11의 배수, 공배수 처리하기
# 1부터 100까지 숫자를 출력하면서 2의 배수일 때는 'Fizz',
# 11의 배수일 때는 'Buzz', 2과 11의 공배수일 때는 'FizzBuzz'가
# 출력되게 만드세요.
for i in range(1, 101):
    if i % 2 == 0 and i % 11 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)
print()
# 코드를 매우 단축하여 FizzBuzz문제 풀기
# 1부터 100까지 숫자 중 3과 5의 공배수 처리하기
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    # 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리
# 심사문제: 5와 7의 배수 공배수 처리하기
a, b = map(int, input().split())
for i in range(a, b+1):
    print('Fizz' * (i % 5 == 0) + 'Buzz' * (i % 7 == 0) or i)
