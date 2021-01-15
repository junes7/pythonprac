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
