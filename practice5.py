#부등호 사용하기
# 10이 20보다 큰지 비교
print(10 > 20)
# 10이 20보다 작은지 비교
print(10 < 20)
# 10이 10보다 크거나 같은지 비교
print(10 >= 10)
# 10이 10보다 작거나 같은지 비교
print(10 <= 10)
# 객체가 같은지 다른지 비교하기
print(1 == 1.0)
print(1 is 1.0)
print(1 is not 1.0)
# 논리 연산자 사용하기
print(not True)
print(not False)
# and, or, not 논리 연산자가 식 하나에 들어있으면
# not, and, or 순으로 판단합니다.
print(not True and False or not False)
# 논리 연산자와 비교 연산자를 함께 사용하기
# True and True
print(10 == 10 and 10 != 5)
# True or False
print(10 > 5 or 10 < 3)
# not True
print(not 10 > 5)
# not False
print(not 1 is 1.0)
# 정수, 실수, 문자열을 불(bool)로 만들기
print(bool(2))
print(bool(0.0))
print(bool(1.5))
print(bool('False'))
print(bool(''))
print(bool(0))
# 첫 번째 값이 거짓이므로 두 번째 값은 확인하지 않고
# 거짓으로 결정
print(False and True)
print(False and False)
# 첫 번째 값이 참이므로 두 번째 값은 확인하지 않고
# 참으로 결정
print(True or True)
print(True or False)
# and 연산자
print(True and 'Python')
print('Python' and True)
print('Python' and False)
print(False and 'Python')
print(0 and 'Python')
# or 연산자
print(True or 'Python')
print('Python' or True)
print(False or 'Python')
print(0 or False)