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







