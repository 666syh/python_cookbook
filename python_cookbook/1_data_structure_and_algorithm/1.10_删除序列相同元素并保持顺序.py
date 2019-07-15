"""
问题
怎样在一个序列上面保持元素顺序的同时消除重复的值？
"""

# 如果序列上的值都是 hashable 类型
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item

a = [1,2,3,4,5,5,6,3]
print(list(dedupe(a)))
# [1, 2, 3, 4, 5, 6]

# unhashable
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            seen.add(val)
            yield item

d = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe2(d, key=lambda x : x['x'])))
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
