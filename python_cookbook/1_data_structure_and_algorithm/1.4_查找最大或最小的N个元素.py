"""
问题
怎样从一个集合中获得最大或者最小的N个元素列表？
"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
# [42, 37, 23]

print(heapq.nsmallest(3, nums))
# [-4, 1, 2]


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s:s['price'])
print(cheap)
# [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, 
#   {'name': 'FB', 'shares': 200, 'price': 21.09}]

print(expensive)
# [{'name': 'AAPL', 'shares': 50, 'price': 5    43.22}, 
#   {'name': 'ACME', 'shares': 75, 'price': 115.65}]


# 实际是堆排序
heapq.heapify(nums)
print(nums)
# [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]


print(heapq.heappop(nums))
# -4

print(heapq.heappop(nums))
# 1

print(heapq.heappop(nums))
#2

