# 심사문제: 온라인 할인 쿠폰 시스템 만들기
price = int(input())
coupon = input()
if coupon == 'Cash3000':
    price -= 3000
if coupon == 'Cash5000':
    price -= 5000
print(price)

x = 10
y = 20
if x == 10 and y == 20:
    print(True)
else:
    print(False)

# 연습문제: 합격 여부 판단하기
written_test = 75
coding_test = True
if written_test >= 80 and coding_test == True:
	print('합격')
else:
   	print('불합격')
# 심사문제: 합격 여부 판단하기
korean, english, math, science = map(int, input().split())
if (0 <= korean <= 100) and (0 <= english <= 100) and (0 <= math <= 100) and (0 <= science <= 100):
    avg = (korean + english + math + science)/4.0
    if avg >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')