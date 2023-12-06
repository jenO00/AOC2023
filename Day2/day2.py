def readFile():
    #read the file
    moves = []
    with open('day2.txt') as file:
        for line in file:
            moves.append(line.rstrip())
    return moves
            

def rpsStrategy():
    #read the lines
    moves = readFile()
    sumOfMoves = 0
    #Rules as follow:
    #A = rock
    #B = paper
    #C = scissor
    #X = rock, Y = paper, Z = scissor
    #Points: 1 for rock, 2 for paper, 3 for scissors
    #Outcome: 0 if lost, 3 is draw, 6 if won
    for move in moves:
        if move[0] == "A" and move[2] == "X":
            #Rock and Rock, 1+3, rock+draw
            sumOfMoves+=4
        elif move[0] == "A" and move[2] == "Y":
            #rock and paper (2+6)
            sumOfMoves+=8
        elif move[0] == "A" and move[2] == "Z":
            #rock and scissors
            sumOfMoves+=(3+0)
        elif move[0] == "B" and move[2]=="X":
            #paper and rock 1+0
            sumOfMoves+=(1+0)
        elif move[0] == "B" and move[2] == "Y":
            #paper and paper #2+3
            sumOfMoves+=(2+3)
        elif move[0]=="B" and move[2]=="Z":
            sumOfMoves+=(3+6)
        elif move[0]=="C" and move[2]=="X":
            #scissors and rock
            sumOfMoves+=(1+6)
        elif move[0]=="C" and move[2]=="Y":
            #scissors and paper
            sumOfMoves += (2+0)
        else:
            #scissors and scissors
            sumOfMoves +=(3+3)
    return sumOfMoves

def partTwo():
    moves = readFile()
    #A = Rock, B = Paper, C = Scissors
    #X = Lose, Y = Draw, Z = Win
    sumOfMoves = 0
    for move in moves:
        if move[2] == "X":
            #Has to lose
            if move[0] == "A":
                #rock and lose
                #choose scissors
                sumOfMoves+=(3+0)
            if move[0] == "B":
                #they have paper, we choose rock
                sumOfMoves += (1+0)
            if move[0] == "C":
                #they have scissors, we choose paper
                sumOfMoves += (2+0)
        if move[2]=="Y":
            #Create a draw
            if move[0] == "A":
                #rock and rock
                sumOfMoves+=(1+3)
            if move[0]=="B":
                #paper and paper
                sumOfMoves+=(2+3)
            if move[0] == "C":
                #scissors and scissors
                sumOfMoves+=(3+3)
        if move[2]=="Z":
            #must win
            if move[0] == "A":
                #rock and paper
                sumOfMoves+=(2+6)
            if move[0]=="B":
                #paper and scissors
                sumOfMoves+=(3+6)
            if move[0] == "C":
                #scissors and rock
                sumOfMoves+=(1+6)
    return sumOfMoves
    
