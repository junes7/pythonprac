# collections 모듈에서 deque를 가져옴
from collections import deque
a = deque([10, 20, 30])
print(a)
# 덱의 오른쪽에 500 추가
a.append(500)
print(a)
# 덱의 왼쪽 요소 하나 삭제
a.popleft()
print(a)

# sort 메서드와 sorted 함수
a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a)
b = [10, 20, 30, 15, 20, 40]
c = sorted(b)
print(c)

# 리스트의 모든 요소를 삭제하기
a = [10, 20, 30]
a.clear()
print(a)
b = [10, 20, 30]
del b[:]
print(b)

# 리스트를 슬라이스로 조작하기
a = [10, 20, 30]
a[len(a):] = [500]
print(a)

# 리스트가 비어 있는지 확인하기
# seq = []
seq = [10, 20, 30]
if seq:
    print(seq[-1])
else:
    print('empty list')

# 인덱스와 요소를 함께 출력하기
a = [38, 21, 53, 62, 19]
# for index, value in enumerate(a):
#     print(index, value)
    # 인덱스를 0이 아니라 1부터 출력하고 싶을 때
    # print(index+1, value)
# 파이썬에서는 위 방법 대신 enumerate에 start index를 지정해주면 된다.
for idx, val in enumerate(a, start=1):
    print(idx, val)

# for 반복문에서 인덱스로 요소를 출력하기
for i in range(len(a)):
    if i == 2:
        print(a[i])
