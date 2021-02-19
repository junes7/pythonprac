# 클래스 사용하기
# Person 클래스 정의
class Person:
    def greeting(self):
        print('Hello')

# 파이썬에서 흔히 볼 수 있는 클래스
a = int(10)
print(a)
b = list(range(10))
print(b)
c = dict(x = 10, y = 20)
print(c)
# type 객체
a = 10
print(type(a))
b = [0, 1, 2]
print(type(b))
c = {'x': 10, 'y': 20}
print(type(c))
maria = Person()
print(type(maria))

