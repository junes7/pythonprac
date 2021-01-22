a = [i for i in range(10)]
print(a)
b = list(i for i in range(10))
print(b)
# 0부터 9까지 숫자를 생성하면서 값에 5를 더하여 리스트 생성
c = [i+5 for i in range(10)]
print(c)
# 0부터 9까지 숫자를 생성하면서 값에 2를 곱하여 리스트 생성
d = list(i*2 for i in range(10))
print(d)
# 리스트 표현식에서 if조건문 사용하기
# 0~9 숫자 중 2의 배수인 숫자(짝수)로 리스트 생성
a = [i for i in range(10) if i % 2 ==0]
print(a)
# 0~9 숫자 중 홀수에 5를 더하여 리스트 생성
b = [i + 5 for i in range(10) if i % 2 ==1]
print(b)
# 반복문과 if 조건문을 여러 번 사용하기
# 2단부터 9단까지 구구단을 리스트 생성합니다.
a = [i * j for j in range(2, 10)
           for i in range(1, 10)]
print(a)