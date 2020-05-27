#Bagel (final version: July 5th, 2019)

import random

def NumberGenerator():
    Digit_List = '0 1 2 3 4 5 6 7 8 9'.split()
    Digit1 = random.randint(0, 10)

    Digit_List.remove(str(Digit1))
    Digit2 = random.choice(Digit_List)
    Digit_List.remove(str(Digit2))
    Digit3 = random.choice(Digit_List)
    ComputerNumber = str(Digit1)+ Digit2 + Digit3
    List_ComputerNumber = [str(Digit1), Digit2, Digit3]
    return List_ComputerNumber

def CheckForNumbers(guess):
    loop = 0
    for i in range(0, 3):
        if guess[i] not in "0 1 2 3 4 5 6 7 8 9".split():
            loop += 1

    if loop != 0:
        print("You need to type in numbers only")
        StateOf_Input = False
        return StateOf_Input

def CheckForSameNumbers(guess):
    Digit_List = '0 1 2 3 4 5 6 7 8 9'.split()
    for i in range(0, 3):
        if guess[i] in Digit_List:
             Digit_List.remove(guess[i])
        else:
            print("You need to type 3 different digits")
            StateOf_Input = False
            return StateOf_Input

def CheckForLenght(guess):
    if len(guess) != 3:
        print("Your number needs to be 3 digits long")
        StateOf_Input = False
        return StateOf_Input


def AskPlayer(): #gotta do -> player_guess = AskPlayer => this variable is a LIST
    gamePlay = True
    while gamePlay == True:
        print("Guess a number with 3 digits, all different from one another")
        guess = input()
        if CheckForLenght(guess) !=False:
            if CheckForNumbers(guess) != False:
                if CheckForSameNumbers(guess) != False:
                
                    break
    guess_asList = list(guess)
    return guess_asList


def CheckWin(player_guess, computer_random):
    if player_guess == computer_random: #note that computer_random is a list, so is player_guess
        PlayerWin = True
        return PlayerWin

def CheckPosition(player_guess, computer_random):
    LeftOver_Guess = []
    Clue_List = []
    for i in range(0, 3):
        if player_guess[i] == computer_random[i]:
            Clue_List.append("Fermi")
        else:
            LeftOver_Guess.append(player_guess[i])
    return Clue_List, LeftOver_Guess

def CheckDigits(LeftOver_Guess, computer_random, Clue_List):
    for i in range(0, len(LeftOver_Guess)):
        if LeftOver_Guess[i] in computer_random:
            Clue_List.append("Pico")
    if Clue_List != []:
        return Clue_List
    else:
        return None

def PlayAgain():
    print("Play again?")
    Play = input().lower().startswith('y')
    return Play



#_________________________
print('''Welcome to Bagels.
The game is this: I will choose a random number comprising of 3 different digits.
You have 8 chances to guess that number.
For each guess, I will give you clues like so:
    I will say "Fermi" for every digit you've guessed correctly and that are in their right position
    I will say "Pico" for every digit you've guessed correctly but that are not in the right position
    I will say "Bagels" if none of the digits are right

    ex. If the number was 123 and you guessed 321, I will say "Fermi pico pico"
    ''')

Play = True


computer_random = NumberGenerator()

while Play == True:
    NumberOfGuesses = 0
    
    while NumberOfGuesses < 8:
        guess = AskPlayer()
        player_guess = list(guess)
        
        PlayerWinning = CheckWin(player_guess, computer_random)
        if  PlayerWinning == True:
            break
        else:
            ClueList, LeftOverGuess = CheckPosition(player_guess, computer_random)
            ClueList2 = CheckDigits(LeftOverGuess, computer_random, ClueList)
            if ClueList2 != None:
                GiveClues = " ".join(ClueList2)
                print(GiveClues)
            else:
                print("Bagels")
            NumberOfGuesses += 1
    if PlayerWinning == True:
        print("You got it!")

    else:
        computer_number = computer_random[0] + computer_random[1] + computer_random[2]
        print("You've ran out of choices: you lose. The number was ", computer_number)
    Play = PlayAgain()
