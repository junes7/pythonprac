# 국어, 영어, 수학, 과학 점수 입력받고 평균점수 출력 프로그램
#a, b, c, d = map(int, input().split())
#print(int((a+b+c+d)/4))
# 값을 여러 개 출력하기
print(1, 2, 3)
print('Hello', 'Python')
# sep로 값 사이에 문자 넣기
# sep에 콤마와 공백을 지정
print(1, 2, 3, sep=', ')
# sep에 콤마만 지정
print(4, 5, 6, sep=',')
# sep에 빈 문자열을 지정
print('Hello,', 'world!', sep=' ')
# sep에 x를 지정
print(1920, 1080, sep=' x ')
# sep에 줄바꿈을 지정
print(1, 2, 3, sep='\n')
# end 사용해 한 줄에 여러 개의 값을 출력
# end에 빈 문자열을 지정하면 다음 번 출력이
# 바로 뒤에 오게 된다.
print(1, end='')
print(2, end='')
print(3)
