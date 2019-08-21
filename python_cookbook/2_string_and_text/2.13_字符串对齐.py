"""
问题
你想通过某种对齐方式来格式化字符串
"""
text = "hello World"
print('\'', text.ljust(20), '\'')
# ' hello World          '

print('\'', text.rjust(20), '\'')
# '          hello World '

print('\'', text.center(20), '\'')
# '     hello World      '

print('\'', text.center(20, '='), '\'')
# ' ====hello World===== '

print('\'', format(text, '>20'),'\'')
# '          hello World '

print('\'', format(text, '<20'),'\'')
# ' hello World          '

print('\'', format(text, '^20'),'\'')
# '     hello World      '

print('\'', format(text, '=^20'),'\'')
# ' ====hello World===== '

print('\'', '{:>10s} {:>10s}'.format('Hello', 'World'), '\'')
# '      Hello      World '