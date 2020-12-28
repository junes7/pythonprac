# 문자열 사용하기
hello = 'Hello, world!'
print(hello)
hello1 = '안녕하세요'
print(hello1)
hello2 = "Hello, Program"
print(hello2)
hello3 = '''Hello, Python!'''
print(hello3)
python = """Python Programming"""
print(python)
# 여러 줄로 된 문자열(multiline string) 사용하기
hello = '''Hello, world!
안녕하세요.
Python입니다.'''
print(hello)
# 문자열 안에 작은따옴표나 큰따옴표 포함하기
s = 'He said "Python is easy".'
s1 = "Python isn't difficult."
s2 = """"Hello", Python"""
s3 = """Hello, 'Python'"""
print(s, s1, s2, s3, sep='\n')
s = 'Python isn\'t difficult.'
s1 = 'Hello, \'Python\''
print(s, s1, sep='\n')
# 연습문제: 여러 줄로 된 문자열 사용하기
s = '''Python is a programming language that lets you work quickly
and
integrate systems more effectively.'''
print(s)
# 심사문제: 여러 줄로 된 문자열 사용하기
# s = '''\'Python\' is a "programming language"
# that lets you work quickly
# and
# integrate systems more effectively.'''
# 다른 방법
s = """'Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively."""
print(s)
# 리스트 만들기
a = [38, 21, 53, 62, 19]
person = ['james', 17, 175.3, True]
print(a)
print(person)
