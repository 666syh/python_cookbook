"""
问题
你想匹配或者搜索特定模式的文本
"""

# 简单的匹配和搜索
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.startswith('yeah'))
# True

print(text.endswith('no'))
# False

print(text.find('no'))
# 10

# 复杂的匹配和搜索
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
print(True if re.match(r"\d+/\d+/\d+", text1) else False)
# True

print(True if re.match(r"\d+/\d+/\d+", text2) else False)
# False

datepat = re.compile(r"\d+/\d+/\d+")
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))
# ['11/27/2012', '3/13/2013']

datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
m = datepat.match('11/27/2012')
print(m.group(1))
print(m.group(2))
print(m.group(3))
# 11
# 27
# 2012

print(datepat.findall(text))
[('11', '27', '2012'), ('3', '13', '2013')]