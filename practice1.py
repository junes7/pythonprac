print('Hello, world!')
print('Python Programming')
a = 2 + 2 # 더하기
if a == 3:
    print(a)
else:
    print('3이')
    print('아닙니다.')
# 사칙연산
a1 = 6 + 8
a2 = 6 - 8
a3 = 6 * 8
print(a1, a2, a3)
b1 = 5 // 2
b2 = 5 / 2
b3 = 5 % 2
b4 = 5 ** 2
print(b1, b2, b3, b4)
# 값을 정수화(Casting)
c1 = int(3.4)
c2 = int(5/2)
c3 = int('10')
# 객체 자료형 표시
c4 = type(10.5)
print(c1, c2, c3, c4)
# 몫과 나머지를 함께 구하기
d1 = divmod(5, 2)
d2 = type(d1)
# quotient, remainder
qu, re = divmod(7, 3)
print(d1, d2)
print(qu, re)
# base2, base8, base16
e1 = 0b1110
e2 = 0o11
e3 = 0xF
print(e1, e2, e3)
# 실수 덧셈, 뺄셈, 곱셈, 나눗셈, 그리고 정수와 덧셈
f1 = 3.5 + 2.1
f2 = 4.3 - 2.7
f3 = 1.5 * 3.1
f4 = 5.5 / 3.1
f5 = 4.2 + 5
print(f1, f2, f3, f4, f5)
# 복소수(complex number)
g1 = complex(1.2, 1.3)
print(g1)
print(int(0.2467 * 12 + 4.159))
print(102 * 0.6 + 225)
# 변수 여러 개를 한 번에 만들기
x, y, z = 10, 20, 30
print(x, y, z)
x1 = y1 = z1 = 10
print(x1, y1, z1)
x2, y2 = 10, 20
print(x2, y2)
x2, y2 = y2, x2
print(x2, y2)
# 빈 변수를 만들때는 None을 할당
x= None
print(x)