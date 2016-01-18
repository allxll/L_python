import logging
logging.basicConfig(level=logging.INFO)
import pdb

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n
print(foo('0'))
