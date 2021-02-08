# 세트 만들기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)

# set를 사용하여 세트 만들기
a = set('apple')
print(a)

# 세트에 특정 값이 있는지 확인하기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print('orange' in fruits)
print('peach' in fruits)

# 집합 연산 사용하기
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(set.union(a, b))