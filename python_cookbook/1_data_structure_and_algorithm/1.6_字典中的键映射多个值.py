"""
问题
怎样实现一个键对应多个值的字典(也叫 multidict )？
"""

# 将多个值放在列表或集合里
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}


from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})

c = defaultdict(set)
c['a'].add(1)
c['a'].add(2)
c['b'].add(4)
print(c) 
# defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})

