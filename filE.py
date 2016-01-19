with open('mass', 'rb') as f:
    for line in f.readlines():
        print(line)

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
print(f)

f1 = StringIO('Hello!\nHI!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO
m = BytesIO()
m.write('中文'.encode('utf-8'))
print(m.getvalue())
