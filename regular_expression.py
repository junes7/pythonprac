# 정규표현식 사용하기
# 문자열 판단하기
import re
re.match('Hello', 'Hello, world!')     # 문자열이 있으므로 정규표현식 매치 객체가 반환됨
re.match('Python', 'Hello, world!')    # 문자열이 없으므로 아무것도 반환되지 않음

# 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단하기
re.search('^Hello', 'Hello, world!')     # Hello로 시작하므로 패턴에 매칭됨
re.search('world!$', 'Hello, world!')    # world!로 끝나므로 패턴에 매칭됨








