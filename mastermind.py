

import random

class Peg(object):
    
    def __init__(self, color):
        self.color = color
    def __eq__(self, other):
        return self.color == other
    def __str__(self):
        return self.color
    def __hash__(self):
        return 0
        
    def getColor(self):
        return self.color

class PegBank(object):
    
    def __init__(self):
        self.bank = []
    def __iter__(self):
        return iter(self.bank)
    def __getitem__(self, i):
        return self.bank[i]
        
    def populate(self):
        black = Peg('black')
        white = Peg('white')
        blue = Peg('blue')
        red = Peg('red')
        green = Peg('green')
        yellow = Peg('yellow')
        colorList = [black, white, blue, red, green, yellow]
        for peg in colorList:
            self.bank.append(peg)

class Sequence(object):

    def __init__(self):
        self.pegList = []
    def __getitem__(self, index):
        return self.pegList[index]
    def __iter__(self):
        return iter(self.pegList)

    def addPeg(self, peg):
        self.pegList.append(peg)
        
    def colorCount(self):
        countDict = {}
        for peg in self.pegList:
            #p = peg.getColor()
            if peg not in countDict:
                countDict[peg] = 1
            else:
                countDict[peg] += 1
        return countDict
    
class Code(Sequence):
    
    def randCode(self, pegBank):
        for i in range(4):
            j = random.choice([0,1,2,3,4,5])
            self.addPeg(pegBank[j])
    
    def userCode(self):
        userColors = input("Enter four colors: ")
        parsed = userColors.split()
        
        for color in parsed:
            if color not in ["white", "black", "blue", "red", "green", "yellow"]:
                print("'{0}' is not a valid color. \n".format(color))
                print("Please pick from: white, black, blue, red, green, or yellow")
                userColors = input("Enter four colors: ")
                parsed = userColors.split()
        for i in parsed:
            self.addPeg(Peg(i))

class Guess(Sequence):
    
    def guess(self):
        userColors = input("Enter your guess: ")
        parsed = userColors.split()
        
        for color in parsed:
            if color not in ["white", "black", "blue", "red", "green", "yellow"]:
                print("'{0}' is not a valid color. \n".format(color))
                print("Please pick from: white, black, blue, red, green, or yellow")
                userColors = input("Enter your guess: ")
                parsed = userColors.split()
        for i in parsed:
            self.addPeg(Peg(i))

    def compGuess(self):
        pass

class Clue(object):
    
    def __init__(self):
        self.clue = []
        self.indexList = []
    def __str__(self):
        return self.clue
        
    def check(self, code, guess):
        guesscolors = guess.colorCount()
        codecolors = code.colorCount()
        indexList = []
        
        for i in range(4):
            if guess[i] == code[i]:
                codecolors[code[i]] -= 1
                self.clue.append('red')
                if codecolors[code[i]] == 0:
                    del codecolors[code[i]]
            else:
                indexList.append(i)
        
        # print(indexList)
        
        for i in indexList:
            if guess[i] in codecolors:
                self.clue.append('white')
                codecolors[guess[i]] -= 1
                if codecolors[guess[i]] == 0:
                    del codecolors[guess[i]]
        # print(self.clue)
        return self.clue
        
class GamePlay(object):
    
    def __init__(self, bank):
        
        self.bank = PegBank()
        self.bank.populate()
        
    def play(self):
        pass
        
    def guessCheck(self, clue):
        pass
        
    def quit(self):
        pass
    
# def main():
#
#     print ("sup bro-beans")
#
# if __name__ == '__main__':
#     main()
    
a = PegBank()
a.populate()
b = Code()
b.randCode(a)
for i in range(4):
    print(b[i])

#print(b.colorCount())

myGuess = Guess()
myGuess.guess()
check = Clue()
check.check(b, myGuess)


    
# c = Code()
# c.userCode()
#
# for i in range(4):
#     print(c[i])
    
    
    
