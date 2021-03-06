# 문자열 바꾸기
print('Hello, world!'.replace('world', 'Python'))
s = 'Hello, world!'
s = s.replace('world', 'Python')
print(s)

# 문자 바꾸기
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))

# 문자열 분리하기 - 기준 문자열이 공백일 때
print('apple pear graph pineapple orange'.split())
# 기준 문자열이 ,(콤마)와 공백일 때
print('apple, pear, graph, pineapple, orange'.split(', '))

# 구분자 문자열과 문자열 리스트 연결하기
# 구분자 문자열이 공백일 때
print(' '.join(['apple', 'pear', 'graph', 'pineapple', 'orange']))
# 구분자 문자열이 -(하이픈)일 때
print('-'.join(['apple', 'pear', 'graph', 'pineapple', 'orange']))

# 소문자를 대문자로 바꾸기
print('python'.upper())

# 대문자를 소문자로 바꾸기
print('PYTHON'.lower())

# 왼쪽 공백 삭제하기
print('   Python   '.lstrip())

# 오른쪽 공백 삭제하기
print('   Python   '.rstrip())

# 양쪽 공백 삭제하기
print('   Python   '.strip())

# 왼쪽의 특정 문자 삭제하기
print(', python.'.lstrip(',.'))

# 오른쪽의 특정 문자 삭제하기
print(', python.'.rstrip(',.'))

# 양쪽의 특정 문자 삭제하기
print(', python.'.strip(',.'))

# 구두점을 간단하게 삭제하기
import string
print(', python.'.strip(string.punctuation))
print(string.punctuation)
# 구두점이랑 공백 삭제하기
print(', python.'.strip(string.punctuation + ' '))
# 메서드 체이닝 이용하기
print(', python.'.strip(string.punctuation).strip())

# 문자열을 왼쪽 정렬하기
print('python'.ljust(10))

# 문자열을 오른쪽 정렬하기
print('python'.rjust(10))
# 메서드 체이닝 사용해서 대문자로 오른쪽 정렬하기
print('python'.rjust(10).upper())

# 문자열을 가운데 정렬하기
print('python'.center(10))

# 문자열 왼쪽에 0 채우기
# 숫자 앞에 0을 채움
print('35'.zfill(4))

# 숫자 앞에 0을 채움
print('3.5'.zfill(6))

# 문자열 앞에 0을 채울 수도 있음
print('hello'.zfill(10))

# 문자열 위치 찾기
print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy'))

# 오른쪽에서부터 문자열 위치 찾기
print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))

# 문자열 개수 세기
print('apple pineapple'.count('pl'))

