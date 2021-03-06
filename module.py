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


# 스크립트 파일로 실행하거나 모듈로 사용하는 코드 만들기
# calc.py
def add(a, b):
    return a + b
 
def mul(a, b):
    return a * b
 
if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    print(add(10, 20))
    print(mul(10, 20))

# main.py
import calc
calc.add(50, 60)
calc.mul(50, 60)

# calcpkg 패키지에 모듈 만들기
# calcpkg/operation.py
def add(a, b):
    return a + b
 
def mul(a, b):
    return a * b

# calcpkg/geometry.py
def triangle_area(base, height):
    return base * height / 2
 
def rectangle_area(width, height):
    return width * height

# 패키지 사용하기
import calcpkg.operation    # calcpkg 패키지의 operation 모듈을 가져옴
import calcpkg.geometry     # calcpkg 패키지의 geometry 모듈을 가져옴
 
print(calcpkg.operation.add(10, 20))    # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10, 20))    # operation 모듈의 mul 함수 사용
 
print(calcpkg.geometry.triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용

# from import로 패키지의 모듈에서 변수, 함수, 클래스 가져오기
from calcpkg.operation import add, mul
add(10, 20)
mul(10, 20)

# 패키지에서 from import 응용하기
# __init__.py
from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴
# main.py
import calcpkg    # calcpkg 패키지만 가져옴
 
print(calcpkg.operation.add(10, 20))    # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10, 20))    # operation 모듈의 mul 함수 사용
 
print(calcpkg.geometry.triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용

# from import로 패키지에 속한 모든 변수, 함수, 클래스 가져오기
# calcpkg/__init__.py
# 현재 패키지의 operation, geometry 모듈에서 각 함수를 가져옴
from .operation import add, mul
from .geometry import triangle_area, rectangle_area

# calcpkg/main.py
from calcpkg import *    # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴
 
print(add(10, 20))    # operation 모듈의 add 함수 사용
print(mul(10, 20))    # operation 모듈의 mul 함수 사용
 
print(triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용
