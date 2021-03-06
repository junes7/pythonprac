#x = input()
#print('실행결과:'+x)
# 입력을 받는 상태인지 출력이 없는 상태인지
# 알기 위해 input 함수 안에 문자열을 지정
x = input('문자열을 입력하세요: ')
print('실행결과:'+x)
# 두 숫자의 합
a = input('첫 번째 숫자를 입력하세요: ')
b = input('두 번째 숫자를 입력하세요: ')
print(a + b)
# input 입력 값은 항상 문자열이기 때문에 '1020' 값이 나온다.
# 따라서 입력 받은 문자열을 정수로 변환 후 더하기 계산
a = int(input('첫 번째 숫자를 입력하세요: '))
b = int(input('두 번째 숫자를 입력하세요: '))
print(a + b)
# 입력받은 값을 공백을 기준으로 분리해
# 변수 두 개에 저장하기
a, b = input('문자열 두 개를 입력하세요: ').split()
print(a)
print(b)
# 입력받은 값을 공백을 기준으로 분리
a, b = input('숫자 두 개를 입력하세요: ').split()
a = int(a)
b = int(b)
print(a + b)
# map 함수를 사용해 한 번에 여러 입력 문자열 정수형으로 변환
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
print(a + b)
# 정수 세 개를 입력받고 합계 출력하기
a, b, c = map(int, input('숫자 세 개를 입력하세요: ').split())
print(a + b + c)
# 50, 100, None이 각 줄에 출력되게 하기
a = int(50)
b = 2*a
c = None
print(a)
print(b)
print(c)
# 두 번째 방법: 세 변수 한 번에 만들면서 값을 할당
a, b, c = int(50), int(100), None
print(a, b, c, sep='\n')