from collections import namedtuple, deque, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
haha = Point(1, 2)
print(haha.x, haha.y)
print(isinstance(haha, tuple))
Circle = namedtuple('Circle', ['x', 'y', 'r'])


q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('hahae')
print(q)

od = OrderedDict([('a', 1), ('c', 2), ('b', 32)])
print(od)

print(od)

c = Counter()
for ch in 'dddefasvcxvjzxlcvoiwloihvon;isdv.knbami;voer':
    c[ch] += 1
print(c)
