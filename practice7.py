print(list(range(0, 10)) + list(range(10, 20)))
print(tuple(range(0, 10)) + tuple(range(10, 20)))
print(list(range(0, 5, 2)) * 3)
print(tuple(range(0, 5, 2)) * 3)

# 요소에 값 할당하기
a = [0, 0, 0, 0, 0]
a[0] = 38
a[1] = 21
a[2] = 53
a[3] = 62
a[len(a)-1] = 19
print(a)
print(a[0], a[-2], a[4], sep=', ')
# 연습문제: 최근 3년간 인구 출력하기
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
print(year[5:])
print(year[-3:])
print(population[-3:])
print(population[5:])
# 연습문제: 인덱스가 홀수인 요소 출력하기
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(len(n))
print(n[1::2])
print(n[1:len(n):2])
print(n[1:12:2])
# 심사문제: 리스트의 마지막 부분 삭제하기
# x = input().split()
# del x[-5:]
# print(tuple(x))
# 심사문제: 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결하기
x = input()
y = input()
print(x[1::2])
print(y[0::2])
print(x[1::2] + y[0::2])