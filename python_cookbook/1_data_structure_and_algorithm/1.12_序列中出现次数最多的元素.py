"""
问题
怎样找出一个序列中出现次数最多的元素呢？
"""
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_count = Counter(words)
print(word_count)
top_three = word_count.most_common(3)
print(top_three)
# [('eyes', 8), ('the', 5), ('look', 4)]

morewords = ['why','are','you','not','looking','in','my','eyes']

word_count.update(morewords)
print(word_count)

# Counter对象可以实现运算操作
a = Counter(words)
b = Counter(morewords)
print(a+b)
print(a-b)