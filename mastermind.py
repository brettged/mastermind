# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:59:28 2016

@author: brett
"""
import random

class Peg(object):
    
    def __init__(self, color):
        self.color = color
        
    def __eq__(self, other):
        return self.color == other
        
    def __str__(self):
        return self.color
        
    def getColor(self):
        return self.color
        
black = Peg('black')
white = Peg('white')
red = Peg('red')
blue = Peg('blue')
green = Peg('green')
yellow = Peg('yellow')

pegBank = [black, white, red, blue, green, yellow]       
        
        
# Have the computer choose a random code
def randCode():
    code = []
    for i in range(4):
        code.append(random.choice(pegBank))
    return code

# Has the user choose a code, prompts for the color
# to go at each position
def userCode():
    print "You have chosen to create the secret code! \n" \
           "The color choices are: \n \n" \
           " white \n black \n red \n blue \n yellow \n green \n"
           
    color1 = Peg(raw_input("Enter color for first position: "))
    color2 = Peg(raw_input("Enter color for second position: "))
    color3 = Peg(raw_input("Enter color for third position: "))
    color4 = Peg(raw_input("Enter color for fourth position: "))
    code = [color1, color2, color3, color4]
    return code
        

class Guess(object):
    
    def __init__(self, g1, g2, g3, g4):
        
        self.guess = [Peg(g1), Peg(g2), Peg(g3), Peg(g4)]
    
    def showGuess(self):
        for g in self.guess:
            print g
            
    def iterGuess(self):
        return self.guess
    
    def __eq__(self, other):
        return self.guess == other

class Code(object):
    
    
    def __init__(self, code):
        
        if code == 'cpu':
            self.code = randCode()
        elif code == 'user':
            self.code = userCode()
            
    def showCode(self):
        for c in self.code:
            print c

    def colorCount(self):
        count = {}
        
        for color in self.code:
            if color in count:
                count[color] += 1
            else:
                count[color] = 1
        return count
        
    def checkGuess(self, code, guess):
        
        codeCount = code.colorCount()
        
        clueList = []        
        
        codeList = code.iterCode()
        guessList = guess.iterGuess()
            
        guessIndex = 0
        for guessColor in guessList:
            
            codeIndex = 0
            for codeColor in codeList:
                
                if guessColor == codeColor:
                    
                    if guessIndex == codeIndex:
                        codeCount[codeColor] -= 1
                        
                        if codeCount[codeColor] == 0:
                            del codeCount[codeColor]
                        
                        clueList.append('red')
                codeIndex += 1
            guessIndex += 1

        
        for guessColor in guessList:

            if guessColor in codeCount.keys():
                r = codeCount.keys().index(guessColor)
                codeKey = codeCount.keys()[r]
                clueList.append('white')
                codeCount[codeKey] -= 1
                
                if codeCount[codeKey] == 0:
                    del codeCount[codeKey]
        print clueList
    def iterCode(self):
        return self.code
    def __eq__(self, other):
        return self.code == other


class MasterMind(object):

    def __init__(self):
        pass


def playMasterMind():
    
    print "Welcome to virtual MasterMind!"
    raw_input("Press Enter to continue: ")
    codeGen = raw_input("Would you like to play against the computer? (y or n) ")

    if codeGen == 'y':
        codeGen = 'cpu'
        code = Code(codeGen)
        raw_input("The computer has created a code, please press Enter to begin guessing: ")
    else:
        codeGen = 'user'
        code = Code(codeGen)

    if codeGen == 'cpu':
        raw_input("The computer has created a code, please press Enter to begin guessing: ")

    print "Color choices are: black, white, red, blue, green, and yellow "
    while True:
        
        g = raw_input("Enter Guess: ")
        gParse = g.split()
        
        userGuess = Guess(gParse[0], gParse[1], gParse[2], gParse[3])
        
        code.checkGuess(code, userGuess)
        
        while userGuess != code:
            g = raw_input("Next Guess: ")
            gParse = g.split()
            
            userGuess = Guess(gParse[0], gParse[1], gParse[2], gParse[3])
            
            code.checkGuess(code, userGuess)
                
            if userGuess == code:
                break
        break
    print "Congratulations! \n" \
          "You solved the code!"
    playAgain = raw_input("Would you like to play again? (y or n) ")
    
    if playAgain == 'y':
        playMasterMind()
        
    else:
        print "Goodbye!"
    
playMasterMind()













        
        
        