# 10진수와 2진수 변환하기
bin(13) # 10진수 13을 2진수로 변환
0b1101	# 2진수 1101을 10진수로 변환
int('1101', 2)    # 2진수로 된 문자열 1101을 10진수로 변환

# 비트 논리 연산자 사용하기
bin(0b1101 & 0b1001)    # 비트 AND
13 & 9                  # 비트 AND
bin(0b1101 | 0b1001)    # 비트 OR
13 | 9                  # 비트 OR
bin(0b1101 ^ 0b1001)    # 비트 XOR
13 ^ 9                  # 비트 XOR
bin(~0b1101)            # 비트 NOT
~13                     # 비트 NOT

# 시프트 연산자 사용하기
0b0011 << 2    # 비트를 왼쪽으로 2번 이동
bin(12)
0b1100 >> 2    # 비트를 오른쪽으로 2번 이동
bin(3)

# bytes
bytes(10)    # 0이 10개 들어있는 바이트 객체 생성
bytes([10, 20, 30, 40, 50])    # 리스트로 바이트 객체 생성
bytes(b'hello')    # 바이트 객체로 바이트 객체 생성

# bytearray
x = bytearray(b'hello')
x[0] = ord('a')    # ord는 문자의 ASCII 코드를 반환
print(x)

# 바이트 자료형과 인코딩
'hello'.encode()     # str을 bytes로 변환
'안녕'.encode('euc-kr')
'안녕'.encode('utf-8')
b'hello'.decode()    # bytes를 str로 변환
x = '안녕'.encode('euc-kr')
x.decode('euc-kr')
y = '안녕'.encode('utf-8')
y.decode('utf-8')
bytes('안녕', encoding='euc-kr')
bytearray('안녕', encoding='cp949')

# time 모듈로 현재 시간 구하기
import time
print(time.time())

# 날짜와 시간 형태로 변환하기
print(time.localtime(time.time()))

# 날짜/시간 포맷에 맞춰서 출력하기
print(time.strftime('%Y-%m-%d-%H-%M-%p', time.localtime(time.time())))
print(time.strftime('%x-%X', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

# datetime 모듈로 현재 날짜와 시간 구하기
import datetime
print(datetime.datetime.today())
print(datetime.datetime.now())

# 특정 날짜와 시간으로 객체 만들기
d = datetime.datetime(2021, 3, 12)
print(d)






