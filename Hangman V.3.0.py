secretw=input("Enter the secret word:-").upper()
showw =["_"]* len(secretw)
guessing=""
Guess_limit=10
number=0
count=0
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Let's the game Begin .\n you have 10 guess")
while guessing!="END" and Guess_limit!=0:
   print("The word you are looking is" + str(showw))
   print("You have " +  str(Guess_limit)  +  " guess left")
   guessing=input("Enter the letter you want to guess:-").upper()

   while number < len(secretw):
       if secretw[number]==guessing:
           showw[number]=guessing
           count=count+1
       number=number+1
   Guess_limit=Guess_limit-1
   number=0
   if count==len(secretw):
       print("You Won")
       print ("the word is :-",showw)
       break
   if Guess_limit ==0:
       print("You are out of guessing.\n Game Over!")




