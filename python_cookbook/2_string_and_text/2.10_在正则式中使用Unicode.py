"""
问题
你正在使用正则表达式处理文本，但是关注的是Unicode字符处理。
"""

import re
num = re.compile(r'\d+')
print(num.match('123'))
# <_sre.SRE_Match object; span=(0, 3), match='123'>

print(num.match('\u0661\u0662\u0663'))
# <_sre.SRE_Match object; span=(0, 3), match='١٢٣'>

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'

print(pat.match(s))
# <_sre.SRE_Match object; span=(0, 6), match='straße'>

print(pat.match(s.upper()))
# None