# 정규표현식 사용하기
# 문자열 판단하기
import re
re.match('Hello', 'Hello, world!')     # 문자열이 있으므로 정규표현식 매치 객체가 반환됨
re.match('Python', 'Hello, world!')    # 문자열이 없으므로 아무것도 반환되지 않음

# 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단하기
re.search('^Hello', 'Hello, world!')     # Hello로 시작하므로 패턴에 매칭됨
re.search('world!$', 'Hello, world!')    # world!로 끝나므로 패턴에 매칭됨

# 지정된 문자열이 하나라도 포함되는지 판단하기
re.match('hello|world', 'hello')    # hello 또는 world가 있으므로 패턴에 매칭됨

# 범위 판단하기
re.match('[0-9]*', '1234')    # 1234는 0부터 9까지 숫자가 0개 이상 있으므로 패턴에 매칭됨
re.match('[0-9]+', '1234')    # 1234는 0부터 9까지 숫자가 1개 이상 있으므로 패턴에 매칭됨
re.match('[0-9]+', 'abcd')    # abcd는 0부터 9까지 숫자가 1개 이상 없으므로 패턴에 매칭되지 않음

# 문자가 한 개만 있는지 판단하기
re.match('abc?d', 'abd')         # abd에서 c 위치에 c가 0개 있으므로 패턴에 매칭됨
re.match('ab[0-9]?c', 'ab3c')    # [0-9] 위치에 숫자가 1개 있으므로 패턴에 매칭됨
re.match('ab.d', 'abxd')         # .이 있는 위치에 문자가 1개 있으므로 패턴에 매칭됨
