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
    