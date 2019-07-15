"""
问题
你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
"""

from collections import OrderedDict

#与被插入的顺序相同
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for k in d:
    print(k, d[k])
# foo 1
# bar 2
# spam 3
# grok 4

import json
print(json.dumps(d))
# {"foo": 1, "bar": 2, "spam": 3, "grok": 4}

# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。
# 所以 OrderedDict 的大小是一个普通字典的两倍