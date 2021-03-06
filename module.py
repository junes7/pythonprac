# 모듈 만들기
base = 2          # 변수
 
def square(n):    # 함수
    return base ** n

# 모듈 사용하기
import square2               # import로 square2 모듈을 가져옴
 
print(square2.base)          # 모듈.변수 형식으로 모듈의 변수 사용
print(square2.square(10))    # 모듈.함수() 형식으로 모듈의 함수 사용

# from import로 변수, 함수 가져오기
from square2 import base, square
print(base)
square(10)

# 모듈과 시작점 알아보기
# hello.py
print('hello 모듈 시작')
print('hello.py __name__:', __name__)    # __name__ 변수 출력
print('hello 모듈 끝')
# main.py
import hello    # hello 모듈을 가져옴
 
print('main.py __name__:', __name__)    # __name__ 변수 출력