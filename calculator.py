#program to calculate different Arithmetic operation(add,sub,mul,divide,floor division,factorial,modulus,gcd,power)
# function to print welcome message.
def welcome():
 print("Hello!")
 print("Welcome to the calculator ")
 

# Define class calculator.
class Calculator:
# Define our function  calculate.
 def calculate(self):
     #conditional statements to check the user input values are correct(integer) or not.
    while True:
     try:
      #ask the user for first number
      self.num1 = int(input('Please enter the first number: '))#class variable
      break
     except ValueError:
      print("oops!That was not a valid integer number")
      #conditional statements to check the user input values are correct(integer) or not.
    while True:
     try:
      #ask the user for second number .
      self.num2 = int(input('Please enter the second number: '))#class variable
      break
     except ValueError:
      print("oops!That was not a valid integer number")
 #take input from the user to perform that particular operational calculation.
    self.operation = input('''
                      Please type in the math operation you would like to complete:
                      +   for addition
                      -   for subtraction
                      *   for multiplication
                      /   for division
                      //  for floor division
                      %   for modulus
                      f   for factorial
                      **  for power
                      g   for greatest common divisor
                      ''')#class variable

    
    #condutional statements
#addition 
    if self.operation == '+':
        self.c=self.num1+self.num2
        print("addition of",self.num1,"+",self.num2,"=",self.c)
#subtraction 
    elif self.operation == '-':
        self.c=self.num1-self.num2
        print("subtraction of",self.num1,"-",self.num2,"=",self.c)
#multiplication
    elif self.operation == '*':
        self.c=self.num1*self.num2
        print("multiplication of",self.num1,"*",self.num2,"=",self.c)
#division
    elif self.operation == '/':
        self.c=self.num1/self.num2
        print("division of",self.num1,"/",self.num2,"=",self.c)
 #power of a number
    elif self.operation =='**':
        self.c=self.num1**self.num2
        print("power of",self.num1,"**",self.num2,"=",self.c)
 #floor division
    elif self.operation =='//':
        self.c=self.num1//self.num2
        print("floor divison of",self.num1,"//",self.num2,"=",self.c)
#factorial
    elif self.operation =='f':
         import math
         self.fact1=math.factorial(self.num1)
         self.fact2=math.factorial(self.num2)
         print("factorial of ",self.num1,"=",self.fact1)
         print("factorial of ",self.num2,"=",self.fact2)
         
 #modulus 
    elif self.operation =='%':
        self.c=self.num1%self.num2
        print("modulus of",self.num1,"%",self.num2,"=",self.c)
# greatest common divisor  
    elif self.operation=='g':
        import math
        self.result=math.gcd(self.num1,self.num2)
        print("greatest common divisor",self.num1,"and",self.num2,"=",self.result)
#invalid operator enterance    
    else:
        print('You have not typed a valid operator, please run the program again.') 
#function to run calculate function again 
#if user want to do calculation again.
 def again(self):
     #take the input from the user yes or no
    self.cal_again = input('''
                       Do you want to calculate again?
                       Please type YES or NO.
                       ''')#local variable
     #if user type yes run the calculate() function from the class calculator again through object
    if self.cal_again.lower() == 'yes':
        a=Calculator()
        a.calculate()
        a.again()
     #if user type no,print the message and exit the program.
    elif self.cal_again.lower() == 'no':
        import time
        print('Thanks you! See you later.')
        time.sleep(5)
        exit()
     #if user type invalid enterance,run the again() function.
    else:
        import time#import time module for providing delay waiting time
        print("invalid input try again\n please enter yes or no")
        time.sleep(5)
        a=Calculator()
        a.again()
#function calling welcome
welcome()
#creating object of class calculator
a=Calculator()
#calling a function of class through object 
a.calculate()
a.again()