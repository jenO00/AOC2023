def readFile():
    signal = ""
    with open('day6.txt') as file:
        for line in file:
            signal += line.rstrip() #add to it
    return signal


def decode():
    signal = readFile()
   # signal = "nppdvjthqldpwncqszvftbrmjlhg"
    #signal="mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    currCount = 0
    totalCount = 0
    used = ""
    found = False
    count = 0
    while found != True:
        if found == True:
            print("Found it :) :", used)
        for i in signal:
           # count+=1
          #  print("Count :", count)
            totalCount+=1
            print("current i :", i)
            if i not in used:
                if currCount == 12:
                    found = True
                else:
                    used+=i
                    print("used :", used)
                    currCount += 1
            else:
                #nollställ värden
                if len(used) != 12:
                    #print("used :", used, currCount, "i :", i)
                    used = "" #retry
                    currCount=0
    return used, signal.index(used)+12-2
                    

def partTwo():
    signal = readFile()
    for x in range(14, len(signal)):
        if len(set(signal[x - 14:x])) == 14:
            print(x)
            exit(0)
