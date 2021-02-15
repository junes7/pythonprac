# 람다 표현식으로 함수 만들기
def plus_ten(x):
    return x + 10
print(plus_ten(1))

print(lambda x: x + 10)

plus_ten = lambda x: x + 10
print(plus_ten(1))

# 람다 표현식 자체를 호출하기
print((lambda x: x + 10)(1))
# 람다 표현식을 인수로 사용하기
def plus_ten(x):
    return x + 10
print(list(map(plus_ten, [1, 2, 3])))

# 람다 표현식에 조건부 표현식 사용하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))