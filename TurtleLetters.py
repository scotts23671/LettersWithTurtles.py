import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.left(90)
        tur.fd(35)
        tur.right(90)
        tur.fd(15)
        #tur.right(180)
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	tur.setheading(0)
        tur.penup()
        tur.fd(15)
        tur.right(90)
        tur.fd(35)
        tur.right(90)
        tur.fd(15)
        tur.right(45)
        tur.fd(12)
        tur.right(180)
        tur.fd(12)
        tur.left(45)
        tur.fd(15)
        tur.left(90)
        tur.fd(35)
        tur.right(90)
        tur.penup()
        tur.fd(15)
    elif letter == "K":
	    pass
    elif letter == "L":
	tur.setheading(0)
        tur.pu
        tur.right(90)
        tur.fd(40)
        tur.left(90)
        tur.fd(20)
        tur.left(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.penup()
        tur.fd(40)
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	tur.setheading(0)
        tur.forward(5)
        tur.right(90)
        tur.forward(50)
        tur.right(180)
        tur.forward(45)
        tur.right(90)
        tur.forward(25)
        tur.right(90)
        tur.forward(20)
        tur.right(90)
        tur.forward(25)
        tur.left(90)
        tur.left(45)
        tur.forward(40)
        tur.penup()
        tur.left(45)
        tur.forward(7)
        tur.left(90)
        tur.forward(53)
        tur.right(90)
    elif letter == "S":
	    pass
    elif letter == "T":
	tur.setheading(0)
        tur.penup()
        tur.forward(5)
        tur.right(90)
        tur.forward(5)
        tur.left(90)
        tur.pendown()
        tur.forward(18)
        tur.right(90)
        tur.forward(45)
        tur.left(180)
        tur.forward(45)
        tur.right(90)
        tur.forward(15)
        tur.penup()
        tur.forward(3)
        tur.left(90)
        tur.forward(6)
        tur.right(90)
        
    elif letter == "U":
	tur.setheading(0)
        tur.penup()
        tur.forward(5)
        tur.pendown()
        tur.right(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(25)
        tur.left(90)
        tur.forward(50)
        tur.penup()
        tur.forward(1)
        tur.right(90)
        tur.forward(12)
    elif letter == "V":
	tur.setheading(0)
        tur.right(65)
        tur.forward(55)
        tur.left(140)
        tur.forward(53)
        tur.penup()
        tur.right(70)
        tur.forward(7)
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
