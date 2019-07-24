"""
问题
你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
"""

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
# [{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
#  {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#  {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#  {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)
# [{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#  {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#  {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#  {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]

# 多个key
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)
# [{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#  {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#  {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
#  {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}]

# lambda
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))