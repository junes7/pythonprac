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