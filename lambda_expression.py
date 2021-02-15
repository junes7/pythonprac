# 람다 표현식으로 함수 만들기
def plus_ten(x):
    return x + 10
print(plus_ten(1))

print(lambda x: x + 10)

plus_ten = lambda x: x + 10
print(plus_ten(1))

# 람다 표현식 자체를 호출하기
print((lambda x: x + 10)(1))