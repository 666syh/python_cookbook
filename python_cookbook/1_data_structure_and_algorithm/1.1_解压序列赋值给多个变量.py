'''
问题
现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量？
'''

p = (1,2)
x, y = p
print(x, y)

data = ['Bob', 50, 91.1, (2019, 7, 10)]
name, shares, price, (year, month, day) = data
print(name, shares, price, year, month, day)

'''
实际上，这种解压赋值可以用在任何可迭代对象上面，
而不仅仅是列表或者元组。 包括字符串，文件对象，迭代器和生成器。
'''

s = "hello"
a,b,c,d,e = s
print(a,b,c,d,e)

_,a,b,_,_ = s
print(a,b)