print(list(range(0, 10)) + list(range(10, 20)))
print(tuple(range(0, 10)) + tuple(range(10, 20)))
print(list(range(0, 5, 2)) * 3)
print(tuple(range(0, 5, 2)) * 3)

# 요소에 값 할당하기
a = [0, 0, 0, 0, 0]
a[0] = 38
a[1] = 21
a[2] = 53
a[3] = 62
a[len(a)-1] = 19
print(a)
print(a[0], a[-2], a[4], sep=', ')


