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