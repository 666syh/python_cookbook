"""
问题
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 
那么怎样才能从这个可迭代对象中解压出N个元素出来？
"""

def dropFirstLast(li):
    first, *middle, last = li
    return middle
print(dropFirstLast([1,2,3,4,5]))
# [2, 3, 4]

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone = record
print(phone)    #此时phone是一个list
# ['773-555-1212', '847-555-1212']


records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    if tag == 'bar':
        do_bar(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *filed, homedir, sh = line.split(":")
print(filed)
# ['*', '-2', '-2', 'Unprivileged User']


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)
# ACME 2012

'''
    递归
'''
def sum(item):
    head, *tail = item
    return head+sum(tail) if tail else head

print(sum([1,2,3,4,5,6,7]))
# 28