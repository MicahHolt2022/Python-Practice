#defining the variable function
def twitchSub(userName):
    #setting output
    print(userName + " has joined the MikaMovement!")
#running function twitchSub
twitchSub("sampleUser123")

#-------------------------- 

#defining my functions
#defining my five favorite films
def fiveFavFilms():
    #print first favorite movie
    print("Rogue One")
    #print second favorite movie
    print("La La Land")
    #print third favorite movie
    print("Megamind")
    #print fourth favorite movie
    print("The Empire Strikes Back")
    #print fifth favorite movie
    print("Knives Out")

#-----------------------------------

#defining snakeEater
def snakeEater():
    #clanking
    print("clank")
    print("clank")
    print("clank")
    print("clank")
    print("clank")
    #saying the first line
    print("What a thrill...")
    #clanking
    print("clank")
    print("clank")
    print("clank")
    print("clank")
    print("clank")
    print("clank")
#defining mySiblings
def mySiblings():
    #print oldest to youngest, my siblings
    print("Caleb")
    print("Susanna")
    print("Grace")
    print("Isak")
    print("Phoebe")
    print("Magdalena")
#defining orderSixtySix
def orderSixtySix():
    #print Palpatine's line
    print("Commander Cody, the time has come. Execute Order Sixty-Six.")
    #print Cody's line
    print("It will be done, my lord.")
#defining my favorite colors
def favoriteColors():
    #print best colors
    print("Dark Green")
    print("Royal Purple")
    print("Black")
#defining bestTeacher
def bestTeacher():
    #printing the question
    print("And the best teacher is...")
    #printing mr osowski
    print("Mr Osowski!")
#defining myNameIs using variables
def myNameIs(snake):
    #defining parameter + print is my name // output string
    print(snake + " is my name")
#printing title
print("These are my five favorite movies!")
#running shortcut fiveFavFilms
fiveFavFilms()
#running snakeEater
snakeEater()
#running mySiblings
mySiblings()
#running orderSixtySix
orderSixtySix()
#running favoriteColors
favoriteColors()
#running bestTeacher
bestTeacher()
#run myNameIs
myNameIs("Mr Osowski")
myNameIs("Snake")

#----------------------------

#defining variable function
def timesTwo(unit):
    #setting output
    print(unit * 2)
#running function
timesTwo(30)

#defining variable function
def plusFive(unit):
    #setting output
    print(unit + 5)
#running function
plusFive(30)

#defining variable function
def dividedByTwo(unit):
    #setting output
    print(unit / 2)
#running function
dividedByTwo(30)

#defining variable function
def addTwoNumbers(unit,unita):
    #setting output
    print(unit + unita)
#running function
addTwoNumbers(10,59)

#defining variable function
def multiply(unit,unita):
    #setting output
    print(unit * unita)
#running function
multiply(2, 3)

#defining woof
def woof():
    #defining substitute
    return "Woof!"
#printing woof()'s substitute
print(woof())


#generate random integer values
from random import seed
from random import randint
#seed random number generator
seed(1)
#generate integers
for _ in range(1):
    value = randint(0,100)
    print(value)

#if statements

def functionWord(word):
    word = word.lower
    if word == "yellow":
        return "cool"
print(functionWord("YeLLOw"))

def greaterThan10(x):
    if x > 10:
        return "x is greater than 10."

    elif x == 10:
        return "x equals 10."

    else:
        return "x is not greater than 10."     
        
print(greaterThan10(5))

#Modulus Operators

print(23 % 10)
print(3 % 2)
print(99 % 100)

def evenOrOdd(a):
    if (a % 2) == 0:
        return True
    else:
        return False

print(evenOrOdd())

#Boolean Logic Expressions
#Boolean Operator "And"
def twoBigAndNumbers(x,y):
    if x > 10 and y > 10:
        return True
    else: 
        return False


    #JANKY ALERT
    def twoBigNumbers(x,y):
        if x > 10:
            if y > 10:
                return True
            else:  False
        else: False
    #JANKY

#Boolean Operator "Or"
def twoBigOrNumbers(x,y):
    if x > 10 or y > 10:
        return True
    else: 
        return False

#Boolean Operator "Not"
def twoBigNotNumbers(x,y):
    if x > 10 or not y > 10:
        return True
    else: 
        return False

#forcing order of operations
def threeBigNumbers(x,y,z):
    if x > 10 or (not y > 10 and z == 5): 
        return True
    else: 
        return False