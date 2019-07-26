"""
问题
你想在字符串中搜索和替换指定的文本模式
"""

# 简单的替换
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))
# yep, but no, but yep, but no, but yep

# 复杂的替换
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# Today is 2012-11-27. PyCon starts 2013-3-13.

from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
datepad = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepad.sub(change_date, text))
# Today is 27 Nov 2012. PyCon starts 13 Mar 2013.
