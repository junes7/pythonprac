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

# 메타클래스 활용하기
class Singleton(type):    # type을 상속받음
    __instances = {}      # 클래스의 인스턴스를 저장할 속성
    def __call__(cls, *args, **kwargs):    # 클래스로 인스턴스를 만들 때 호출되는 메서드
        if cls not in cls.__instances:     # 클래스로 인스턴스를 생성하지 않았는지 확인
            cls.__instances[cls] = super().__call__(*args, **kwargs)
                                           # 생성하지 않았으면 인스턴스를 생성하여 속성에 저장
        return cls.__instances[cls]        # 클래스로 인스턴스를 생성했으면 인스턴스 반환
 
class Hello(metaclass=Singleton):    # 메타클래스로 Singleton을 지정
    pass
 
a = Hello()     # 클래스 Hello로 인스턴스 a 생성
b = Hello()     # 클래스 Hello로 인스턴스 b 생성
print(a is b)   # True: 인스턴스 a와 b는 같음

# 네이티브 코루틴 만들기
import asyncio
 
async def hello():    # async def로 네이티브 코루틴을 만듦
    print('Hello, world!')
 
loop = asyncio.get_event_loop()     # 이벤트 루프를 얻음
loop.run_until_complete(hello())    # hello가 끝날 때까지 기다림
loop.close()                        # 이벤트 루프를 닫음

# await로 네이트브 코루틴 실행하기
import asyncio
async def add(a, b):
    print('add: {0} + {1}'.format(a, b))
    await asyncio.sleep(1.0)    # 1초 대기. asyncio.sleep도 네이티브 코루틴
    return a + b    # 두 수를 더한 결과 반환
 
async def print_add(a, b):
    result = await add(a, b)    # await로 다른 네이티브 코루틴 실행하고 반환값을 변수에 저장
    print('print_add: {0} + {1} = {2}'.format(a, b, result))
 
loop = asyncio.get_event_loop()             # 이벤트 루프를 얻음
loop.run_until_complete(print_add(1, 2))    # print_add가 끝날 때까지 이벤트 루프를 실행
loop.close()                                # 이벤트 루프를 닫음

