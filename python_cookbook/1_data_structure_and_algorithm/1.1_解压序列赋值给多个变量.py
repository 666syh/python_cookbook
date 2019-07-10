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
