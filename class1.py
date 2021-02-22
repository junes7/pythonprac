# 비공개 클래스 속성 사용하기
# class Knight:
#     __item_limit = 10    # 비공개 클래스 속성
 
#     def print_item_limit(self):
#         print(Knight.__item_limit)    # 클래스 안에서만 접근할 수 있음
 
 
# x = Knight()
# x.print_item_limit()    # 10
 
# print(Knight.__item_limit)    # 클래스 바깥에서는 접근할 수 없음

# 클래스와 메서드의 독스트링 사용하기
class Person:
    '''사람 클래스입니다.'''
    
    def greeting(self):
        '''인사 메서드입니다.'''
        print('Hello')
 
print(Person.__doc__)             # 사람 클래스입니다.
print(Person.greeting.__doc__)    # 인사 메서드입니다.
 
maria = Person()
print(maria.greeting.__doc__)     # 인사 메서드입니다.

# 정적 메서드 사용하기
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출

# 파이썬 자료형의 인스턴스 메서드와 정적 메서드
a = {1, 2, 3, 4}
a.update({5}) # 인스턴스 메서드
print(a)
print(set.union({1, 2, 3, 4}, {5}))