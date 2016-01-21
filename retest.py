import re
code ='''hadkfalifexxI
xxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'''
L = re.findall('xx(.*?)xx', code, re.S)
print(L)
output = re.sub('xx(.*?)xx', ']]', code)
print(output)
