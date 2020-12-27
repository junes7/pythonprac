# 국어, 영어, 수학, 과학 점수 입력받고 평균점수 출력 프로그램
a, b, c, d = map(int, input().split())
print(int((a+b+c+d)/4))
print((a+b+c+d)//4)
# 값을 여러 개 출력하기
print(1, 2, 3)
print('Hello', 'Python')
# sep로 값 사이에 문자 넣기
# sep에 콤마와 공백을 지정
print(1, 2, 3, sep=', ')
# sep에 콤마만 지정
print(4, 5, 6, sep=',')
# sep에 빈 문자열을 지정
print('Hello,', 'world!', sep='')
# sep에 x를 지정
print(1920, 1080, sep=' x ')
# 문자열 안에 \n을 사용하여 줄바꿈
print('1\n2\n3')
# sep에 줄바꿈을 지정
print(1, 2, 3, sep='\n')
# end 사용해 한 줄에 여러 개의 값을 출력
# end에 빈 문자열을 지정하면 다음 번 출력이
# 바로 뒤에 오게 된다.
print(1, end='')
print(2, end='')
print(3)
# end에 공백 한 칸 지정
print(1, end=' ')
print(2, end=' ')
print(3)
# 16:9 출력하는 방법
print(16, 9, sep=':')
print('Hello', 'Python', sep='\n')
print('Hello', '\n', 'Python', sep='')
print('Hello\nPython')
print('Hello', 'Python', end='\n\n')
print('Hello', 'Python')
# 날짜와 시간 출력하기
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

# year, month, day, hour, minute, second = input().split()
print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')

a = 20
b = 30
#c = -a
#c-=b
c = a + 10
#b + = a
#c = a // b
print(c)

# 입력받은 값을 콤마를 기준으로 분리
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
print(a, b, sep=', ')
print(a + b)

# 입력된 값을 실수로 변환하여 변수 두 개에 저장
a, b = map(float, input('실수를 입력하세요: ').split())
print(a, b, sep=', ')
print(a + b)