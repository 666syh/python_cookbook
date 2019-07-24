"""
问题
你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。
"""

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
# 51325.0

# modify
SHARE = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARE]) * float(record[PRICE])
print(cost)
# 51325.0

items = [0,1,2,3,4,5,6]
a = slice(2, 4)
print(items[a])
# [2, 3]

items[a] = [10, 11]
print(items)
# [0, 1, 10, 11, 4, 5, 6]

del items[a]
print(items)
# [0, 1, 4, 5, 6]

s = slice(5, 50, 2)
print(s.start, s.stop, s.step)
# 5 50 2


