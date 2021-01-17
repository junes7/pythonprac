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
import turtle as t
t = t.Turtle()
t.shape('turtle')
# t.color('green')
t.color('#FF69B4')  # 핫핑크
t.begin_fill()
for i in range(6):
    t.fd(100)
    t.rt(360/6)
t.end_fill()
input()






