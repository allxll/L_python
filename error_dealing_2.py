import logging


def bar():
    try:
        fooa('0')
    except ValueError as e:
        print('valueError!::~~~~~~~~')
        raise

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

class FooError(ValueError):
    pass

def fooa(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10/n
bar()
