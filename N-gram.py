# 단어 단위 N-gram 만들기
n = int(input())
text = input()
words = text.split()
if (len(words) < n):
    print('wrong')
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)
