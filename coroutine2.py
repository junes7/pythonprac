# 하위 코루틴의 반환값 가져오기
def accumulate():
    total = 0
    while True:
        x = (yield)         # 코루틴 바깥에서 값을 받아옴
        if x is None:       # 받아온 값이 None이면
            return total    # 합계 total을 반환
        total += x
 
def sum_coroutine():
    while True:
        total = yield from accumulate()    # accumulate의 반환값을 가져옴
        print(total)
 
co = sum_coroutine()
next(co)
 
for i in range(1, 11):    # 1부터 10까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄
 
for i in range(1, 101):   # 1부터 100까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

# StopIteration 예외 발생시키기
def accumulate():
    total = 0
    while True:
        x = (yield)                       # 코루틴 바깥에서 값을 받아옴
        if x is None:                     # 받아온 값이 None이면
            raise StopIteration(total)    # StopIteration에 반환할 값을 지정(파이썬 3.6 이하)
        total += x
 
def sum_coroutine():
    while True:
        total = yield from accumulate()    # accumulate의 반환값을 가져옴
        print(total)
 
co = sum_coroutine()
next(co)
 
for i in range(1, 11):    # 1부터 10까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄
 
for i in range(1, 101):   # 1부터 100까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

# 함수의 시작과 끝 출력
def hello():
    print('hello 함수 시작')
    print('hello')
    print('hello 함수 끝')
 
def world():
    print('world 함수 시작')
    print('world')
    print('world 함수 끝')
 
hello()
world()

# 데코레이터 사용해 함수의 시작과 끝 출력
def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():                           # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
def hello():
    print('hello')
 
def world():
    print('world')
 
trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
trace_hello()                 # 반환된 함수를 호출
trace_world = trace(world)    # 데코레이터에 호출할 함수를 넣음
trace_world()                 # 반환된 함수를 호출

# @으로 데코레이터 사용하기
def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
@trace    # @데코레이터
def hello():
    print('hello')
 
@trace    # @데코레이터
def world():
    print('world')
 
hello()    # 함수를 그대로 호출
world()    # 함수를 그대로 호출

# 데코레이터를 여러 개 지정하기
def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper
 
def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper
 
# 데코레이터를 여러 개 지정
@decorator1
@decorator2
def hello():
    print('hello')
 
hello()

# 매개변수와 반환값을 처리하는 데코레이터 만들기
def trace(func):          # 호출할 함수를 매개변수로 받음
    def wrapper(a, b):    # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
        r = func(a, b)    # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
        return r          # func의 반환값을 반환
    return wrapper        # wrapper 함수 반환
 
@trace              # @데코레이터
def add(a, b):      # 매개변수는 두 개
    return a + b    # 매개변수 두 개를 더해서 반환
 
print(add(10, 20))

# 가변 인수 함수 데코레이터
def trace(func):                     # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs):    # 가변 인수 함수로 만듦
        r = func(*args, **kwargs)    # func에 args, kwargs를 언패킹하여 넣어줌
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
                                     # 매개변수와 반환값 출력
        return r                     # func의 반환값을 반환
    return wrapper                   # wrapper 함수 반환
 
@trace                   # @데코레이터
def get_max(*args):      # 위치 인수를 사용하는 가변 인수 함수
    return max(args)
 
@trace                   # @데코레이터
def get_min(**kwargs):   # 키워드 인수를 사용하는 가변 인수 함수
    return min(kwargs.values())
 
print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))