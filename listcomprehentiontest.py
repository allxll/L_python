a = [y for x in ['abcde', 'fghij'] for y in x]
print(a)
import time
reps = 1000
resplist = range(reps)
def timer(func, *pargs, **kargs):
    start = time.time()
    for i in resplist:
        ret = func(*pargs, **kargs)
    elapsed = time.time() - start
    return (elapsed, ret)
print(timer(map, sorted, [-1, -2, -3, -4]))
