"""
问题
你想创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。
"""

s = '{name} has {n} messages.'
print(s.format(name='Bob', n=36))
# Bob has 36 messages.

# use vars() 变量域
name = 'Tom'
n = 12
print(s.format_map(vars()))
# Tom has 12 messages.

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Henry', 20)
print(s.format_map(vars(a)))
# Henry has 20 messages.

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'
del n
print(s.format_map(safesub(vars())))
# Tom has {n} messages.

import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Jorge'
n = 28
print(sub('Hello {name}'))
# Hello Jorge
print(sub('You have {n} messages.'))
# You have 28 messages.
print(sub('Your favorite color is {color}'))
# Your favorite color is {color}