"""
问题
你想使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串
"""

from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
# True

print(fnmatch('foo.txt', '?oo.txt'))
# True

print(fnmatch('dav32.csv', 'dav[0-9]*'))
# True

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
# ['Dat1.csv', 'Dat2.csv']

print(fnmatch('foo.txt', '*.TXT'))
# True

print(fnmatchcase('foo.txt', '*.TXT'))
# False
