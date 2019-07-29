"""
问题
你正在处理Unicode字符串，需要确保所有字符串在底层有相同的表示。
"""

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1, s2)
# Spicy Jalapeño Spicy Jalapeño

print(s1==s2)
# False

print(len(s1), len(s2))
# 14 15

# 标准化
import unicodedata
t1 = unicodedata.normalize("NFC", s1)
t2 = unicodedata.normalize("NFC", s2)
print(t1 == t2)
# True

t1 = unicodedata.normalize("NFD", s1)
t2 = unicodedata.normalize("NFD", s2)
print(t1 == t2)
# True