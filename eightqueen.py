def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

state = []
LIFO = []
i = 0
minusflag = False
while True:
    if len(state) == 8:
        break
    if not minusflag:
        LIFO.append([row for row in range(8) if not conflict(state, row)])
    else:
        minusflag = False
        LIFO[i] = [row for row in range(8) if not conflict(state, row)]
    print(LIFO)
    print(state)
    if LIFO[i]:
        try:
            m = LIFO[i].pop()
            state[i] = m
        except IndexError:
            state.append(m)
        i += 1
    else:
        i -= 1
        minusflag = True

print(state)
