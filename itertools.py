from itertools import permutations
# permutations
# 데이터 준비
data = ['A', 'B', 'C']
# 모든 순열 구하기
result = list(permutations(data, 3))
print(result)

from itertools import combinations
# combinations
# 데이터 준비
data = ['A', 'B', 'C']
# 2개를 뽑는 모든 조합 구하기
result = list(combinations(data, 2))
print(result)

from itertools import product
# 데이터 준비
data = ['A', 'B', 'C']
# 2개를 뽑는 모든 순열 구하기(중복 허용)
result = list(product(data, repeat=2))
print(result)

