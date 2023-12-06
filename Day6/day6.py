def readFile():
    data = ""
    time = ""
    recordDistance = ""
    with open('day6.txt') as file:
        for i in file:
            data += i
    time, recordDistance = data.split("Distance")
    return time, recordDistance

def part2():
    time, recordDistance = readFile()
    timeData, recordData = formatData(time, recordDistance)
    newTime = ""
    newRecord = ""
    for i in timeData:
        newTime += str(i)
    print("time: ", newTime)
    for i in recordData:
        newRecord += str(i)
    print("record: ", newRecord)
    turns = checkTurns(int(newTime), int(newRecord))
    return turns
    
  #  print("time. ", timeData, "record: ", recordData)
        

def formatData(time, recordDistance):
  #  time, recordDistance = readFile()
    timeData = []
    number = ""
    for i in time:
        if i == " " and number:
            timeData.append(int(number))
            number = "" #ny siffra
        elif i.isdigit() and i != " " and i != ":":
            number += i
    timeData.append(int(number))
    number = ""
    recordData = []
    for i in recordDistance:
        if i == " " and number:
            recordData.append(int(number))
            number = "" #ny siffra
        elif i.isdigit() and i != " " and i != ":":
            number += i
    recordData.append(int(number))
    return timeData, recordData



        
 
        
