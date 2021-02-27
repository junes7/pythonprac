# 제너레이터 만들기
def number_generator(stop):
    n = 0              # 숫자는 0부터 시작
    while n < stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때 반복
        yield n        # 현재 숫자를 바깥으로 전달
        n += 1         # 현재 숫자를 증가시킴
 
for i in number_generator(3):
    print(i)

# yield에서 함수 호출하기
def upper_generator(x):
    for i in x:
        yield i.upper() # 함수의 반환값을 바깥으로 전달
        
fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits):
    print(i)

# yield from 으로 값을 여러 번 바깥으로 전달하기
def number_generator():
    x = [1, 2, 3]
    for i in x:
        yield i
 
for i in number_generator():
    print(i)

def number_generator():
    x = [1, 2, 3]
    yield from x    # 리스트에 들어있는 요소를 한 개씩 바깥으로 전달
 
for i in number_generator():
    print(i)

g = number_generator()
next(g)
next(g)
next(g)
next(g)

# yield from에 제너레이터 객체 지정하기
def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1
        
def three_generator():
    # 숫자를 세 번 바깥으로 전달
    yield from number_generator(3)
    
for i in three_generator():
    print(i)


