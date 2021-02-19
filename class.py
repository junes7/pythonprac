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

# 메서드 안에서 메서드 호출하기
class Person:
    def greeting(self):
        print('Hello')
 
    def hello(self):
        self.greeting()    # self.메서드() 형식으로 클래스 안의 메서드를 호출
 
james = Person()
james.hello()    # Hello

# 속성 사용하기
class Person:
    def __init__(self):
        self.hello = '안녕하세요.'
        
	def greeting(self):
        print(self.hello)
james = Person()
james.greeting()	# 안녕하세요.

# 인스턴스를 만들 때 값 받기
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
        
	def greeting(self):
        print('{0} 저는 {1} 입니다.'.format(self.hello, self.name))
        
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting() # 안녕하세요. 저는 마리아입니다.
print('이름:', maria.name)	# 마리아
print('나이:', maria.age)		# 20
print('주소:', maria.address)	# 서울시 서초구 반포동

