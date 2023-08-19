#eulan spiral
import turtle

#Globals
MAXNUMBER = 1999 #the number that the spiral will count up to
STARTNUMBER = 1000
NUMBERLENGTH = len(str(MAXNUMBER)) #how long (in characters) the numbers are


def isPrime(number):
    if number == 0 or number == 1: #special cases
        return False
    for n in range(2, int((number/2) + 1)):
        if number % n == 0 or number == 0:
            return False
    return True

def spiral(MAXNUMBER, current_num):
    side_length = 1 # the length of the current "side" of the spiral
    
    side_count = 3 #the number of sides round the square that this part of he spiral is
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    t.color("blue")
    while current_num <= MAXNUMBER:
        if side_length > 1:
            side_count = 2
        for i in range(side_count):
            for number in range(side_length):
                if current_num <= MAXNUMBER: #ensuring it doesn't go past the MAXNUMBER constant. 
                    t.forward(NUMBERLENGTH * 7.5) # size of a 3 digit number, will start overlapping after that
                    if isPrime(current_num): 
                        t.color("red")
                    else:
                        t.color("blue")
                    t.write(current_num)
                    current_num += 1
            t.right(90)
        side_length += 1

spiral(MAXNUMBER, STARTNUMBER)
input()