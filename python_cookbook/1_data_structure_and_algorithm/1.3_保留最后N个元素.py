"""
问题
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
"""

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

# 打印所有包含 print 的行以及这些行的前边三行
def do():
    with open("D:\\workplace\\python cookbook\\python_cookbook\\1_data_structure_and_algorithm\\1.2_解压可迭代对象赋值给多个变量.py", encoding='utf-8') as f:
        for line, prevlines in search(f, 'print', 3):
            for pline in prevlines:
                print(pline, end='')
            print(line,end='')
            print('-' * 20)
# do()

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
# deque([1, 2, 3], maxlen=3)

q.append(4)
print(q)
# deque([2, 3, 4], maxlen=3)

q = deque() # 无限大小
q.append(1)
q.append(2)
q.append(3)
print(q)
# deque([1, 2, 3])

q.appendleft(4)
print(q)
# deque([4, 1, 2, 3])

q.pop()
print(q)
# deque([4, 1, 2])

q.popleft()
print(q)
# deque([1, 2])
