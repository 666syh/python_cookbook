"""
问题
怎样在两个字典中寻找相同点(比如相同的键、相同的值等等)？
"""

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# 集合操作
# 交集
print(a.keys() & b.keys())
# {'y', 'x'}

# 补集
print(a.keys() - b.keys())
# {'z'}

print(a.items() & b.items())
# {('y', 2)}

