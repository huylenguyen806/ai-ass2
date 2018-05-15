

# ======================== Class Player =======================================


class Player:
    # student do not allow to change two first functions
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return self.str

    def evaluate(self, state, playerPos, opponentPos):
        playerLose = [False, False, False, False]
        opponentLose = [False, False, False, False]
        pl = 0
        op = 0
        for row in range(10):
            for col in range(10):
                if(state[row][col] == '.'):
                    continue
                if(state[row][col] == self.str):
                    playerPos[pl] = [row, col]
                if(state[row][col] != self.str):
                    opponentPos[op] = [row, col]
                if(row > 0 and row < 9 and col > 0 and col < 9):  # from 1 - 8
                    if(state[row-1][col-1] == 'X'
                            and state[row+1][col+1] == 'X'
                            and state[row-1][col] == 'X'
                            and state[row][col-1] == 'X'
                            and state[row+1][col] == 'X'
                            and state[row][col+1] == 'X'
                            and state[row-1][col+1] == 'X'
                            and state[row+1][col-1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        elif(state[row][col] != 'X'):
                            opponentLose[op] = True
                            op += 1
                elif(row > 0 and col > 0):  # [9,9]
                    if(state[row-1][col] == 'X' and state[row][col-1] == 'X'
                            and state[row-1][col-1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        elif(state[row][col] != 'X'):
                            opponentLose[op] = True
                            op += 1
                elif(row < 9 and col < 9):  # [0,0]
                    if(state[row+1][col] == 'X' and state[row][col+1] == 'X'
                            and state[row+1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        elif(state[row][col] != 'X'):
                            opponentLose[op] = True
                            op += 1
                elif(row > 0 and col < 9):  # [9,0]
                    if(state[row-1][col] == 'X' and state[row][col+1] == 'X'
                            and state[row-1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        elif(state[row][col] != 'X'):
                            opponentLose[op] = True
                            op += 1
                elif(row < 9 and col > 0):  # [0,9]
                    if(state[row][col-1] == 'X' and state[row+1][col] == 'X'
                            and state[row+1][col-1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        elif(state[row][col] != 'X'):
                            opponentLose[op] = True
                            op += 1
                elif(row < 9):  # [0,x] with 0 < x < 9
                    if(state[row][col-1] == 'X' and state[row][col+1] == 'X'
                            and state[row+1][col] == 'X' and state[row+1][col-1] == 'X'
                            and state[row+1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        elif(state[row][col] != 'X'):
                            opponentLose[op] = True
                            op += 1
                elif(row > 0):  # [9,x] with 0 < x < 9
                    if(state[row][col-1] == 'X' and state[row][col+1] == 'X'
                            and state[row-1][col] == 'X' and state[row-1][col-1] == 'X'
                            and state[row-1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        elif(state[row][col] != 'X'):
                            opponentLose[op] = True
                            op += 1
                elif(col < 9):  # [x,0] with 0 < x < 9
                    if(state[row-1][col] == 'X' and state[row+1][col] == 'X'
                            and state[row][col+1] == 'X' and state[row+1][col+1] == 'X'
                            and state[row-1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        elif(state[row][col] != 'X'):
                            opponentLose[op] = True
                            op += 1
                else:   # [x,9] with 0 < x < 9
                    if(state[row-1][col] == 'X' and state[row+1][col] == 'X'
                            and state[row-1][col-1] == 'X' and state[row][col-1] == 'X'
                            and state[row+1][col-1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        elif(state[row][col] != 'X'):
                            opponentLose[op] = True
                            op += 1

        if(all(item == True for item in playerLose)):
            return -1  # player loses the game
        elif(all(item == True for item in opponentLose)):
            return 1  # player wins the game
        else:
            return 0  # neither win nor lose

    def doMove(self, move, state):
        state[move[0][0]][move[0][1]] = '.'
        state[move[1][0]][move[1][1]] = self.str
        state[move[2][0]][move[2][1]] = 'X'

    def undoMove(self, move, state):
        state[move[0][0]][move[0][1]] = self.str
        state[move[1][0]][move[1][1]] = '.'
        state[move[2][0]][move[2][1]] = '.'

    def minimax(self, state, depth, isMax):
        playerPos = [(0, 0), (0, 0), (0, 0), (0, 0)]
        opponentPos = [(0, 0), (0, 0), (0, 0), (0, 0)]
        score = self.evaluate(state, playerPos, opponentPos)

        if(score != 0):
            return score

        move = [(0, 0), (0, 0), (0, 0)]

        if(isMax):
            best = -9999
            # make a move for max
            for eachQueen in range(4):
                # [row_motmove,col_notmove]
                move[0] = playerPos[eachQueen]
                for eachQueenMove in range(4):
                    if(eachQueenMove == 0):  # Move horizontal
                        for col in range(10):
                            row = move[0][0]
                            if(state[row][col] == '.'):  # empty slot, it means can move
                                # save the moved slot: [row_move,col_move]
                                move[1] = [row, col]
                                for eachArrowDirection in range(4):
                                    if(eachArrowDirection == 0):  # horizontal direction: --
                                        for aCol in range(10):
                                            aRow = move[1][0]
                                            if(state[aRow][aCol] == '.' or
                                                    (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 1):  # vertical direction: |
                                        for aRow in range(10):
                                            aCol = move[1][1]
                                            if(state[aRow][aCol] == '.'):
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                        b = row - col  # y = x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 0):  # y go to 0 faster than x
                                            rangex0 = -b
                                            rangex1 = 9  # x go to 9 faster than y
                                        else:  # x go to 0 faster than y
                                            rangex0 = 0
                                            rangex1 = 9 - b  # y go to 9 faster than x
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    else:  # diagonal2 direction: \
                                        b = row + col  # y = -x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 10):  # rangex from 0 to where y=0
                                            rangex0 = 0
                                            rangex1 = b
                                        else:  # rangex from where y=9 to 9
                                            rangex0 = b - 9
                                            rangex1 = 9
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = -x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                    elif(eachQueenMove == 1):  # move vertical
                        for row in range(10):
                            col = move[0][1]
                            if(state[row][col] == '.'):
                                move[1] = [row, col]
                                for eachArrowDirection in range(4):
                                    if(eachArrowDirection == 0):  # horizontal direction: --
                                        for aCol in range(10):
                                            aRow = move[1][0]
                                            if(state[aRow][aCol] == '.' or
                                                    (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 1):  # vertical direction: |
                                        for aRow in range(10):
                                            aCol = move[1][1]
                                            if(state[aRow][aCol] == '.'):
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                        b = row - col  # y = x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 0):  # y go to 0 faster than x
                                            rangex0 = -b
                                            rangex1 = 9  # x go to 9 faster than y
                                        else:  # x go to 0 faster than y
                                            rangex0 = 0
                                            rangex1 = 9 - b  # y go to 9 faster than x
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    else:  # diagonal2 direction: \
                                        b = row + col  # y = -x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 10):  # rangex from 0 to where y=0
                                            rangex0 = 0
                                            rangex1 = b
                                        else:  # rangex from where y=9 to 9
                                            rangex0 = b - 9
                                            rangex1 = 9
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = -x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                    elif(eachQueenMove == 2):  # move diagonal1: /
                        # y_queen = x_queen + b_queen
                        b_queen = move[0][0] - move[0][1]
                        rangexq0 = None
                        rangexq1 = None
                        if(b_queen < 0):
                            rangexq0 = -b_queen
                            rangexq1 = 9
                        else:
                            rangexq0 = 0
                            rangexq1 = 9 - b_queen
                        for x_queen in range(rangexq0, rangexq1+1, 1):
                            y_queen = x_queen + b_queen
                            if(state[y_queen][x_queen] == '.'):
                                move[1] = [y_queen, x_queen]
                                row = y_queen
                                col = x_queen
                                for eachArrowDirection in range(4):
                                    if(eachArrowDirection == 0):  # horizontal direction: --
                                        for aCol in range(10):
                                            aRow = move[1][0]
                                            if(state[aRow][aCol] == '.' or
                                                    (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 1):  # vertical direction: |
                                        for aRow in range(10):
                                            aCol = move[1][1]
                                            if(state[aRow][aCol] == '.'):
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                        b = row - col  # y = x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 0):  # y go to 0 faster than x
                                            rangex0 = -b
                                            rangex1 = 9  # x go to 9 faster than y
                                        else:  # x go to 0 faster than y
                                            rangex0 = 0
                                            rangex1 = 9 - b  # y go to 9 faster than x
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    else:  # diagonal2 direction: \
                                        b = row + col  # y = -x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 10):  # rangex from 0 to where y=0
                                            rangex0 = 0
                                            rangex1 = b
                                        else:  # rangex from where y=9 to 9
                                            rangex0 = b - 9
                                            rangex1 = 9
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = -x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                    else:  # move diagonal2: \
                        b_queen = move[0][0] + \
                            move[0][1]  # y_queen = x_queen + b_queen
                        rangexq0 = None
                        rangexq1 = None
                        if(b_queen < 10):
                            rangexq0 = 0
                            rangexq1 = b_queen
                        else:
                            rangexq0 = b_queen - 9
                            rangexq1 = 9
                        for x_queen in range(rangexq0, rangexq1+1, 1):
                            y_queen = -x_queen + b_queen
                            if(state[y_queen][x_queen] == '.'):
                                move[1] = [y_queen, x_queen]
                                row = y_queen
                                col = x_queen
                                for eachArrowDirection in range(4):
                                    if(eachArrowDirection == 0):  # horizontal direction: --
                                        for aCol in range(10):
                                            aRow = move[1][0]
                                            if(state[aRow][aCol] == '.' or
                                                    (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 1):  # vertical direction: |
                                        for aRow in range(10):
                                            aCol = move[1][1]
                                            if(state[aRow][aCol] == '.'):
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                        b = row - col  # y = x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 0):  # y go to 0 faster than x
                                            rangex0 = -b
                                            rangex1 = 9  # x go to 9 faster than y
                                        else:  # x go to 0 faster than y
                                            rangex0 = 0
                                            rangex1 = 9 - b  # y go to 9 faster than x
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    else:  # diagonal2 direction: \
                                        b = row + col  # y = -x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 10):  # rangex from 0 to where y=0
                                            rangex0 = 0
                                            rangex1 = b
                                        else:  # rangex from where y=9 to 9
                                            rangex0 = b - 9
                                            rangex1 = 9
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = -x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
            return best
        else:
            best = 9999
            # make a move for min
            for eachQueen in range(4):
                # [row_motmove,col_notmove]
                move[0] = opponentPos[eachQueen]
                for eachQueenMove in range(4):
                    if(eachQueenMove == 0):  # Move horizontal
                        for col in range(10):
                            row = move[0][0]
                            if(state[row][col] == '.'):  # empty slot, it means can move
                                # save the moved slot: [row_move,col_move]
                                move[1] = [row, col]
                                for eachArrowDirection in range(4):
                                    if(eachArrowDirection == 0):  # horizontal direction: --
                                        for aCol in range(10):
                                            aRow = move[1][0]
                                            if(state[aRow][aCol] == '.' or
                                                    (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 1):  # vertical direction: |
                                        for aRow in range(10):
                                            aCol = move[1][1]
                                            if(state[aRow][aCol] == '.'):
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                        b = row - col  # y = x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 0):  # y go to 0 faster than x
                                            rangex0 = -b
                                            rangex1 = 9  # x go to 9 faster than y
                                        else:  # x go to 0 faster than y
                                            rangex0 = 0
                                            rangex1 = 9 - b  # y go to 9 faster than x
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    else:  # diagonal2 direction: \
                                        b = row + col  # y = -x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 10):  # rangex from 0 to where y=0
                                            rangex0 = 0
                                            rangex1 = b
                                        else:  # rangex from where y=9 to 9
                                            rangex0 = b - 9
                                            rangex1 = 9
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = -x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                    elif(eachQueenMove == 1):  # move vertical
                        for row in range(10):
                            col = move[0][1]
                            if(state[row][col] == '.'):
                                move[1] = [row, col]
                                for eachArrowDirection in range(4):
                                    if(eachArrowDirection == 0):  # horizontal direction: --
                                        for aCol in range(10):
                                            aRow = move[1][0]
                                            if(state[aRow][aCol] == '.' or
                                                    (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 1):  # vertical direction: |
                                        for aRow in range(10):
                                            aCol = move[1][1]
                                            if(state[aRow][aCol] == '.'):
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                        b = row - col  # y = x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 0):  # y go to 0 faster than x
                                            rangex0 = -b
                                            rangex1 = 9  # x go to 9 faster than y
                                        else:  # x go to 0 faster than y
                                            rangex0 = 0
                                            rangex1 = 9 - b  # y go to 9 faster than x
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    else:  # diagonal2 direction: \
                                        b = row + col  # y = -x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 10):  # rangex from 0 to where y=0
                                            rangex0 = 0
                                            rangex1 = b
                                        else:  # rangex from where y=9 to 9
                                            rangex0 = b - 9
                                            rangex1 = 9
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = -x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                    elif(eachQueenMove == 2):  # move diagonal1: /
                        # y_queen = x_queen + b_queen
                        b_queen = move[0][0] - move[0][1]
                        rangexq0 = None
                        rangexq1 = None
                        if(b_queen < 0):
                            rangexq0 = -b_queen
                            rangexq1 = 9
                        else:
                            rangexq0 = 0
                            rangexq1 = 9 - b_queen
                        for x_queen in range(rangexq0, rangexq1+1, 1):
                            y_queen = x_queen + b_queen
                            if(state[y_queen][x_queen] == '.'):
                                move[1] = [y_queen, x_queen]
                                row = y_queen
                                col = x_queen
                                for eachArrowDirection in range(4):
                                    if(eachArrowDirection == 0):  # horizontal direction: --
                                        for aCol in range(10):
                                            aRow = move[1][0]
                                            if(state[aRow][aCol] == '.' or
                                                    (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 1):  # vertical direction: |
                                        for aRow in range(10):
                                            aCol = move[1][1]
                                            if(state[aRow][aCol] == '.'):
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                        b = row - col  # y = x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 0):  # y go to 0 faster than x
                                            rangex0 = -b
                                            rangex1 = 9  # x go to 9 faster than y
                                        else:  # x go to 0 faster than y
                                            rangex0 = 0
                                            rangex1 = 9 - b  # y go to 9 faster than x
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    else:  # diagonal2 direction: \
                                        b = row + col  # y = -x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 10):  # rangex from 0 to where y=0
                                            rangex0 = 0
                                            rangex1 = b
                                        else:  # rangex from where y=9 to 9
                                            rangex0 = b - 9
                                            rangex1 = 9
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = -x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                    else:  # move diagonal2: \
                        b_queen = move[0][0] + \
                            move[0][1]  # y_queen = x_queen + b_queen
                        rangexq0 = None
                        rangexq1 = None
                        if(b_queen < 10):
                            rangexq0 = 0
                            rangexq1 = b_queen
                        else:
                            rangexq0 = b_queen - 9
                            rangexq1 = 9
                        for x_queen in range(rangexq0, rangexq1+1, 1):
                            y_queen = -x_queen + b_queen
                            if(state[y_queen][x_queen] == '.'):
                                move[1] = [y_queen, x_queen]
                                row = y_queen
                                col = x_queen
                                for eachArrowDirection in range(4):
                                    if(eachArrowDirection == 0):  # horizontal direction: --
                                        for aCol in range(10):
                                            aRow = move[1][0]
                                            if(state[aRow][aCol] == '.' or
                                                    (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 1):  # vertical direction: |
                                        for aRow in range(10):
                                            aCol = move[1][1]
                                            if(state[aRow][aCol] == '.'):
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                        b = row - col  # y = x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 0):  # y go to 0 faster than x
                                            rangex0 = -b
                                            rangex1 = 9  # x go to 9 faster than y
                                        else:  # x go to 0 faster than y
                                            rangex0 = 0
                                            rangex1 = 9 - b  # y go to 9 faster than x
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
                                    else:  # diagonal2 direction: \
                                        b = row + col  # y = -x + b
                                        rangex0 = None
                                        rangex1 = None
                                        if(b < 10):  # rangex from 0 to where y=0
                                            rangex0 = 0
                                            rangex1 = b
                                        else:  # rangex from where y=9 to 9
                                            rangex0 = b - 9
                                            rangex1 = 9
                                        for x in range(rangex0, rangex1+1, 1):  # for each col
                                            y = -x + b  # find each col's row
                                            if(state[y][x] == '.'):
                                                move[2] = [y, x]
                                                self.doMove(move, state)
                                                best = min(best, self.minimax(
                                                    state, depth+1, not isMax))
                                                self.undoMove(move, state)
            return best

    def findBestMove(self, state):
        playerPos = [(0, 0), (0, 0), (0, 0), (0, 0)]
        opponentPos = [(0, 0), (0, 0), (0, 0), (0, 0)]
        self.evaluate(state, playerPos, opponentPos)
        bestVal = -99999999999999999
        move = [(0, 0), (0, 0), (0, 0), (0, 0)]
        bestMove = None
        for eachQueen in range(4):
            move[0] = playerPos[eachQueen]  # [row_motmove,col_notmove]
            for eachQueenMove in range(4):
                if(eachQueenMove == 0):  # Move horizontal
                    for col in range(10):
                        row = move[0][0]
                        if(state[row][col] == '.'):  # empty slot, it means can move
                            # save the moved slot: [row_move,col_move]
                            move[1] = [row, col]
                            for eachArrowDirection in range(4):
                                if(eachArrowDirection == 0):  # horizontal direction: --
                                    for aCol in range(10):
                                        aRow = move[1][0]
                                        if(state[aRow][aCol] == '.' or
                                                (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                            move[2] = [aRow, aCol]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                elif(eachArrowDirection == 1):  # vertical direction: |
                                    for aRow in range(10):
                                        aCol = move[1][1]
                                        if(state[aRow][aCol] == '.'):
                                            move[2] = [aRow, aCol]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                    b = row - col  # y = x + b
                                    rangex0 = None
                                    rangex1 = None
                                    if(b < 0):  # y go to 0 faster than x
                                        rangex0 = -b
                                        rangex1 = 9  # x go to 9 faster than y
                                    else:  # x go to 0 faster than y
                                        rangex0 = 0
                                        rangex1 = 9 - b  # y go to 9 faster than x
                                    for x in range(rangex0, rangex1+1, 1):  # for each col
                                        y = x + b  # find each col's row
                                        if(state[y][x] == '.'):
                                            move[2] = [y, x]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                else:  # diagonal2 direction: \
                                    b = row + col  # y = -x + b
                                    rangex0 = None
                                    rangex1 = None
                                    if(b < 10):  # rangex from 0 to where y=0
                                        rangex0 = 0
                                        rangex1 = b
                                    else:  # rangex from where y=9 to 9
                                        rangex0 = b - 9
                                        rangex1 = 9
                                    for x in range(rangex0, rangex1+1, 1):  # for each col
                                        y = -x + b  # find each col's row
                                        if(state[y][x] == '.'):
                                            move[2] = [y, x]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                elif(eachQueenMove == 1):  # move vertical
                    for row in range(10):
                        col = move[0][1]
                        if(state[row][col] == '.'):
                            move[1] = [row, col]
                            for eachArrowDirection in range(4):
                                if(eachArrowDirection == 0):  # horizontal direction: --
                                    for aCol in range(10):
                                        aRow = move[1][0]
                                        if(state[aRow][aCol] == '.' or
                                                (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                            move[2] = [aRow, aCol]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                elif(eachArrowDirection == 1):  # vertical direction: |
                                    for aRow in range(10):
                                        aCol = move[1][1]
                                        if(state[aRow][aCol] == '.'):
                                            move[2] = [aRow, aCol]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                    b = row - col  # y = x + b
                                    rangex0 = None
                                    rangex1 = None
                                    if(b < 0):  # y go to 0 faster than x
                                        rangex0 = -b
                                        rangex1 = 9  # x go to 9 faster than y
                                    else:  # x go to 0 faster than y
                                        rangex0 = 0
                                        rangex1 = 9 - b  # y go to 9 faster than x
                                    for x in range(rangex0, rangex1+1, 1):  # for each col
                                        y = x + b  # find each col's row
                                        if(state[y][x] == '.'):
                                            move[2] = [y, x]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                else:  # diagonal2 direction: \
                                    b = row + col  # y = -x + b
                                    rangex0 = None
                                    rangex1 = None
                                    if(b < 10):  # rangex from 0 to where y=0
                                        rangex0 = 0
                                        rangex1 = b
                                    else:  # rangex from where y=9 to 9
                                        rangex0 = b - 9
                                        rangex1 = 9
                                    for x in range(rangex0, rangex1+1, 1):  # for each col
                                        y = -x + b  # find each col's row
                                        if(state[y][x] == '.'):
                                            move[2] = [y, x]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                elif(eachQueenMove == 2):  # move diagonal1: /
                    # y_queen = x_queen + b_queen
                    b_queen = move[0][0] - move[0][1]
                    rangexq0 = None
                    rangexq1 = None
                    if(b_queen < 0):
                        rangexq0 = -b_queen
                        rangexq1 = 9
                    else:
                        rangexq0 = 0
                        rangexq1 = 9 - b_queen
                    for x_queen in range(rangexq0, rangexq1+1, 1):
                        y_queen = x_queen + b_queen
                        if(state[y_queen][x_queen] == '.'):
                            move[1] = [y_queen, x_queen]
                            row = y_queen
                            col = x_queen
                            for eachArrowDirection in range(4):
                                if(eachArrowDirection == 0):  # horizontal direction: --
                                    for aCol in range(10):
                                        aRow = move[1][0]
                                        if(state[aRow][aCol] == '.' or
                                                (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                            move[2] = [aRow, aCol]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                elif(eachArrowDirection == 1):  # vertical direction: |
                                    for aRow in range(10):
                                        aCol = move[1][1]
                                        if(state[aRow][aCol] == '.'):
                                            move[2] = [aRow, aCol]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                    b = row - col  # y = x + b
                                    rangex0 = None
                                    rangex1 = None
                                    if(b < 0):  # y go to 0 faster than x
                                        rangex0 = -b
                                        rangex1 = 9  # x go to 9 faster than y
                                    else:  # x go to 0 faster than y
                                        rangex0 = 0
                                        rangex1 = 9 - b  # y go to 9 faster than x
                                    for x in range(rangex0, rangex1+1, 1):  # for each col
                                        y = x + b  # find each col's row
                                        if(state[y][x] == '.'):
                                            move[2] = [y, x]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                else:  # diagonal2 direction: \
                                    b = row + col  # y = -x + b
                                    rangex0 = None
                                    rangex1 = None
                                    if(b < 10):  # rangex from 0 to where y=0
                                        rangex0 = 0
                                        rangex1 = b
                                    else:  # rangex from where y=9 to 9
                                        rangex0 = b - 9
                                        rangex1 = 9
                                    for x in range(rangex0, rangex1+1, 1):  # for each col
                                        y = -x + b  # find each col's row
                                        if(state[y][x] == '.'):
                                            move[2] = [y, x]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                else:  # move diagonal2: \
                    b_queen = move[0][0] + \
                        move[0][1]  # y_queen = x_queen + b_queen
                    rangexq0 = None
                    rangexq1 = None
                    if(b_queen < 10):
                        rangexq0 = 0
                        rangexq1 = b_queen
                    else:
                        rangexq0 = b_queen - 9
                        rangexq1 = 9
                    for x_queen in range(rangexq0, rangexq1+1, 1):
                        y_queen = -x_queen + b_queen
                        if(state[y_queen][x_queen] == '.'):
                            move[1] = [y_queen, x_queen]
                            row = y_queen
                            col = x_queen
                            for eachArrowDirection in range(4):
                                if(eachArrowDirection == 0):  # horizontal direction: --
                                    for aCol in range(10):
                                        aRow = move[1][0]
                                        if(state[aRow][aCol] == '.' or
                                                (aRow == row and aCol == col)):  # fire an arrow to the old pos
                                            move[2] = [aRow, aCol]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                elif(eachArrowDirection == 1):  # vertical direction: |
                                    for aRow in range(10):
                                        aCol = move[1][1]
                                        if(state[aRow][aCol] == '.'):
                                            move[2] = [aRow, aCol]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                elif(eachArrowDirection == 2):  # diagonal1 direction: /
                                    b = row - col  # y = x + b
                                    rangex0 = None
                                    rangex1 = None
                                    if(b < 0):  # y go to 0 faster than x
                                        rangex0 = -b
                                        rangex1 = 9  # x go to 9 faster than y
                                    else:  # x go to 0 faster than y
                                        rangex0 = 0
                                        rangex1 = 9 - b  # y go to 9 faster than x
                                    for x in range(rangex0, rangex1+1, 1):  # for each col
                                        y = x + b  # find each col's row
                                        if(state[y][x] == '.'):
                                            move[2] = [y, x]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
                                else:  # diagonal2 direction: \
                                    b = row + col  # y = -x + b
                                    rangex0 = None
                                    rangex1 = None
                                    if(b < 10):  # rangex from 0 to where y=0
                                        rangex0 = 0
                                        rangex1 = b
                                    else:  # rangex from where y=9 to 9
                                        rangex0 = b - 9
                                        rangex1 = 9
                                    for x in range(rangex0, rangex1+1, 1):  # for each col
                                        y = -x + b  # find each col's row
                                        if(state[y][x] == '.'):
                                            move[2] = [y, x]
                                            self.doMove(move, state)
                                            depth = 0
                                            moveVal = self.minimax(
                                                state, depth, False)
                                            if(moveVal - depth > bestVal):
                                                bestMove = move
                                                bestVal = moveVal - depth
                                            self.undoMove(move, state)
        return bestMove

        # Student MUST implement this function
        # The return value should be a move that is denoted by a list of tuples:
        # [(row1, col1), (row2, col2), (row3, col3)] with:
        # (row1, col1): current position of selected amazon
        # (row2, col2): new position of selected amazon
        # (row3, col3): position of the square is shot

    def nextMove(self, state):
        # result = [(0,3),(5,3),(8,6)] # example move in wikipedia
        return self.findBestMove(state)
