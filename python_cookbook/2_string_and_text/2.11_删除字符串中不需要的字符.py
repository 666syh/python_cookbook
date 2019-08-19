"""
问题
你想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白。
"""

s = " hello world\n"
print(s.strip())
# 'hello world'

print(s.lstrip())
# 'hello world\n'

print(s.rstrip())
# ' hello world'


t = t = '-----hello====='
print(t.lstrip('-'))
# 'hello====='

print(t.strip('-='))
# 'hello'

print(s.replace(' ', ''))
# 'helloworld'