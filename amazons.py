
# vec [y,x] ~ [row,col]
vecVertical = [1, 0]
vecHorizontal = [0, 1]
vecDiagonal1 = [1, 1]
vecDiagonal2 = [1, -1]
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
        self.playerPos = [(0,0),(0,0),(0,0),(0,0)]
        self.opponentPos = [(0,0),(0,0),(0,0),(0,0)]
        for row in range(0, 10):
            for col in range(0, 10):
                if(state[row][col] == '.'):
                    continue
                if(state[row][col] == self.str):
                    self.playerPos[pl] = [row,col]
                if(state[row][col] != self.str):
                    self.opponentPos[op] = [row,col]
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
                elif(row > 0):  # [9,x] with 0 < x < 9
                    if(state[row][col-1] == 'X' and state[row][col+1] == 'X'
                            and state[row-1][col] == 'X' and state[row-1][col-1] == 'X'
                            and state[row-1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        else:
                            opponentLose[op] = True
                            op += 1
                elif(col < 9):  # [x,0] with 0 < x < 9
                    if(state[row-1][col] == 'X' and state[row+1][col] == 'X'
                            and state[row][col+1] == 'X' and state[row+1][col+1] == 'X'
                            and state[row-1][col+1] == 'X'):
                        if(state[row][col] == self.str):
                            playerLose[pl] = True
                            pl += 1
                        else:
                            opponentLose[op] = True
                            op += 1
                else:   # [x,9] with 0 < x < 9
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
            return -1   #player loses the game
        elif(all(item == True for item in opponentLose)):
            return 1    #player wins the game
        else:
            return 0    #neither win nor lose


    def doMove(self, move, state):
        state[move[0][0]][move[0][1]] = '.'
        state[move[1][0]][move[1][1]] = self.str
        state[move[2][0]][move[2][1]] = 'X'


    def undoMove(self, move, state):
        state[move[0][0]][move[0][1]] = self.str
        state[move[1][0]][move[1][1]] = '.'
        state[move[2][0]][move[2][1]] = '.'


    def minimax(self, state, isMax):
        score = self.evaluate(state)

        if(score != 0):
            return score
        
        move = [(0,0),(0,0),(0,0)]
        
        if(isMax):
            best = -2
            #make a move for max
            for eachQueen in range(0,4):
                move[0] = self.playerPos[eachQueen] #[row,col]
                for eachQueenMove in range(0,4):
                    if(eachQueenMove == 0): # Move horizontal
                        for col in range(0,10):
                            row = move[0][0]
                            if(state[row][col] == '.'):  #empty slot, it means can move
                                move[1] = [row, col] #save the moved slot
                                for eachArrowDirection in range(0,4):
                                    if(eachArrowDirection == 0):    #horizontal direction
                                        for aCol in range(0,10):
                                            aRow = move[1][0]
                                            if(state[aRow][aCol] == '.' or 
                                                    (aRow == row and aCol == col)): #fire an arrow to the old pos
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(state, !isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 1):  #vertical direction
                                        for aRow in range(0,10):
                                            aCol = move[1][1]
                                            if(state[aRow][aCol] == '.'):
                                                move[2] = [aRow, aCol]
                                                self.doMove(move, state)
                                                best = max(best, self.minimax(state, !isMax))
                                                self.undoMove(move, state)
                                    elif(eachArrowDirection == 2):  #diagonal1 direction
                                        

                
            
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
