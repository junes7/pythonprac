def hello():
    print('Hello, world!')
 
hello()

# 덧셈 함수 만들기
def add(a, b):
    print(a + b)

add(10, 20)
# 함수에서 값을 여러 개 반환하기
def add_sub(a, b):
    return a + b, a - b
x = add_sub(10, 20)
print(x)