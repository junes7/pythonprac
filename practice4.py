# a를 b번 곱한 후 결과를 a에 할당
a = 5
b = 2
a **= b
print(a)
# numpy 모듈을 가져옴
import numpy as np
# 3x3 행렬 생성
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 3x3 행렬 생성
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 행렬 곱셈
print(a @ b)
c = a @ b
print('\n', c)
# 비교, 논리 연산자 알아보기
print(3 > 1)
# 10과 10이 같은지 비교
print(10 == 10)
# 10과 5가 다른지 비교
print(10 != 5)
# 문자열이 같은지 다른지 비교하기
print('Python' == 'Python')
print('Python' == 'python')
print('Python' != 'python')
# 연산자의 결과
print(6 == 2 * 3)
print(4 == 2 + 2)
print(2 * 3 is 3 + 3)
print(8 is 4 * 2.0)
print(5 is 6 - 1.1)
# 비교 연산자와 논리 연산자의 결과
a = 10
b = 20
print(a == 10 or b == 10)
print(a >= 10 and b < 30)
print(not a == 10)
print(b != 20 or a != 10)
print(not b != 20 and a > 5)
# 연습문제: 합격 여부 출력하기
# 국어, 영어, 수학, 과학 점수가 있을 때
# 한 과목이라도 50점 미만이면 불합격이다.
korean = 92
english = 47
mathematics = 86
science = 81
print(korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50)
# 국어는 90점 이상, 영어는 80점 초과,
# 수학은 85점 초과, 과학은 80점 이상일 때 합격이다.
korean, english, mathematics, science = map(int, input().split())
print(korean >= 90 and english > 80 and mathematics > 85 and science >= 80)
