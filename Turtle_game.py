## RACING TURTLES
import random
import turtle 

s = turtle.getscreen()
turtle.bgcolor('black')
turtle.title("LET'S RACE !!!!!!")

line = turtle.Turtle()
line.shape('circle')
line.pen(pencolor = 'white')
line.penup()
line.goto(-200, 200)
line.pendown()
line.fd(400)

player_1 = turtle.Turtle()
player_1.shape('turtle')
player_1.goto(-100,-100)
player_1.color('green')
player_1.pen(pencolor = 'blue', speed = 1)
player_1.penup()
player_1.lt(90)

player_2 = turtle.Turtle()
player_2.shape('turtle')
player_2.goto(100,-100)
player_2.color('red')
player_2.pen(pencolor = 'yellow', speed = 1)
player_2.penup()
player_2.lt(90)

om = turtle.Turtle()
ankit = turtle.Turtle()

om.pen(pencolor='green')
om.penup()
om.goto(-100,-150)
om.pendown()
om.write('Om', font=('Cooper Black', '25', 'normal'))
om.lt(90)

ankit.pen(pencolor='red')
ankit.penup()
ankit.goto(100,-150)
ankit.pendown()
ankit.write('Ankit', font=('Cooper Black', '25', 'normal'))
ankit.lt(90)


die = [1,2,3,4,5,6]

i = 100
while i < 200:
    player_1.pendown()
    s = random.choice(die)
    die_1 = input("Om's turn. For rolling die, type 'roll' : ")
    if die_1 == 'roll':
        print('Die showed {}'.format(s))
        player_1.fd(5*s)
    else:
        print('Invalid reply.')
    if player_1.pos() >= (-100,200):
        print('Om WON!')
        break
    else:
        player_1.penup()
        player_2.pendown()
        t = random.choice(die)
        die_2 = input("Ankit's turn. Type 'roll' for rolling die : ")
        if die_2 == 'roll':
            print("Die showed {}".format(t))
            player_2.fd(5*t)
        else:
            print('INvalid response.')
        if player_2.pos() >= (100,200):
            print('Ankit WON!')
            break
        else:
            player_2.penup()
