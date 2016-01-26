D = {'dsfsf':8383, '12idc': 392, '33211':'de'}
m = sorted(D.items(),reverse=True)
with open('writetest', 'w+') as f:
    f.write(str(m) + '\n')
    f.write("[2221, 'def', 33]")
    f.seek(0)
    L = f.readlines()
    for i, line in enumerate(L):
        if i == 1: L1 = eval(line.strip())
print(L1)
L = [1, 2, 3, 4, 5]
print(L)
X = 'spam'
Y = 'eggs'
X, Y = Y, X
print(X, Y)
S = ['s', 'p', 'a', 'm']
print(S[1][0][0][0][0])
