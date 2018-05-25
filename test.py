from main import Initial_Board
from amazons import Player

def eval():
    a = Player('w')
    playerPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
    opponentPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
    print(a.evaluate(Initial_Board, playerPos, opponentPos))
    print(playerPos)
    print(opponentPos)

eval()