"""
问题
你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹配。 而你想修改它变成查找最短的可能匹配。
"""

import re
# 正常情况--贪婪模式
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'

print(str_pat.findall(text1))
# ['no.']

text2 = 'Computer says "no." Phone says "yes."'

print(str_pat.findall(text2))
# ['no." Phone says "yes.']

# 最短匹配--非贪婪模式
str_pat2 = re.compile(r'\"(.*?)\"')
print(str_pat2.findall(text2))
# ['no.', 'yes.']