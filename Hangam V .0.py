import random

def get_word():
    words=["lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop","laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"]
    return random.choice(words).upper()

def check(word,guesses,guess):
    status=""
    matches=0
    for letter in word:
        if letter in guesses:
            status=status + letter
        else:
            status=status +'_'
        if letter==guess:
            matches=matches + 1
    if matches>1:
        print("Yes! the word contains",matches,"'" + guess + "'" +"s")
    elif matches==1:
        print("Yes!the word contain the letter" + guess + "'")
    else:
        print("sorry ,the word does not contain the leter:- "+ guess +"'")
    return status


def main():
    word=get_word()
    guesses=[]
    gussed=False
    limit=0

    print("the word contains",len(word),"letters")
    while not gussed:
        guess=input("please enter one letter or a {}-letter word.".format(len(word))).upper()
        if guess in guesses:
            print("you already guessed"+ guess + '"')
        elif len(guess)==len(word):
            guesses.append(guess)
            if guess==word:
                gussed=True
            else:
                print("sorry,that is incorrect.")
        elif len(guess)==1:
            guesses.append(guess)
            result=check(word,guesses,guess)
            if result==word:
                gussed=True

            else:
                print(result)
        else:
            print("Invalid entry")
    print("Yes ,the word is ",word + "!you got it in",len(guesses),"tries")
main()


