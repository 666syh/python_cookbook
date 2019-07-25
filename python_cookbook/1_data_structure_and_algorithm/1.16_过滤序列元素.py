"""
问题
你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
"""

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
# [1, 4, 10, 2, 3]

print([n for n in mylist if n < 0])
# [-5, -7, -1]

# 使用生成器
pos = (n for n in mylist if n > 0)
print(pos)
# <generator object <genexpr> at ...>

for i in pos:
    print(i)
# 1
# 4
# 10
# 2
# 3

# 过滤规则比较复杂
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)
# ['1', '2', '-3', '4', '5']

import math
print([math.sqrt(n) for n in mylist if n > 0])
# [1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]

# 替代不符合的值，而不是丢弃
print([n if n > 0 else 0 for n in mylist])
# [1, 4, 0, 10, 0, 2, 3, 0]

print([n if n < 0 else 0 for n in mylist])
# [0, 0, -5, 0, -7, 0, 0, -1]


addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
# [False, False, True, False, False, True, True, False]

print(list(compress(addresses, more5)))
# ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']

