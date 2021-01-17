# 일반 형태로 사각형 구현
# import turtle as t
# t = t.Turtle()
# t.shape('turtle')
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# input()
# 축약 코드로 사각형 구현
# import turtle as t
# t= t.Turtle()
# t.shape('turtle')
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# input()
# 반복 코드로 사각형 구현
# t.shape('turtle')
# for i in range(4):
#     t.fd(100)
#     t.rt(90)
# input()
# 반복 코드로 오각형 구현
# import turtle as t
# t= t.Turtle()
# # 오각형이므로 5번 반복
# for i in range(5):
#     t.fd(100)
#     # 360을 5로 나누어서 외각을 구함
#     t.rt(360/5)
# input()
# 반복 구문으로 다각형 구현
# import turtle as t
# t = t.Turtle()
# t.shape('turtle')
# n = int(input())
# for i in range(n):
#     t.fd(100)
#     t.rt(360/n)
# input()
# 다각형에 색칠하기
# import turtle as t
# n = 6				# 육각형
# t = t.Turtle()
# t.shape('turtle')
# t.color('#FF69B4')	# 펜의 색을 핫핑크색으로 지정
# t.begin_fill()		# 색칠할 영역 시작
# for i in range(n):	# n번 반복
#     t.fd(100)
#     t.rt(360/6)		# 360을 n으로 나누어서 외각을 구함
# t.end_fill()		# 색칠할 영역 끝
# input()
# 초록색 원 그리기
# import turtle as t
# t = t.Turtle()
# t.shape('turtle')
# t.color('green')
# t.begin_fill()
# t.circle(120)
# t.end_fill()
# input()
# 파란색 원 60번 반복해서 그리기
# import turtle as t
# t = t.Turtle()
# n = 60
# t.shape('turtle')
# t.speed('fastest')
# t.color('blue')
# for i in range(n):
#     t.circle(120)
#     t.rt(360/n)
# input()
# 선으로 복잡한 무늬 그리기
# 300번 반복, 오른쪽 91도, 반복할 때마다 forward i 증가
# import turtle as t
# n = 300
# t = t.Turtle()
# t.shape('turtle')
# t.speed('fastest')
# t.color('brown')
# for i in range(n):
#     t.forward(i)
#     t.right(91)
# input()
# 연습문제: 오각별 그리기
# import turtle as t
# n = 5
# t = t.Turtle()
# t.shape('turtle')
# # 핫핑크 색
# t.color('#FF69B4')
# for i in range(n):
#     t.fd(100)
#     t.rt((360/n)*2)
#     t.fd(100)
#     t.lt(360/n)
# input()
# 심사문제: 별 그리기
import turtle as t
n, line = map(int, input().split())
t = t.Turtle()
t.shape('turtle')
t.color('purple')
t.speed('fastest')
for i in range(n):
    t.forward(line)
    t.rt((360/n)*2)
    t.forward(line)
    t.lt(360/n)
input()


