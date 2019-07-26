"""
问题
你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme等等。
"""

filename = 'spam.txt'
print(filename.endswith('txt'))
# True

print(filename.startswith('file'))
# False

url = 'http://www.python.org'
print(url.startswith('http:'))
# True

filename = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]

# need a tuple, not a list
print([name for name in filename if name.endswith(('.c', '.h'))])
# ['foo.c', 'spam.c', 'spam.h']


