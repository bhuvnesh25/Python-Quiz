def clear():
    for i in range(30):
        print('\n')

def startInterface():
    clear()
    print('####################')
    print('#                  #')
    print('#      Hangman     #')
    print('#                  #')
    print('####################')
    print('       1.Start      ')
    print('       2.Exit       ')
    choice = int(input('Input Selection: '))
    return choice


def index():
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|\  | ')
        print('        / \  | ')
        print('             | ')
        print('     ________|_')

def index1():
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|\  | ')
        print('        /    | ')
        print('             | ')
        print('     ________|_')

def index2():
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|\  | ')
        print('             | ')
        print('             | ')
        print('     ________|_')

def index3():
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('        /|   | ')
        print('             | ')
        print('             | ')
        print('     ________|_')

def index4():
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('         |   | ')
        print('             | ')
        print('             | ')
        print('     ________|_')

def index5():
        print('         _____ ')
        print('         |   | ')
        print('         O   | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')

def index6():
        print('         _____ ')
        print('         |   | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')

def index7():
        print('         _____ ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')

def index8():
        print('               ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('             | ')
        print('     ________|_')


def Play(secretWord):
    failedGuesses = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    guess = ""
    displayWord = DisplayWord(secretWord)
    gameOver = False

    while not gameOver:
        Input = True
        while Input:
            print("Player", Player, end="")
            guess = input(", please guess a letter: ").upper()
            if len(guess) > 1 or guess not in alphabet:
                print("You did enter a valid guess. Please try again.")
            else:
                Input = False
        if guess in secretWord:
            for i in range(len(secretWord)):
                if secretWord[i] == guess:
                    displayWord[i] = guess
            printword(displayWord)
            if "_" not in displayWord:
                print("Player", Player, " wins!")
                gameOver = True
        else:
            failedGuesses += 1
            print("Your guess is incorrect! Please try again.")
            print("Hangman Status: ", end="")



            if failedGuesses == 1:
                clear()
                index8()
            elif failedGuesses == 2:
                clear()
                index7()
            elif failedGuesses == 3:
                clear()
                index6()
            elif failedGuesses == 4:
                clear()
                index5()
            elif failedGuesses == 5:
                clear()
                index4()
            elif failedGuesses == 6:
                clear()
                index3()
            elif failedGuesses == 7:
                clear()
                index2()
            elif failedGuesses == 8:
                clear()
                index1()
            elif failedGuesses == 9:
                clear()
                index()
                print("You died!")
                gameOver = True
            print("Number of chances left:", 9- failedGuesses)

            printword(displayWord)


def printword(displayWord):
            word = ""
            for i in range(len(displayWord)):
                word += displayWord[i]
            print()
            print("Current Progress: ", word)


def DisplayWord(secretWord):
            displayWord = []
            for i in range(len(secretWord)):
                if secretWord[i] in alphabet:
                    displayWord.append("_")
                else:
                    displayWord.append(secretWord[i])
            return displayWord


def main1():
            global Player
            global alphabet
            Player = 1
            secretWord = ""
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            Start = True

            while Start:
                if Player == 1:
                    print()
                    secretWord = input("Player one, please enter your secret word: ").upper()
                    for i in range(50):
                        print()
                    Player = 2
                    print("Player 2 must guess Player's One's word")
                    Play(secretWord)
                elif Player == 2:
                    print()
                    secretWord = input("Player two, please enter your secret word: ").upper()
                    for i in range(50):
                        print()
                    Player = 1
                    print("Player 1 must guess Player's Two's word")
                    Play(secretWord)
                    exit()
            print()
            print("Thank you for playing Hangman!")


import random

wordlist = ['PHONE', 'HAPPY', 'APPLE', 'EARTH', 'GONGYIWEI', 'PYTHON', 'PIONEER', 'SINGAPORE', 'FATHER', 'MOTHER',
            'GONGYIWEI']

secret = random.choice(wordlist).upper()
correct = []
incorrect = []


def clear():
    for i in range(30):
        print('\n')


hangman = ['''





            ________|__''',
           '''         




                     |
                     |
            _________|__''',
           '''          
                     |
                     |
                     |
                     |
                     |
           __________|__''',
           '''          
                     \\   
                     |
                     |
                     |
                     |
                     |
           __________|__''',

           '''          
             /-------\\
                     |
                     |
                     |
                     |
                     |
           __________|__''',
           '''          
             /-------\\
             O       |
                     |
                     |
                     |
                     |
           __________|__''',
           '''
             /-------\\
             O       |
            /|\      |
                     |
                     |
                     |
           __________|__''',
           '''          
             /-------\\
             O       |
            /|       |
             |       |
                     |
                     |
           __________|__''',
           ''' 
             /--------\\
             O        |
            /|\       |
             |        |
                      |
                      |
           ___________|__''',
           '''  
             /--------\\
             O        |
            /|\       |
             |        |
            /         |
                      |
           ___________|__''',
           '''  
             /--------\\
             O        |
            /|\       |
             |        |
            / \       |
                      |
           ___________|__''']


# 1
def guess_display():
    print("")
    print(hangman[len(incorrect)])
    while True:
        print("#############################################")
        guess = input("Enter your guess:-").upper()
        print("#############################################")
        if guess in correct or guess in incorrect:
            print("You had already guessed the " + guess, " letter.\nGuess Again")
        elif guess.isdigit():
            print("Please enter on letter,not numeric,\nGuess Again")
        elif len(guess) > 1:
            print("Please enter only one letter at a time.\nGuess Again")
        elif len(guess) == 0:
            print("Please enter a Guess")
        else:
            break
    if guess in secret:
        correct.append(guess)
    else:
        incorrect.append(guess)


# 2
def correct_diplay():
    clear()

    print("#############################################")
    for l in secret:
        if l in correct:
            print(l, end=" ")
        else:
            print(str(" _ "), end=" ")
    print("")
    print("#############################################")


# 3
def incorrect_display():
    print("\n")
    print("#######---INCORRECT CHANCE ONLY 10 ---#######")
    for l in incorrect:
        print(l, end=" ")
    print("")
    print("#############################################")


def check_win():
    if len(incorrect) > 9:
        return "lose"

    for i in secret:
        if i not in correct:
            return "no win"
    return "win"


def main():
    while True:

        correct_diplay()
        incorrect_display()
        guess_display()
        win_condition = check_win()

        if win_condition == "lose":
            print("GAME OVER! YOU DIE\n The word is    ", secret)
            print(hangman[10])
            break
        elif win_condition == "win":
            print("YOU WIN! \n The word is    ", secret)
            break


print(" __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.")
print("|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |")
print("|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |")
print("|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |")
print("|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |")
print("|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|")
print('###############################################################################')
print('#                          (Version)5.0.1                                     #')
print('#                           Android  game                                     #')
print('#                      Made by:-BHUVNESH KUMAR                                #')
print('#                  CSE Student    Working on Python                           #')
print('###############################################################################')
print()
print('#    Wait for starting...', end='')
print('<=========================================> 100% DONE!')
input('#    Press Enter')


def startInterface():
    clear()
    print('##########################################################################')
    print('#                                                                        #')
    print('#                               MENU                                     #')
    print('#                                                                        #')
    print('##########################################################################')
    print('                         1.Play offline                                   ')
    print('                         2.Play online                                    ')
    print('                         3.Exit                                           ')
    while True:
        try:

            choice = int(input('Input Selection: '))
            break
        except ValueError:
            print("Enter Valid Input no character")
    return choice


sel=startInterface()
if sel==1:
    main1()
elif sel==2:
    main()
elif sel==3:
    exit()
