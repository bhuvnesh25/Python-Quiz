import random

wordlist= ['PHONE','HAPPY','APPLE','EARTH','GONGYIWEI','PYTHON','PIONEER','SINGAPORE','FATHER','MOTHER','GONGYIWEI']


secret = random.choice(wordlist).upper()
correct=[]
incorrect=[]

def clear():
    for i in range(30):
        print('\n')
hangman=['''
                    
                    
                    
                    
                    
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


         
         
         


#1
def guess_display():
        print("")
        print(hangman[len(incorrect)])
        while True:
          print("#############################################")
          guess = input("Enter your guess:-").upper()
          print("#############################################")
          if guess in correct or guess in incorrect:
            print("You had already guessed the "+guess," letter.\nGuess Again")
          elif guess.isdigit():
            print("Please enter on letter,not numeric,\nGuess Again")
          elif len(guess)>1:
            print("Please enter only one letter at a time.\nGuess Again")
          elif len(guess)==0:
            print("Please enter a Guess")
          else:
            break
        if guess in secret:
            correct.append(guess)
        else:
            incorrect.append(guess)


#2
def correct_diplay():
        clear()

        print("#############################################")
        for l in secret:
            if l in correct:
                print(l,end=" ")
            else:
                print(str(" _ "),end=" ")
        print("")
        print("#############################################")
#3
def incorrect_display():
        print("\n")
        print("#######---INCORRECT CHANCE ONLY 10 ---#######")
        for l in incorrect:
            print(l,end=" ")
        print("")
        print("#############################################")

def check_win():

       if len(incorrect)>9:
            return "lose"

       for i in secret:
           if i not in correct:
               return "no win"
       return"win"


def main():
  while True:

    correct_diplay()
    incorrect_display()
    guess_display()
    win_condition=check_win()

    if win_condition=="lose":
      print("GAME OVER! YOU DIE\n The word is    ",secret)
      print(hangman[10])
      break
    elif win_condition=="win":
      print("YOU WIN! \n The word is    ",secret)
      break





print(" __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.")
print("|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |")
print("|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |")
print("|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |")
print("|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |")
print("|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|")
print('##########################################################')
print('#                 (Version)4.0                           #')
print('#                 Android  game                          #')
print('#             Made by:-BHUVNESH KUMAR                    #')
print('#         CSE Student    Working on Python               #')
print('##########################################################')
print()
print('#    Wait for starting...', end='')
print('<=========================================> 100% DONE!')
input('#    Press Enter')

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

sel=startInterface()


if sel==1:
    main()
elif sel==2:
    exit()
else:
    startInterface()