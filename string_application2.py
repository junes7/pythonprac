xs = [()]
res = [False] * 2
if xs:
    res[0] = True
if xs[0]:
    res[1] = True
print(res)

# input string by using format specifier
print('I am %s.' % 'james')
# input string by using format specifier with variable
name = 'david'
print('I am %s.' % name)

# input number in string by using format speicifier
print('I am %d years old.' % 20)

# express decimal point by using format specifier
print('%f' % 2.3)

print('%10d' % 150)

print('%10d' % 15000)

# use format method
print('Hello, {0}'.format('world!'))
print('Hello, {0}'.format(100))


# input multiple value to format method
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))

# input multiple same value to format method
print('{0} {0} {1} {1}'.format('Python', 'Script'))


