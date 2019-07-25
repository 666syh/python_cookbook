"""
问题
你需要在数据序列上执行聚集函数(比如 sum() , min() , max() )， 
但是首先你需要先转换或者过滤数据
"""

nums = [1,2,3,4,5]
print(sum(x * x for x in nums))
# 55

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
# ACME,50,123.45

portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

print(min(s['shares'] for s in portfolio))
# 20
