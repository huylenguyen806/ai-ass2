
import random
import time
import math
# ======================== Class Player =======================================
from copy import deepcopy


class Player:
    # student do not allow to change two first functions
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return self.str

    def CalculateDistances(self, row, col, state, playerPos, opponentPos,
                           noMoveLeftPL, noMoveLeftOP):
        Distances = [0.0, 0.0]
        for eachPL in range(4):
            if(noMoveLeftPL[eachPL]):
                continue
            Distances[0] += math.sqrt(math.pow(row-playerPos[eachPL]
                                               [0], 2) + math.pow(col-playerPos[eachPL][1], 2))
        for eachOP in range(4):
            if(noMoveLeftOP[eachOP]):
                continue
            Distances[1] += math.sqrt(math.pow(row-opponentPos[eachOP]
                                               [0], 2) + math.pow(col-opponentPos[eachOP][1], 2))
        return Distances

    def findTerritory(self, state, playerPos, opponentPos, noMoveLeftPL, noMoveLeftOP):
        numberOfTerritory = [0, 0]
        for row in range(10):
            for col in range(10):
                if(state[row][col] != '.'):
                    continue
                distances = self.CalculateDistances(
                    row, col, state, playerPos, opponentPos, noMoveLeftPL, noMoveLeftOP)
                if(distances[0] > distances[1]):
                    numberOfTerritory[1] += 1
                elif(distances[0] < distances[1]):
                    numberOfTerritory[0] += 1
        return numberOfTerritory

    def evaluate(self, state, playerPos, opponentPos, numberofX, noMoveLeftPL, noMoveLeftOP):
        playerLose = [False, False, False, False]
        opponentLose = [False, False, False, False]
        pl = 0
        op = 0
        numberofX[:] = [0]
        for row in range(10):
            for col in range(10):
                if(state[row][col] == '.'):
                    continue
                if(state[row][col] == 'X'):
                    numberofX[0] += 1
                    continue
                if(row > 0 and row < 9 and col > 0 and col < 9):  # from 1 - 8
                    if(state[row-1][col-1] != '.'
                            and state[row+1][col+1] != '.'
                            and state[row-1][col] != '.'
                            and state[row][col-1] != '.'
                            and state[row+1][col] != '.'
                            and state[row][col+1] != '.'
                            and state[row-1][col+1] != '.'
                            and state[row+1][col-1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row == 9 and col == 9):  # [9,9]
                    if(state[row-1][col] != '.' and state[row][col-1] != '.'
                            and state[row-1][col-1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row == 0 and col == 0):  # [0,0]
                    if(state[row+1][col] != '.' and state[row][col+1] != '.'
                            and state[row+1][col+1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row == 9 and col == 0):  # [9,0]
                    if(state[row-1][col] != '.' and state[row][col+1] != '.'
                            and state[row-1][col+1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row == 0 and col == 9):  # [0,9]
                    if(state[row][col-1] != '.' and state[row+1][col] != '.'
                            and state[row+1][col-1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row == 0 and col > 0 and col < 9):  # [0,x] with 0 < x < 9
                    if(state[row][col-1] != '.' and state[row][col+1] != '.'
                            and state[row+1][col] != '.' and state[row+1][col-1] != '.'
                            and state[row+1][col+1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row == 9 and col > 0 and col < 9):  # [9,x] with 0 < x < 9
                    if(state[row][col-1] != '.' and state[row][col+1] != '.'
                            and state[row-1][col] != '.' and state[row-1][col-1] != '.'
                            and state[row-1][col+1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(col == 0 and row > 0 and row < 9):  # [x,0] with 0 < x < 9
                    if(state[row-1][col] != '.' and state[row+1][col] != '.'
                            and state[row][col+1] != '.' and state[row+1][col+1] != '.'
                            and state[row-1][col+1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                # [x,9] with 0 < x < 9
                elif(col == 9 and row > 0 and row < 9):
                    if(state[row-1][col] != '.' and state[row+1][col] != '.'
                            and state[row-1][col-1] != '.' and state[row][col-1] != '.'
                            and state[row+1][col-1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                if(state[row][col] == self.str):
                    playerPos[pl] = [row, col]
                    pl += 1
                else:
                    opponentPos[op] = [row, col]
                    op += 1
        noMoveLeftPL[:] = playerLose
        noMoveLeftOP[:] = opponentLose
        num_territories = self.findTerritory(
            state, playerPos, opponentPos, noMoveLeftPL, noMoveLeftOP)
        plIsLost = False
        opIsLost = False
        if(all(item == True for item in playerLose)):
            plIsLost = True  # player loses the game
        elif(all(item == True for item in opponentLose)):
            opIsLost = True  # player wins the game
        if(plIsLost and not opIsLost):
            return -1000
        elif(not plIsLost and opIsLost):
            return 1000
        else:
            return num_territories[0] - num_territories[1]

    def doMoveForQueen(self, move, state, string):
        state[move[0][0]][move[0][1]] = '.'
        state[move[1][0]][move[1][1]] = string

    def undoMoveForQueen(self, move, state, string):
        state[move[1][0]][move[1][1]] = '.'
        state[move[0][0]][move[0][1]] = string

    def doFireArrow(self, move, state):
        state[move[2][0]][move[2][1]] = 'X'

    def undoFireArrow(self, move, state):
        state[move[2][0]][move[2][1]] = '.'

    def moveUp(self, move, step, state, isQueen):
        row = move[0][0] if isQueen else move[1][0]
        col = move[0][1] if isQueen else move[1][1]
        if(row - step >= 0):
            for rowi in range(row - 1, row - step - 1, -1):
                if(state[rowi][col] != '.'):
                    return False
            i = 1 if isQueen else 2
            move[i] = (row - step, col)
            return True
        else:
            return False

    def moveDown(self, move, step, state, isQueen):
        row = move[0][0] if isQueen else move[1][0]
        col = move[0][1] if isQueen else move[1][1]
        if(row + step <= 9):
            for rowi in range(row + 1, row + step + 1, 1):
                if(state[rowi][col] != '.'):
                    return False
            i = 1 if isQueen else 2
            move[i] = (row + step, col)
            return True
        else:
            return False

    def moveLeft(self, move, step, state, isQueen):
        row = move[0][0] if isQueen else move[1][0]
        col = move[0][1] if isQueen else move[1][1]
        if(col - step >= 0):
            for coli in range(col - 1, col - step - 1, -1):
                if(state[row][coli] != '.'):
                    return False
            i = 1 if isQueen else 2
            move[i] = (row, col - step)
            return True
        else:
            return False

    def moveRight(self, move, step, state, isQueen):
        row = move[0][0] if isQueen else move[1][0]
        col = move[0][1] if isQueen else move[1][1]
        if(col + step <= 9):
            for coli in range(col + 1, col + step + 1, 1):
                if(state[row][coli] != '.'):
                    return False
            i = 1 if isQueen else 2
            move[i] = (row, col + step)
            return True
        else:
            return False

    def moveUpLeft(self, move, step, state, isQueen):  # decrease both row, col
        row = move[0][0] if isQueen else move[1][0]
        col = move[0][1] if isQueen else move[1][1]
        if(col - step >= 0 and row - step >= 0):
            coli = col
            for rowi in range(row - 1, row - step - 1, -1):
                coli -= 1
                if(state[rowi][coli] != '.'):
                    return False
            i = 1 if isQueen else 2
            move[i] = (row - step, col - step)
            return True
        else:
            return False

    def moveDownRight(self, move, step, state, isQueen):  # increase both row, col
        row = move[0][0] if isQueen else move[1][0]
        col = move[0][1] if isQueen else move[1][1]
        if(col + step <= 9 and row + step <= 9):
            coli = col
            for rowi in range(row + 1, row + step + 1, 1):
                coli += 1
                if(state[rowi][coli] != '.'):
                    return False
            i = 1 if isQueen else 2
            move[i] = (row + step, col + step)
            return True
        else:
            return False

    def moveUpRight(self, move, step, state, isQueen):  # increase col, decrease row
        row = move[0][0] if isQueen else move[1][0]
        col = move[0][1] if isQueen else move[1][1]
        if(col + step <= 9 and row - step >= 0):
            coli = col
            for rowi in range(row - 1, row - step - 1, -1):
                coli += 1
                if(state[rowi][coli] != '.'):
                    return False
            i = 1 if isQueen else 2
            move[i] = (row - step, col + step)
            return True
        else:
            return False

    def moveDownLeft(self, move, step, state, isQueen):  # decrease col, increase row
        row = move[0][0] if isQueen else move[1][0]
        col = move[0][1] if isQueen else move[1][1]
        if(col - step >= 0 and row + step <= 9):
            coli = col
            for rowi in range(row + 1, row + step + 1, 1):
                coli -= 1
                if(state[rowi][coli] != '.'):
                    return False
            i = 1 if isQueen else 2
            move[i] = (row + step, col - step)
            return True
        else:
            return False

    def moves(self, move, step, state, isQueen, iterator):
        if(iterator == 0):
            return self.moveUp(move, step, state, isQueen)
        elif(iterator == 1):
            return self.moveDown(move, step, state, isQueen)
        elif(iterator == 2):
            return self.moveLeft(move, step, state, isQueen)
        elif(iterator == 3):
            return self.moveRight(move, step, state, isQueen)
        elif(iterator == 4):
            return self.moveUpLeft(move, step, state, isQueen)
        elif(iterator == 5):
            return self.moveDownRight(move, step, state, isQueen)
        elif(iterator == 6):
            return self.moveUpRight(move, step, state, isQueen)
        else:
            return self.moveDownLeft(move, step, state, isQueen)

    def alphabetaMinimax(self, state, depth, isMax, alphabeta):
        playerPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
        opponentPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
        noMoveLeftPL = [True, True, True, True]
        noMoveLeftOP = [True, True, True, True]
        numberofX = [0]
        score = self.evaluate(state, playerPos, opponentPos,
                              numberofX, noMoveLeftPL, noMoveLeftOP)
        best = None
        move = [(0, 0), (0, 0), (0, 0)]
        if(score == 1000 or score == -1000 or (depth >= 0 and numberofX[0] < 42) 
                or (depth >= 1 and numberofX[0] < 62) or depth >= 3):
            return score
        if(isMax):
            best = -99999
            for eachPlayer in range(4):
                if(noMoveLeftPL[eachPlayer]):
                    continue
                move[0] = (playerPos[eachPlayer][0], playerPos[eachPlayer][1])
                isMoveLeft = True
                stepMove = 0
                while(isMoveLeft):
                    stepMove += 1
                    tempMove = [False, False, False,
                                False, False, False, False, False]
                    for eachMove in range(8):
                        if(self.moves(move, stepMove, state, True, eachMove)):
                            self.doMoveForQueen(move, state, self.str)
                            tempMove[eachMove] = True
                            isArrowLeft = True
                            stepArrow = 0
                            while(isArrowLeft):
                                stepArrow += 1
                                tempArrow = [False, False, False,
                                             False, False, False, False, False]
                                for eachArrow in range(8):
                                    if(self.moves(move, stepArrow, state, False, eachArrow)):
                                        tempArrow[eachArrow] = True
                                        self.doFireArrow(move, state)
                                        best = max(best, self.alphabetaMinimax(state, depth + 1,
                                                                               not isMax, alphabeta))
                                        self.undoFireArrow(move, state)
                                        alphabeta[0] = max(best, alphabeta[0])
                                        if(alphabeta[1] <= alphabeta[0]):
                                            break
                                if(all(item2 == False for item2 in tempArrow)):
                                    isArrowLeft = False
                            self.undoMoveForQueen(move, state, self.str)
                    if(all(item1 == False for item1 in tempMove)):
                        isMoveLeft = False
        else:
            best = 99999
            opstr = 'w'
            if(self.str == 'w'):
                opstr = 'b'
            for eachOpponent in range(4):
                if(noMoveLeftOP[eachOpponent]):
                    continue
                move[0] = (opponentPos[eachOpponent][0],
                           opponentPos[eachOpponent][1])
                isMoveLeft = True
                stepMove = 0
                while(isMoveLeft):
                    stepMove += 1
                    tempMove = [False, False, False,
                                False, False, False, False, False]
                    for eachMove in range(8):
                        if(self.moves(move, stepMove, state, True, eachMove)):
                            self.doMoveForQueen(move, state, opstr)
                            tempMove[eachMove] = True
                            isArrowLeft = True
                            stepArrow = 0
                            while(isArrowLeft):
                                stepArrow += 1
                                tempArrow = [False, False, False,
                                             False, False, False, False, False]
                                for eachArrow in range(8):
                                    if(self.moves(move, stepArrow, state, False, eachArrow)):
                                        tempArrow[eachArrow] = True
                                        self.doFireArrow(move, state)
                                        best = min(best, self.alphabetaMinimax(state, depth + 1,
                                                                               not isMax, alphabeta))
                                        self.undoFireArrow(move, state)
                                        alphabeta[1] = min(best, alphabeta[1])
                                        if(alphabeta[1] <= alphabeta[0]):
                                            break
                                if(all(item2 == False for item2 in tempArrow)):
                                    isArrowLeft = False
                            self.undoMoveForQueen(move, state, opstr)
                    if(all(item1 == False for item1 in tempMove)):
                        isMoveLeft = False
        return best

    def findBestMove(self, state):
        playerPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
        opponentPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
        noMoveLeftPL = [True, True, True, True]
        noMoveLeftOP = [True, True, True, True]
        numberofX = [0]
        self.evaluate(state, playerPos, opponentPos,
                      numberofX, noMoveLeftPL, noMoveLeftOP)
        bestMove = None
        if(all(item == True for item in noMoveLeftPL)):
            return bestMove
        if(numberofX[0] < 10):
            # move randomly
            i = random.randint(0, 3)
            while(noMoveLeftPL[i]):
                i = random.randint(0, 3)
            row = playerPos[i][0]
            col = playerPos[i][1]
            randmove = random.randint(0, 7)
            randstep = random.randint(1, 9)
            randfire = random.randint(0, 7)
            randstepfire = random.randint(1, 9)
            move = [(row, col), (0, 0), (0, 0)]
            while(not self.moves(move, randstep, state, True, randmove)):
                randmove = random.randint(0, 7)
                randstep = random.randint(1, 9)
            self.doMoveForQueen(move, state, self.str)
            while(not self.moves(move, randstepfire, state, False, randfire)):
                randfire = random.randint(0, 7)
                randstepfire = random.randint(1, 9)
            self.undoMoveForQueen(move, state, self.str)
            bestMove = deepcopy(move)
        else:
            bestVal = -9999999999999999999999
            move = [(0, 0), (0, 0), (0, 0)]
            for eachPlayer in range(4):
                if(noMoveLeftPL[eachPlayer]):
                    continue
                move[0] = (playerPos[eachPlayer][0],
                            playerPos[eachPlayer][1])
                isMoveLeft = True
                stepMove = 0
                while(isMoveLeft):
                    stepMove += 1
                    tempMove = [False, False, False,
                                False, False, False, False, False]
                    for eachMove in range(8):
                        if(self.moves(move, stepMove, state, True, eachMove)):
                            self.doMoveForQueen(move, state, self.str)
                            tempMove[eachMove] = True
                            isArrowLeft = True
                            stepArrow = 0
                            while(isArrowLeft):
                                stepArrow += 1
                                tempArrow = [False, False, False,
                                                False, False, False, False, False]
                                for eachArrow in range(8):
                                    if(self.moves(move, stepArrow, state, False, eachArrow)):
                                        tempArrow[eachArrow] = True
                                        self.doFireArrow(move, state)
                                        best = self.alphabetaMinimax(state, 0,
                                                                        False, [-99999, 99999])
                                        self.undoFireArrow(move, state)
                                        if(best > bestVal):
                                            bestVal = best
                                            bestMove = deepcopy(move)
                                if(all(item2 == False for item2 in tempArrow)):
                                    isArrowLeft = False
                            self.undoMoveForQueen(move, state, self.str)
                    if(all(item1 == False for item1 in tempMove)):
                        isMoveLeft = False
        return bestMove

    def nextMove(self, state):
        # result = [(0,3),(5,3),(8,6)] # example move in wikipedia
        return self.findBestMove(state)
