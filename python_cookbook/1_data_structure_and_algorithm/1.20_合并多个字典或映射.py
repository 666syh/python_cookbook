"""
问题
现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作， 
比如查找值或者检查某些键是否存在。
"""
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a, b)
print(c['x'], c['y'], c['z'])
# 1 2 3

print(len(c))
# 3
print(list(c.keys()))
# ['z', 'x', 'y']

print(list(c.values()))
# [1, 3, 2]


values = ChainMap()
values['x'] = 1
print(values)
# ChainMap({'x': 1})

values = values.new_child()
values['x'] = 2
print(values)
# ChainMap({'x': 2}, {'x': 1})

values = values.new_child()
values['x'] = 3
print(values)
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})

values = values.parents
print(values['x'])
# 2

values = values.parents
print(values['x'])
# 1

# 使用update来合并字典
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged.update(a)
print(merged)
# {'y': 2, 'z': 3, 'x': 1}


