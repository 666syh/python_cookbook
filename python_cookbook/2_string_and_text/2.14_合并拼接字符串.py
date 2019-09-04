"""
问题
你想将几个小的字符串合并为一个大的字符串
"""
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
# Is Chicago Not Chicago?

print(','.join(parts))
# Is,Chicago,Not,Chicago?

a = 'Is Chicago'
b = 'Not Chicago?'
print(a+' '+b)
# Is Chicago Not Chicago?

print('{} {}'.format(a, b))
# Is Chicago Not Chicago?

a = 'Hello' 'World'
print(a)
# HelloWorld

data = ['Tom', 50, 91.1]
print(' '.join(str(d) for d in data))
# Tom 50 91.1

# print has join itself
print('a', 'b', 'c', sep=':')
# a:b:c
