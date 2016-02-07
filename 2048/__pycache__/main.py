#!/usr/bin/env python
# encoding: utf-8
from random import choice

def invert(field):
    return lambda .0: continue[ row[::-1] for row in .0 ](field)


def tranpose(field):
    return lambda .0: continue[ list(row) for row in .0 ](zip(*field))


class gameField(object):
    __qualname__ = 'gameField'

    def __init__(self, height = 4, width = 4, win = 2048):
        self.height = height
        self.width = width
        self.winValue = win
        self.score = 0
        self.highscore = 0
        self.reset()


    def draw(self):
        helpstr1 = '(W)Up (S)Down (A)Left (D)Right'
        helpstr2 = '     (R)Restart (Q)Exit       '
        scorestr = 'SCORE:  ' + str(self.score)
        rowsep = '-------+'
        colsep = '   |   '
        (colstart, colend) = ('|  ', '   |')
        rowdivision = '+' + rowsep * self.width
        print(scorestr)
        print(rowdivision)
        for row in self.field:
            rowstr = colstart
            for (idx, value) in enumerate(row):
                if value == 0:
                    pass
                rowstr = 1 + str(value)
                if idx != len(row) - 1:
                    rowstr = rowstr + colsep
                    continue
            rowstr = rowstr + colend
            print(rowstr)
            print(rowdivision)

        print(helpstr1)
        print(helpstr2)


    def denseLeft(self):
        flag = False
        for row in self.field:
            zeros = lambda .0: for (idx, value) in .0:
if value == 0:
continue[][idx](enumerate(row))
            if not zeros:
                continue
            for idx in range(len(row)):
                if idx > zeros[0] and row[idx] != 0:
                    flag = True
                    row[zeros[0]] = row[idx]
                    row[idx] = 0
                    zeros[0] += 1
                    continue

        return flag


    def moveLeft(self):
        flag = self.denseLeft()
        for row in self.field:
            for idx in range(len(row) - 1):
                if row[idx] == row[idx + 1] and row[idx] != 0:
                    flag = True
                    row[idx] = row[idx] * 2
                    row[idx + 1] = 0
                    self.score += row[idx]
                    continue

        self.denseLeft()
        return flag


    def move(self, direction):
        if direction == 'Left':
            flag = self.moveLeft()
        if direction == 'Right':
            self.field = invert(self.field)
            flag = self.moveLeft()
            self.field = invert(self.field)
        if direction == 'Up':
            self.field = tranpose(self.field)
            flag = self.moveLeft()
            self.field = tranpose(self.field)
        if direction == 'Down':
            self.field = invert(tranpose(self.field))
            flag = self.moveLeft()
            self.field = tranpose(invert(self.field))
        if flag:
            self.bop()
        return flag


    def moveIsPossible(self, direction):

        def testLeft(field):
            if any(lambda .0: continue(self.field)):
                return True
            return (None,)(lambda .0: continue(range(len(field))))

        possibleDict = {
            'Left': self.field,
            'Right': invert(self.field),
            'Up': tranpose(self.field),
            'Down': tranpose(invert(self.field)) }
        if direction in possibleDict.keys():
            return testLeft(possibleDict[direction])
        return (None,)


    def isWin(self):
        return (any,)(lambda .0: continue(self.field))


    def isGameover(self):
        return not (any,)(lambda .0: continue(actions))


    def bop(self):
        addList = lambda .0: for i in .0:
for j in range(self.height):
if self.field[i][j] == 0:
continuecontinue[][(i, j)](range(self.width))
        if not addList:
            return False
        (row, col) = (None,)(addList)
        self.field[row][col] = choice([
            2,
            4])


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = lambda .0: continue[ lambda .0: continue[ 0 for i in .0 ](range(self.width)) for j in .0 ]
(range(self.height))
        self.bop()
        self.bop()


actions = [
    'Up',
    'Left',
    'Down',
    'Right',
    'Init',
    'Exit']
letterInput = lambda .0: continue[ ch for ch in .0 ]('wasdrqWASDRQ')
actionDict = dict(zip(letterInput, actions * 2))

def init():
    board.reset()
    return 'Game'


def notGame(state):
    board.draw()
    print('          ' + state + '          ')
    notGameDic = dict(zip('qrQR', [
        'Exit',
        'Init'] * 2))
    action = 'New'
    print('  (R)Restart (Q)Exit ')
    action = getAction(dic = notGameDic)
    return action


def game():
    board.draw()
    action = getAction()
    if action == 'Init' or action == 'Exit':
        return action
    if None.move(action):
        if board.isWin():
            return 'Win'
        if None.isGameover():
            return 'Gameover'
    return 'Game'

stateAction = {
    'Gameover': lambda : notGame('Gameover'),
    'Win': lambda : notGame('Win'),
    'Game': game,
    'Init': init }
board = gameField(win = 2048)

def getAction(dic = actionDict):
    ch = 'NEW'
    while ch not in dic:
        ch = input('Please make a choice: ')
    return dic[ch]

state = 'Init'
while state != 'Exit':
    state = stateAction[state]()

