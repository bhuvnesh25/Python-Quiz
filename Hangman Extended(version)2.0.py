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


def main():
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
                quit = input("Do you want to quit? (Yes/No): ").upper()
                if quit == "YES" or quit == "Y" or quit == 'y':
                    Start = False
            print()
            print("Thank you for playing Hangman!")

clear()
print(" __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.")
print("|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |")
print("|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |")
print("|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |")
print("|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |")
print("|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|")
print('##########################################################')
print('#                (Versio)2.0                             #')
print('#                Android game                            #')
print('#          Made by:-BHUVNESH KUMAR                       #')
print('#                 CSE Student                            #')
print('##########################################################')
print()
print('#    Wait for starting...', end='')
print('<=========================================> 100% DONE!')
input('#    Press Enter')

sel=startInterface()


if sel==1:
    main()
elif sel==2:
    exit()
else:
    startInterface()