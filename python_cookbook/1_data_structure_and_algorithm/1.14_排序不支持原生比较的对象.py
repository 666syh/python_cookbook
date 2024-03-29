"""
问题
你想排序类型相同的对象，但是他们不支持原生的比较操作。
"""

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))
# [User(23), User(3), User(99)]
# [User(3), User(23), User(99)]

from operator import attrgetter
print(sorted(users, key=attrgetter("user_id")))
# [User(3), User(23), User(99)]