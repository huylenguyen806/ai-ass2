
# vec [y,x] ~ [row,col]
vecVertical = [1, 0]
vecHorizontal = [0, 1]
vecDiagonal = [1, 1]
# ======================== Class Player =======================================


class Player:
    # student do not allow to change two first functions
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return self.str

    def evaluate(self, state):
        playerLose = [False, False, False, False]
        opponentLose = [False, False, False, False]
        pl = 0
        op = 0
        for row in range(0, 10):
            for col in range(0, 10):
                if(state[row][col] == '.'):
                    continue
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
                        else:
                            opponentLose[op] = True
                            op += 1
                elif(row > 0 and col > 0):  # [9,9]
                    if(state[row-1][col] == 'X' and state[row][col-1] == 'X'
                            and state[row-1][col-1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        else:
                            opponentLose[op] = True
                            op += 1
                elif(row < 9 and col < 9):  # [0,0]
                    if(state[row+1][col] == 'X' and state[row][col+1] == 'X'
                            and state[row+1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        else:
                            opponentLose[op] = True
                            op += 1
                elif(row > 0 and col < 9):  # [9,0]
                    if(state[row-1][col] == 'X' and state[row][col+1] == 'X'
                            and state[row-1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        else:
                            opponentLose[op] = True
                            op += 1
                elif(row < 9 and col > 0):  # [0,9]
                    if(state[row][col-1] == 'X' and state[row+1][col] == 'X'
                            and state[row+1][col-1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        else:
                            opponentLose[op] = True
                            op += 1
                elif(row < 9):  # [0,x] with 0 < x < 9
                    if(state[row][col-1] == 'X' and state[row][col+1] == 'X'
                            and state[row+1][col] == 'X' and state[row+1][col-1] == 'X'
                            and state[row+1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        else:
                            opponentLose[op] = True
                            op += 1
                elif(row < 0):
                    if(state[row][col-1] == 'X' and state[row][col+1] == 'X'
                            and state[row-1][col] == 'X' and state[row-1][col-1] == 'X'
                            and state[row-1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        else:
                            opponentLose[op] = True
                            op += 1
                elif(col < 9):
                    if(state[row-1][col] == 'X' and state[row+1][col] == 'X'
                            and state[row][col+1] == 'X' and state[row+1][col+1] == 'X'
                            and state[row-1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        else:
                            opponentLose[op] = True
                            op += 1
                else:
                    if(state[row-1][col] == 'X' and state[row+1][col] == 'X'
                            and state[row-1][col-1] == 'X' and state[row][col-1] == 'X'
                            and state[row+1][col-1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        else:
                            opponentLose[op] = True
                            op += 1

        if(all(item == True for item in playerLose)):
            return -1
        elif(all(item == True for item in opponentLose)):
            return 1
        else:
            return 0

    def minimax(self, state, isMax):
        score = self.evaluate(state);

        if(score != 0):
            return score
        
        if(isMax):
            best = -2
            #make a move for max
            best = max(best, self.minimax(state, !isMax))
            return best
        else:
            best = 2
            #make a move for min
            best = min(best, self.minimax(state, !isMax))
            return best

        # Student MUST implement this function
        # The return value should be a move that is denoted by a list of tuples:
        # [(row1, col1), (row2, col2), (row3, col3)] with:
        # (row1, col1): current position of selected amazon
        # (row2, col2): new position of selected amazon
        # (row3, col3): position of the square is shot

    def nextMove(self, state):
        # result = [(0,3),(5,3),(8,6)] # example move in wikipedia
        result = None

        return result
