"""
问题
一些无聊的幼稚黑客在你的网站页面表单中输入文本”pýtĥöñ”，然后你想将这些字符清理掉。
"""

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap = {
    ord('\t'):'',
    ord('\f'):'',
    ord('\r'):None
}
a = s.translate(remap)
print(a)
# pýtĥöñisawesome

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
# pýtĥöñisawesome

print(b.translate(cmb_chrs))
# pythonisawesome

print(b.encode('ascii', 'ignore').decode('ascii'))
# pythonisawesome