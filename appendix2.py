import datetime
# 문자열로 날짜/시간 객체 만들기
d = datetime.datetime.strptime('2021-03-12', '%Y-%m-%d')
print(d)

# 날짜/시간 객체를 문자열로 만들기
print(d.strftime('%Y-%m-%d'))
print(d.strftime('%c'))

# 날짜와 시간 속성에 접근하기
today = datetime.datetime.today()
print(today.year, today.month, today.day, today.hour, today.minute, today.second, today.microsecond)

# 날짜와 시간 차이 계산하기
d = datetime.datetime(2021, 3, 13)
from datetime import timedelta
print(d - timedelta(days=20))
print(datetime.datetime(2021, 3, 13) - datetime.datetime(2021, 2, 1))

# 두 실수가 같은지 판단하기
import math, sys
x = 0.1 + 0.2
print(math.fabs(x - 0.3) <= sys.float_info.epsilon)
# 파이썬 3.5 이상부터는 math.isclose함수를 사용해 두 실수가 같은지 판단
print(math.isclose(0.1 + 0.2, 0.3))

# Decimal으로 정확한 자릿수 표현하기
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))

# fraction으로 분수 표현하기
from fractions import Fraction
print(Fraction('10/3'))    # 10을 3으로 나누면 순환소수 3.33333...이지만 분수 3분의 10으로 표현

# with as에 사용할 수 있는 클래스 만들기
class OpenHello:
    def __enter__(self):
        self.file = open('hello.txt', 'w')    # 파일 객체를 속성에 저장
        return self.file     # __enter__에서 값을 반환하면 as에 지정한 변수에 들어감
 
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()    # __exit__에서 파일 객체 닫기
 
with OpenHello() as hello:
    hello.write('Hello, world!')

# type를 사용하여 동적으로 클래스 생성하기
Hello = type('Hello', (), {})    # type으로 클래스 Hello 생성
print(Hello)
h = Hello()                      # 클래스 Hello로 인스턴스 h 생성
print(h)

# type을 상속받아서 메타클래스 구현하기
class MakeCalc(type):    # type을 상속받음
    def __new__(metacls, name, bases, namespace):      # 새 클래스를 만들 때 호출되는 메서드
        namespace['desc'] = '계산 클래스'              # 새 클래스에 속성 추가
        namespace['add'] = lambda self, a, b: a + b    # 새 클래스에 메서드 추가
        return type.__new__(metacls, name, bases, namespace)    # type의 __new__ 호출
 
Calc = MakeCalc('Calc', (), {})    # 메타클래스 MakeCalc로 클래스 Calc 생성
c = Calc()                         # 클래스 Calc로 인스턴스 c 생성
print(c.desc)                      # '계산 클래스': 인스턴스 c의 속성 출력
print(c.add(1, 2))                 # 3: 인스턴스 c의 메서드 호출
