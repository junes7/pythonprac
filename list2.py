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
# 실수가 저장된 리스트가 있을 때 이 리스트의 모든 요소를 정수로 변환
a = [1.2, 2.5, 3.7, 4.6]
print('정수 변환 전:', a)
# for i in range(len(a)):
#     # 실수를 정수로 변환
#     a[i] = int(a[i])
# map을 이용해 실수를 정수로 변환
a = list(map(int, a))
print('정수 변환 후:', a)

# 리스트 안 map 함수를 이용해 숫자를 문자 형태로 변환해 출력하기
b = list(map(str, range(10)))
print(b)

# 튜플에서 특정 값의 인덱스 구하기
a = (38, 21, 53, 62, 19, 53)
print(a.index(53))

# 튜플에서 특정 값의 개수 구하기
b = (10, 20, 30, 15, 20, 40)
print(b.count(20))

# 튜플 표현식 사용하기
# 0~9 숫자 중 2의 배수인 숫자(짝수)로 튜플 생성
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)
print(i for i in range(10) if i % 2 == 0)

# tuple에 map 사용하기
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

# tuple에서 가장 작은 수, 가장 큰 수, 합계 구하기
a = (38, 21, 53, 62, 19)
print(min(a), max(a), sum(a), sep=', ')

# 연습문제: 리스트에서 특정 요소만 뽑아내기
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
# b = [a[i] for i in range(len(a)) if len(a[i]) == 5]
b = [i for i in a if len(i) == 5]
print(b)

# 심사문제: 2의 거듭제곱 리스트 생성하기
a, b = map(int, input().split())
# c = [2**i for i in range(a, b+1) if i != a+1 and i != b-1]
# print(c)
# 다른 방법
c = [2**i for i in range(a, b+1)]
c.pop(1)
c.pop(-2)
print(c)
