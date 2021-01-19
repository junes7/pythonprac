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
