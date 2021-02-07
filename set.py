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

a & b
{3, 4}
>>> set.intersection(a, b)
{3, 4}

a - b
{1, 2}
>>> set.difference(a, b)
{1, 2}