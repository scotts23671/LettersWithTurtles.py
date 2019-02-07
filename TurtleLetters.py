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
        tur.pu()
        tur.fd(10)
        tur.right(90)
        tur.fd(5)
        tur.pendown()
        tur.left(90)
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
        tur.left(90)
        tur.fd(5)
        tur.right(90)
    elif letter == "K":
        tur.setheading(0)
        tur.penup()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pendown()
        tur.fd(40)
        tur.right(180)
        tur.fd(20)
        tur.right(45)
        tur.fd(25)
        tur.right(180)
        tur.fd(25)
        tur.left(90)
        tur.fd(25)
        tur.left(180)
        tur.fd(25)
        tur.right(45)
        tur.fd(20)
        tur.right(90)
        tur.penup()
        tur.fd(35)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
    elif letter == "L":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pendown()
        tur.fd(40)
        tur.left(90)
        tur.fd(20)
        tur.left(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(40)
        tur.right(90)
        tur.penup()
        tur.fd(35)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
    elif letter == "M":
	tur.setheading(0)
        tur.penup()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pendown()
        tur.fd(40)
        tur.right(180)
        tur.fd(40)
        tur.right(135)
        tur.fd(20)
        tur.left(90)
        tur.fd(20)
        tur.right(135)
        tur.fd(40)
        tur.right(180)
        tur.fd(40)
        tur.penup()
        tur.fd(5)
        tur.right(90)
        tur.fd(10)
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
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
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
