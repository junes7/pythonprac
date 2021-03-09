import re
# 그룹 사용하기
m = re.match('([0-9]+) ([0-9]+)', '10 295')
m.group(1)    # 첫 번째 그룹(그룹 1)에 매칭된 문자열을 반환
m.group(2)    # 두 번째 그룹(그룹 2)에 매칭된 문자열을 반환
m.group()     # 매칭된 문자열을 한꺼번에 반환
m.group(0)    # 매칭된 문자열을 한꺼번에 반환

# 패턴에 매칭되는 모든 문자열 가져오기
re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')

# *, +와 그룹 활용하기
re.match('[a-z]+(.[a-z]+)*$', 'hello.world')    # .world는 문자열이므로 패턴에 매칭됨
re.match('[a-z]+(.[a-z]+)*$', 'hello.1234')     # .1234는 숫자이므로 패턴에 매칭되지 않음
re.match('[a-z]+(.[a-z]+)*$', 'hello')          # .뒤에 문자열이 없어도 패턴에 매칭됨

# 문자열 바꾸기
def multiple10(m):        # 매개변수로 매치 객체를 받음
    n = int(m.group())    # 매칭된 문자열을 가져와서 정수로 변환
    return str(n * 10)    # 숫자에 10을 곱한 뒤 문자열로 변환해서 반환

re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8')

