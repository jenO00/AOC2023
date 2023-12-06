def readFile():
    lines = []
    with open('day2.txt') as file:
        for line in file:
            lines.append((line.strip()).lower())
    #print(lines)
    return lines

#Part1
def possibleGames():
    listgames = readFile()
    colon = ":"
    comma = ","
    semi = ";"
    IDCount = 0
    correctIDS = 0
    yesno= []
    testData = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue','Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red','Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
    games = []
    for game in listGames:
        print("index: ", listgames.index(game))
        if listgames.index(game) < 99:
            games.append(game[8:].rstrip(''))
        else:
            games.append(game[9:].rstrip(''))
    for i in games:
        IDCount += 1
        number = ""
        blueCount = 0
        redCount = 0
        greenCount = 0
        color = ""
        for char in i:
            if char.isdigit():
                #if it is a number
                number += char
           
            elif char == semi:
                #new game
                blueCount = 0
                greenCount = 0
                redCount = 0
                number = ""
                print("NEW GAME, IDCOUNT: ", IDCount)
            elif char != comma and char != " " and not char.isdigit():
                color += char
                if color == "blue":
                    blueCount += int(number)
                    if blueCount > 14:
                        yesno.append("no")
                    else:
                        yesno.append("yes")
                    print("Blue: ", blueCount)
                    number = "" #nollställ
                    color = ""
                elif color == "green":
                    greenCount += int(number)
                    print("Green: ", greenCount)
                    if greenCount > 13:
                        yesno.append("no")
                    else:
                        yesno.append("yes")
                    number = ""
                    color = ""
                elif color == "red":
                    redCount += int(number)
                    print("Red: ", redCount)
                    if redCount > 12:
                        yesno.append("no")
                    else:
                        yesno.append("yes")
                    number = ""
                    color = ""
                else:
                    pass
        print("Yesno: ", yesno)
        if "no" in yesno:
            yesno = [] #återställ fuck den
        else:
            correctIDS += IDCount
            yesno = [] #återställ
    return correctIDS
        
        
def leastNeeded():
    listgames = readFile()
    colon = ":"
    comma = ","
    semi = ";"
    IDCount = 0
    correctIDS = 0
    yesno= []
    res = 0
    testData = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue','Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red','Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
    games = []
    for game in listgames:
         if listgames.index(game) < 99:
             games.append(game[8:].rstrip(''))
         else:
             games.append(game[9:].rstrip(''))
    biggestBlue = 0
    biggestRed = 0
    biggestGreen = 0
    for i in games:
        res += biggestRed*biggestGreen*biggestBlue
        print("res: ", res)
        IDCount += 1
        #loop through each
        number = ""
        blueCount = 0
        redCount = 0
        greenCount = 0
        biggestBlue = 0
        biggestRed = 0
        biggestGreen = 0
        color = ""
        for char in i:
            if char.isdigit():
                #if it is a number
                number += char
           
            elif char != comma and char != " " and not char.isdigit() and char != semi:
                color += char
             #   print("Color: ", color)
              #  print("Color: ", color)
                if color == "blue":
                    blueCount += int(number)
                    if blueCount > biggestBlue:
                        biggestBlue = blueCount
                     
                    number = "" #nollställ
                    color = ""
                elif color == "green":
                    greenCount += int(number)
                    if greenCount > biggestGreen:
                        biggestGreen = greenCount
                    
                    number = ""
                    color = ""
                elif color == "red":
                    redCount += int(number)
                    if redCount > biggestRed:
                        biggestRed = redCount
        
                    number = ""
                    color = ""
                else:
                    pass
            elif char == semi:
                #new game
              
                blueCount = 0
                greenCount = 0
                redCount = 0
                number = ""
                print("NEW GAME, IDCOUNT: ", IDCount)
    res += biggestRed*biggestGreen*biggestBlue
    print("res: ", res)
    return res     
