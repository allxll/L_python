def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))

def myzip(*args):
    iters = list(map(iter, args))
    while any(iters):
        res = [next(i) for i in iters]
        yield tuple(res)



if __name__ == '__main__':
    for i in myzip([x**2 for x in range(8)], range(10)):
        print(i)
