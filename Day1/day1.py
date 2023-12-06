def readFile():
    lines = []
    curr = 0
    currSum=0
    with open('data.txt') as file:
        for line in file:
            if line.rstrip()=="":
                lines.append([curr, currSum])
                currSum=0
                curr+=1
            else:
                currSum+=int(line)

        new_list = sorted(lines, key = lambda x: x[1])
        #Part 1:
        #return new_list[::-1][0]
    return new_list[::-1][0][1]+new_list[::-1][1][1]+new_list[::-1][2][1]
        



