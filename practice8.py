# 심사문제: 온라인 할인 쿠폰 시스템 만들기
price = int(input())
coupon = input()
if coupon == 'Cash3000':
    price -= 3000
if coupon == 'Cash5000':
    price -= 5000
print(price)