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
