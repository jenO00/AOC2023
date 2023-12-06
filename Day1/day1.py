def readFile():
    lines = []
    with open('day1.txt') as file:
        for line in file:
            lines.append((line.strip()).lower())
   # print(lines)
    return lines

def addNumbers():
    lines = readFile()
    sumOfNumbers = 0
    currentNumber1 = ""
    currentNumber2 = ""
    currDigitWord = ""
    digits = {"one": "1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    currDigit = ""
    first_number = ""
    for i in lines:
        currentNumber1 = "" #återställ
        currentDigitWord = ""
        WordWithLast = ""
        for char in i:
            if char.isdigit() == True:
                currentNumber1 += char
                currentDigitWord = "" #it wont be a word in that case
                WordWithLast = "" #wont be this either
            else:
                currDigitWord += char.lower()
                WordWithLast += char.lower()
                for key in digits.keys():
                    if key in currDigitWord:
                        currentNumber1 += digits[key]
                        WordWithLast = currDigitWord[::-1][0]
                        currDigitWord = ""
                        
                    elif key in WordWithLast:
                        currentNumber1 += digits[key]
                        WordWithLast = WordWithLast[::-1][0]
                        currDigitWord = ""
                if currDigitWord in digits:
                    currentNumber1 += digits[currDigitWord]
                    WordWithLast = currDigitWord[::-1][0]
                    currDigitWord = ""
                elif WordWithLast in digits:
                    currentNumber1 += digits[WordWithLast]
                    #lägg den i numret --> andra ska tömmas
                    currDigitWord = ""
                    WordWithLast = WordWithLast[::-1][0]
        currentNumber2 = currentNumber1[0] + currentNumber1[-1]
        sumOfNumbers += int(currentNumber2)
    return sumOfNumbers
