# 함수 안에서 전역 변수 변경하기
x = 10		# 전역 변수
def foo():
    x = 20	# x는 foo의 지역 변수
    print(x)# foo의 지역 변수 출력
foo()
print(x)	# 전역 변수 출력

# 함수 안에서 함수 만들기
def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()
print_hello()

# 클로져 사용하기
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환
 
c = calc()
print(c(1), c(2), c(3), c(4), c(5))

# lambda로 클로저 만들기
def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환
 
c = calc()
print(c(1), c(2), c(3), c(4), c(5))

# 클로저의 지역 변수 변경하기
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
 
c = calc()
c(1)
c(2)
c(3)



