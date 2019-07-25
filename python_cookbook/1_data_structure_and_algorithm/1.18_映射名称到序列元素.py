"""
问题
你有一段通过下标访问列表或者元组中元素的代码，
但是这样有时候会使得你的代码难以阅读， 于是你想通过名称来访问元素。
"""

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2019-10-19')

print(sub)
# Subscriber(addr='jonesy@example.com', joined='2019-10-19')

print(sub.addr, sub.joined)
# jonesy@example.com 2019-10-19

print(len(sub))
# 2

addr, join = sub
print(addr, join)
# jonesy@example.com 2019-10-19

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
# Stock(name='ACME', shares=100, price=123.45, date=None, time=None)


