"""
问题
怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)？
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 使用 zip() 函数先将键和值反转过来

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# (10.75, 'FB')

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
# (612.78, 'AAPL')

price_sorted = sorted(zip(prices.values(), prices.keys()))
print(price_sorted)
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'),
# (612.78, 'AAPL')]

