"""
问题
你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的。
"""

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 捕获分组

field = re.split(r'(;|,|\s)\s*', line)
print(field)
# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

values = field[::2]
delimiter = field[1::2]+['']
print(''.join(v+d for v, d in zip(values, delimiter)))
# asdf fjdk;afed,fjek,asdf,foo
