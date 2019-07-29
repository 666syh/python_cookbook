"""
问题
你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。
"""

import re
comment = re.compile('/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '/* this is \
        multiline comment */'
print(comment.findall(text1))
# [' this is a comment ']
print(comment.findall(text2))
# [' this is         multiline comment ']

comment2 = re.compile('/\*(.*?|\n)\*/')
print(comment2.findall(text2))