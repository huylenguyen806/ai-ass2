

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
                if(state[row][col] == '.' or state[row][col] == 'X'):
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
                elif(row > 0 and col > 0):  # [9,9]
                    if(state[row-1][col] != '.' and state[row][col-1] != '.'
                            and state[row-1][col-1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row < 9 and col < 9):  # [0,0]
                    if(state[row+1][col] != '.' and state[row][col+1] != '.'
                            and state[row+1][col+1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row > 0 and col < 9):  # [9,0]
                    if(state[row-1][col] != '.' and state[row][col+1] != '.'
                            and state[row-1][col+1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row < 9 and col > 0):  # [0,9]
                    if(state[row][col-1] != '.' and state[row+1][col] != '.'
                            and state[row+1][col-1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row < 9):  # [0,x] with 0 < x < 9
                    if(state[row][col-1] != '.' and state[row][col+1] != '.'
                            and state[row+1][col] != '.' and state[row+1][col-1] != '.'
                            and state[row+1][col+1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(row > 0):  # [9,x] with 0 < x < 9
                    if(state[row][col-1] != '.' and state[row][col+1] != '.'
                            and state[row-1][col] != '.' and state[row-1][col-1] != '.'
                            and state[row-1][col+1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                elif(col < 9):  # [x,0] with 0 < x < 9
                    if(state[row-1][col] != '.' and state[row+1][col] != '.'
                            and state[row][col+1] != '.' and state[row+1][col+1] != '.'
                            and state[row-1][col+1] != '.'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                        else:
                            opponentLose[op] = True
                else:   # [x,9] with 0 < x < 9
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

        plIsLost = False
        opIsLost = False
        if(all(item == True for item in playerLose)):
            plIsLost = True  # player loses the game
        elif(all(item == True for item in opponentLose)):
            opIsLost = True  # player wins the game
        if(plIsLost and not opIsLost):
            return -1
        elif(not plIsLost and opIsLost):
            return 1
        else:
            return 0

    def doMove(self, move, state, string):
        state[move[0][0]][move[0][1]] = '.'
        state[move[1][0]][move[1][1]] = string
        state[move[2][0]][move[2][1]] = 'X'

    def undoMove(self, move, state, string):
        state[move[2][0]][move[2][1]] = '.'
        state[move[1][0]][move[1][1]] = '.'
        state[move[0][0]][move[0][1]] = string

    def minimax2(self, state, depth, isMax, alpha, beta):
        playerPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
        opponentPos = [[0, 0], [0, 0], [0, 0], [0, 0]]

        score = self.evaluate(state, playerPos, opponentPos)

        if(score != 0 or depth > 5):
            return score

        move = [[0, 0], [0, 0], [0, 0]]

        if(isMax):
            best = -9999
            # iterate each player
            for eachPlayer in range(4):
                move[0] = playerPos[eachPlayer]
                # iterate each move (there're 8 moves):
                #up, down, left, right, upleft, upright, downleft, downright
                for eachMove in range(8):
                    row0 = move[0][0]
                    col0 = move[0][1]
                    # move up
                    if(eachMove == 0):
                        # decreasing row
                        for eachRow in range(row0 - 1, -1, -1):
                            if(state[eachRow][col0] != '.'):
                                break
                            move[1] = [eachRow, col0]
                            # fire arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                    # move down
                    elif(eachMove == 1):
                        # increasing row
                        for eachRow in range(row0 + 1, 10, 1):
                            if(state[eachRow][col0] != '.'):
                                break
                            move[1] = [eachRow, col0]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                    # move left
                    elif(eachMove == 2):
                        # decreasing col
                        for eachCol in range(col0 - 1, -1, -1):
                            if(state[row0][eachCol] != '.'):
                                break
                            move[1] = [row0, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                    # move right
                    elif(eachMove == 3):
                        # increasing col
                        for eachCol in range(col0 + 1, 10, 1):
                            if(state[row0][eachCol] != '.'):
                                break
                            move[1] = [row0, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                    # move upleft
                    elif(eachMove == 4):
                        # y = ax + b and decreasing iteration (y = row0, x = col0)
                        eachRow = row0
                        for eachCol in range(col0 - 1, -1, -1):
                            eachRow -= 1
                            if(eachRow < 0 or state[eachRow][eachCol] != '.'):
                                break
                            move[1] = [eachRow, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                    # move upright
                    elif(eachMove == 5):
                        # y = -ax + b, increasing x, decreasing y (y = row0, x= col0)
                        eachRow = row0
                        for eachCol in range(col0 + 1, 10, 1):
                            eachRow -= 1
                            if(eachRow < 0 or state[eachRow][eachCol] != '.'):
                                break
                            move[1] = [eachRow, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                    # move downleft
                    elif(eachMove == 6):
                        # y = -ax + b, decreasing x, increasing y (y = row0, x = col0)
                        eachRow = row0
                        for eachCol in range(col0 - 1, -1, -1):
                            eachRow += 1
                            if(eachRow > 9 or state[eachRow][eachCol] != '.'):
                                break
                            move[1] = [eachRow, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                    # move downright
                    else:
                        # y = ax + b and increasing iteration (y = row0, x = col0)
                        eachRow = row0
                        for eachCol in range(col0 + 1, 10, 1):
                            eachRow += 1
                            if(eachRow > 9 or state[eachRow][eachCol] != '.'):
                                break
                            move[1] = [eachRow, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, self.str)
                                        depth += 1
                                        best = max(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        alpha = max(alpha, best)
                                        self.undoMove(move, state, self.str)
                                        if(beta <= alpha):
                                            break

            return best
        else:
            best = 9999
            opstr = 'w'
            if(self.str == 'w'):
                opstr = 'b'
            # iterate each opponent
            for eachOpponent in range(4):
                move[0] = opponentPos[eachOpponent]
                # iterate each move (there're 8 moves):
                #up, down, left, right, upleft, upright, downleft, downright
                for eachMove in range(8):
                    row0 = move[0][0]
                    col0 = move[0][1]
                    # move up
                    if(eachMove == 0):
                        # decreasing row
                        for eachRow in range(row0 - 1, -1, -1):
                            if(state[eachRow][col0] != '.'):
                                break
                            move[1] = [eachRow, col0]
                            # fire arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                    # move down
                    elif(eachMove == 1):
                        # increasing row
                        for eachRow in range(row0 + 1, 10, 1):
                            if(state[eachRow][col0] != '.'):
                                break
                            move[1] = [eachRow, col0]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                    # move left
                    elif(eachMove == 2):
                        # decreasing col
                        for eachCol in range(col0 - 1, -1, -1):
                            if(state[row0][eachCol] != '.'):
                                break
                            move[1] = [row0, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                    # move right
                    elif(eachMove == 3):
                        # increasing col
                        for eachCol in range(col0 + 1, 10, 1):
                            if(state[row0][eachCol] != '.'):
                                break
                            move[1] = [row0, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                    # move upleft
                    elif(eachMove == 4):
                        # y = ax + b and decreasing iteration (y = row0, x = col0)
                        eachRow = row0
                        for eachCol in range(col0 - 1, -1, -1):
                            eachRow -= 1
                            if(eachRow < 0 or state[eachRow][eachCol] != '.'):
                                break
                            move[1] = [eachRow, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                    # move upright
                    elif(eachMove == 5):
                        # y = -ax + b, increasing x, decreasing y (y = row0, x= col0)
                        eachRow = row0
                        for eachCol in range(col0 + 1, 10, 1):
                            eachRow -= 1
                            if(eachRow < 0 or state[eachRow][eachCol] != '.'):
                                break
                            move[1] = [eachRow, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                    # move downleft
                    elif(eachMove == 6):
                        # y = -ax + b, decreasing x, increasing y (y = row0, x = col0)
                        eachRow = row0
                        for eachCol in range(col0 - 1, -1, -1):
                            eachRow += 1
                            if(eachRow > 9 or state[eachRow][eachCol] != '.'):
                                break
                            move[1] = [eachRow, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                    # move downright
                    else:
                        # y = ax + b and increasing iteration (y = row0, x = col0)
                        eachRow = row0
                        for eachCol in range(col0 + 1, 10, 1):
                            eachRow += 1
                            if(eachRow > 9 or state[eachRow][eachCol] != '.'):
                                break
                            move[1] = [eachRow, eachCol]
                            # fire an arrow
                            for eachArrow in range(8):
                                row = move[1][0]
                                col = move[1][1]
                                # fire up
                                if(eachArrow == 0):
                                    # iterating up (which means decreasing row)
                                    for rowi in range(row - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire down
                                elif(eachArrow == 1):
                                    # iterating down (which means increasing row)
                                    for rowi in range(row + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[rowi][col] != '.'):
                                            break
                                        move[2] = [rowi, col]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire left
                                elif (eachArrow == 2):
                                    # iterating left (which means decreasing col)
                                    for coli in range(col - 1, -1, -1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire right
                                elif(eachArrow == 3):
                                    # iterating right (which means increasing col)
                                    for coli in range(col + 1, 10, 1):
                                        # meet an obstacle
                                        if(state[row][coli] != '.'):
                                            break
                                        move[2] = [row, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upleft
                                elif (eachArrow == 4):
                                    # y = +ax + b and decreasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire upright
                                elif (eachArrow == 5):
                                    # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi -= 1
                                        if(rowi < 0 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downleft
                                elif (eachArrow == 6):
                                    # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                    rowi = row
                                    for coli in range(col - 1, -1, -1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

                                # fire downright
                                else:
                                    # y = +ax + b and increasing iteration (y = row, x = col)
                                    rowi = row
                                    for coli in range(col + 1, 10, 1):
                                        rowi += 1
                                        if(rowi > 9 or state[rowi][coli] != '.'):
                                            break
                                        move[2] = [rowi, coli]
                                        self.doMove(move, state, opstr)
                                        depth += 1
                                        best = min(best, self.minimax2(
                                            state, depth, not isMax, alpha, beta))
                                        beta = min(beta, best)
                                        self.undoMove(move, state, opstr)
                                        if(beta <= alpha):
                                            break

            return best

    def findBestMove2(self, state):
        playerPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
        opponentPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.evaluate(state, playerPos, opponentPos)
        print(playerPos)
        bestVal = -99999999999999999
        move = [[0, 0], [0, 0], [0, 0]]
        bestMove = None
        # iterate each player
        for eachPlayer in range(4):
            move[0] = playerPos[eachPlayer]
            # iterate each move (there're 8 moves):
            #up, down, left, right, upleft, upright, downleft, downright
            row0 = move[0][0]
            col0 = move[0][1]
            for eachMove in range(8):
                # move up
                if(eachMove == 0):
                    # decreasing row
                    for eachRow in range(row0 - 1, -1, -1):
                        if(state[eachRow][col0] != '.'):
                            break
                        move[1] = [eachRow, col0]
                        # fire arrow
                        for eachArrow in range(8):
                            row = move[1][0]
                            col = move[1][1]
                            # fire up
                            if(eachArrow == 0):
                                # iterating up (which means decreasing row)
                                for rowi in range(row - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire down
                            elif(eachArrow == 1):
                                # iterating down (which means increasing row)
                                for rowi in range(row + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire left
                            elif (eachArrow == 2):
                                # iterating left (which means decreasing col)
                                for coli in range(col - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire right
                            elif(eachArrow == 3):
                                # iterating right (which means increasing col)
                                for coli in range(col + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upleft
                            elif (eachArrow == 4):
                                # y = +ax + b and decreasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upright
                            elif (eachArrow == 5):
                                # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downleft
                            elif (eachArrow == 6):
                                # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downright
                            else:
                                # y = +ax + b and increasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                # move down
                elif(eachMove == 1):
                    # increasing row
                    for eachRow in range(row0 + 1, 10, 1):
                        if(state[eachRow][col0] != '.'):
                            break
                        move[1] = [eachRow, col0]
                        # fire an arrow
                        for eachArrow in range(8):
                            row = move[1][0]
                            col = move[1][1]
                            # fire up
                            if(eachArrow == 0):
                                # iterating up (which means decreasing row)
                                for rowi in range(row - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire down
                            elif(eachArrow == 1):
                                # iterating down (which means increasing row)
                                for rowi in range(row + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire left
                            elif (eachArrow == 2):
                                # iterating left (which means decreasing col)
                                for coli in range(col - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire right
                            elif(eachArrow == 3):
                                # iterating right (which means increasing col)
                                for coli in range(col + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upleft
                            elif (eachArrow == 4):
                                # y = +ax + b and decreasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upright
                            elif (eachArrow == 5):
                                # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downleft
                            elif (eachArrow == 6):
                                # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downright
                            else:
                                # y = +ax + b and increasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                # move left
                elif(eachMove == 2):
                    # decreasing col
                    for eachCol in range(col0 - 1, -1, -1):
                        if(state[row0][eachCol] != '.'):
                            break
                        move[1] = [row0, eachCol]
                        # fire an arrow
                        for eachArrow in range(8):
                            row = move[1][0]
                            col = move[1][1]
                            # fire up
                            if(eachArrow == 0):
                                # iterating up (which means decreasing row)
                                for rowi in range(row - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire down
                            elif(eachArrow == 1):
                                # iterating down (which means increasing row)
                                for rowi in range(row + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire left
                            elif (eachArrow == 2):
                                # iterating left (which means decreasing col)
                                for coli in range(col - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire right
                            elif(eachArrow == 3):
                                # iterating right (which means increasing col)
                                for coli in range(col + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upleft
                            elif (eachArrow == 4):
                                # y = +ax + b and decreasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upright
                            elif (eachArrow == 5):
                                # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downleft
                            elif (eachArrow == 6):
                                # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downright
                            else:
                                # y = +ax + b and increasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                # move right
                elif(eachMove == 3):
                    # increasing col
                    for eachCol in range(col0 + 1, 10, 1):
                        if(state[row0][eachCol] != '.'):
                            break
                        move[1] = [row0, eachCol]
                        # fire an arrow
                        for eachArrow in range(8):
                            row = move[1][0]
                            col = move[1][1]
                            # fire up
                            if(eachArrow == 0):
                                # iterating up (which means decreasing row)
                                for rowi in range(row - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire down
                            elif(eachArrow == 1):
                                # iterating down (which means increasing row)
                                for rowi in range(row + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire left
                            elif (eachArrow == 2):
                                # iterating left (which means decreasing col)
                                for coli in range(col - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire right
                            elif(eachArrow == 3):
                                # iterating right (which means increasing col)
                                for coli in range(col + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upleft
                            elif (eachArrow == 4):
                                # y = +ax + b and decreasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upright
                            elif (eachArrow == 5):
                                # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downleft
                            elif (eachArrow == 6):
                                # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downright
                            else:
                                # y = +ax + b and increasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                # move upleft
                elif(eachMove == 4):
                    # y = ax + b and decreasing iteration (y = row0, x = col0)
                    eachRow = row0
                    for eachCol in range(col0 - 1, -1, -1):
                        eachRow -= 1
                        if(eachRow < 0 or state[eachRow][eachCol] != '.'):
                            break
                        move[1] = [eachRow, eachCol]
                        # fire an arrow
                        for eachArrow in range(8):
                            row = move[1][0]
                            col = move[1][1]
                            # fire up
                            if(eachArrow == 0):
                                # iterating up (which means decreasing row)
                                for rowi in range(row - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire down
                            elif(eachArrow == 1):
                                # iterating down (which means increasing row)
                                for rowi in range(row + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire left
                            elif (eachArrow == 2):
                                # iterating left (which means decreasing col)
                                for coli in range(col - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire right
                            elif(eachArrow == 3):
                                # iterating right (which means increasing col)
                                for coli in range(col + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upleft
                            elif (eachArrow == 4):
                                # y = +ax + b and decreasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upright
                            elif (eachArrow == 5):
                                # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downleft
                            elif (eachArrow == 6):
                                # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downright
                            else:
                                # y = +ax + b and increasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                # move upright
                elif(eachMove == 5):
                    # y = -ax + b, increasing x, decreasing y (y = row0, x= col0)
                    eachRow = row0
                    for eachCol in range(col0 + 1, 10, 1):
                        eachRow -= 1
                        if(eachRow < 0 or state[eachRow][eachCol] != '.'):
                            break
                        move[1] = [eachRow, eachCol]
                        # fire an arrow
                        for eachArrow in range(8):
                            row = move[1][0]
                            col = move[1][1]
                            # fire up
                            if(eachArrow == 0):
                                # iterating up (which means decreasing row)
                                for rowi in range(row - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire down
                            elif(eachArrow == 1):
                                # iterating down (which means increasing row)
                                for rowi in range(row + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire left
                            elif (eachArrow == 2):
                                # iterating left (which means decreasing col)
                                for coli in range(col - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire right
                            elif(eachArrow == 3):
                                # iterating right (which means increasing col)
                                for coli in range(col + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upleft
                            elif (eachArrow == 4):
                                # y = +ax + b and decreasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upright
                            elif (eachArrow == 5):
                                # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downleft
                            elif (eachArrow == 6):
                                # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downright
                            else:
                                # y = +ax + b and increasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                # move downleft
                elif(eachMove == 6):
                    # y = -ax + b, decreasing x, increasing y (y = row0, x = col0)
                    eachRow = row0
                    for eachCol in range(col0 - 1, -1, -1):
                        eachRow += 1
                        if(eachRow > 9 or state[eachRow][eachCol] != '.'):
                            break
                        move[1] = [eachRow, eachCol]
                        # fire an arrow
                        for eachArrow in range(8):
                            row = move[1][0]
                            col = move[1][1]
                            # fire up
                            if(eachArrow == 0):
                                # iterating up (which means decreasing row)
                                for rowi in range(row - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire down
                            elif(eachArrow == 1):
                                # iterating down (which means increasing row)
                                for rowi in range(row + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire left
                            elif (eachArrow == 2):
                                # iterating left (which means decreasing col)
                                for coli in range(col - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire right
                            elif(eachArrow == 3):
                                # iterating right (which means increasing col)
                                for coli in range(col + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upleft
                            elif (eachArrow == 4):
                                # y = +ax + b and decreasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upright
                            elif (eachArrow == 5):
                                # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downleft
                            elif (eachArrow == 6):
                                # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downright
                            else:
                                # y = +ax + b and increasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                # move downright
                else:
                    # y = ax + b and increasing iteration (y = row0, x = col0)
                    eachRow = row0
                    for eachCol in range(col0 + 1, 10, 1):
                        eachRow += 1
                        if(eachRow > 9 or state[eachRow][eachCol] != '.'):
                            break
                        move[1] = [eachRow, eachCol]
                        # fire an arrow
                        for eachArrow in range(8):
                            row = move[1][0]
                            col = move[1][1]
                            # fire up
                            if(eachArrow == 0):
                                # iterating up (which means decreasing row)
                                for rowi in range(row - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire down
                            elif(eachArrow == 1):
                                # iterating down (which means increasing row)
                                for rowi in range(row + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[rowi][col] != '.'):
                                        break
                                    move[2] = [rowi, col]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire left
                            elif (eachArrow == 2):
                                # iterating left (which means decreasing col)
                                for coli in range(col - 1, -1, -1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire right
                            elif(eachArrow == 3):
                                # iterating right (which means increasing col)
                                for coli in range(col + 1, 10, 1):
                                    # meet an obstacle
                                    if(state[row][coli] != '.'):
                                        break
                                    move[2] = [row, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upleft
                            elif (eachArrow == 4):
                                # y = +ax + b and decreasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire upright
                            elif (eachArrow == 5):
                                # y = -ax + b, increasing x and decreasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi -= 1
                                    if(rowi < 0 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downleft
                            elif (eachArrow == 6):
                                # y = -ax + b, decreasing x and increasing y (y = row, x = col)
                                rowi = row
                                for coli in range(col - 1, -1, -1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

                            # fire downright
                            else:
                                # y = +ax + b and increasing iteration (y = row, x = col)
                                rowi = row
                                for coli in range(col + 1, 10, 1):
                                    rowi += 1
                                    if(rowi > 9 or state[rowi][coli] != '.'):
                                        break
                                    move[2] = [rowi, coli]
                                    self.doMove(move, state, self.str)
                                    depth = 0
                                    moveVal = self.minimax2(
                                        state, depth, False, -9999, 9999)
                                    if(moveVal - depth > bestVal):
                                        bestMove = move
                                        bestVal = moveVal - depth
                                    self.undoMove(move, state, self.str)

        return bestMove

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

    def moveUpLeft(self, move, step, state, isQueen): #decrease both row, col
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

    def moveDownRight(self, move, step, state, isQueen): #increase both row, col
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

    def moveUpRight(self, move, step, state, isQueen): #increase col, decrease row
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

    def moveDownLeft(self, move, step, state, isQueen): #decrease col, increase row
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

    def nextMove(self, state):
        # result = [(0,3),(5,3),(8,6)] # example move in wikipedia
        return self.findBestMove2(state)
