def checkIndex(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithmeticSequence(object):
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)
        try: return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value

class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)

class testing(object):

    @staticmethod
    def happy():
        print('yes')

    @classmethod
    def no(cls):
        print(cls)

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        print('I dont inform you')

def flatten(nested):
    try:
        try: nested + ''
        except: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

def repeater(value):
    while True:
        nie = (yield value)
        if nie is not None: value = nie

if __name__ == '__main__':
    print(list(flatten([[1,2], [], [2,3, [4,2,[1112,3],12]]])))
    r = repeater(32)
    print(r.__next__())
    print(r.send('hae'))
