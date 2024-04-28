import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800,650)

bord=turtle.Turtle()
bord.penup()
bord.goto(390,-290)
bord.pendown()
bord.pencolor("White")
bord.speed(0)
for _ in range(2):
    bord.left(90)
    bord.forward(580)
    bord.left(90)
    bord.forward(780)
bord.hideturtle()
bord.penup()

p1score = 0
p2score = 0
score = "Score: "+str(p1score)+" | "+ str(p2score)
bord.setposition(-30,310)
bord.write(score)


p1=turtle.Turtle()
p1.shape("square")
p1.color("white")
p1.penup()
p1.speed(0)
p1.setpos(-350,0)
p1.shapesize(stretch_wid=5, stretch_len=1)

p2=turtle.Turtle()
p2.shape("square")
p2.color("white")
p2.penup()
p2.speed(0)
p2.setpos(350,0)
p2.shapesize(stretch_wid=5, stretch_len=1)

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ballspeed=12

def p1go_up():
    if p1.ycor()<240:
        p1.goto(p1.xcor(),p1.ycor()+40)
def p1go_down():
    if p1.ycor() > -240:
        p1.goto(p1.xcor(),p1.ycor()-40)
def p2go_up():
    if p2.ycor() < 240:
        p2.goto(p2.xcor(),p2.ycor()+40)
def p2go_down():
    if p2.ycor() > -240:
        p2.goto(p2.xcor(),p2.ycor()-40)

def wallcollision(a,y):
    if a <= 180 and a >= 0 and y + 12 >= 290:
        c = - a
        return c
    elif a <= 0 and a >= - 180 and y - 12 <= -290:
        c = - a
        return c
    else: return a

def player1collision(b):
    if b<0:
        return random.randint(-80,-15)
    else:
        return random.randint(15,80)

def player2collision(b):
    if b<0:
        return random.randint(-160,-105)
    else:
        return random.randint(105,160)
def reset():
    p1.sety(0)
    p2.sety(0)
    ball.setposition(0,0)

turtle.listen()
turtle.onkey(p1go_up,"z")
turtle.onkey(p1go_down,"s")
turtle.onkey(p2go_up,"Up")
turtle.onkey(p2go_down,"Down")

dvic=random.randint(-179,179)
ball.setheading(dvic)
while True:
    ball.forward(ballspeed)
    if ball.xcor()+12<390 and ball.xcor()-12>-390 and ball.ycor()+12<290 and ball.ycor()-12>-290:
        if (ball.xcor()-12 < p1.xcor()+10) and (ball.xcor()+12 > p1.xcor()-10) :
            if (ball.ycor()-12 < p1.ycor()+50) and (ball.ycor()+12 > p1.ycor()-50):
                dvic = player1collision(ball.ycor()-p1.ycor())
        elif (ball.xcor() + 12 > p2.xcor() - 10) and (ball.xcor() - 12 < p2.xcor() + 10):
            if (ball.ycor() - 12 < p2.ycor() + 50) and (ball.ycor() + 12 > p2.ycor() - 50):
                dvic = player2collision(ball.ycor()-p2.ycor())
    else:
        if ball.ycor()+12>290 or ball.ycor()-12<-290:
            dvic=wallcollision(dvic,ball.ycor())
        else:
            if ball.xcor()-12<-390:p2score += 1
            elif ball.xcor() + 12 > 390:p1score += 1
            bord.undo()
            score = "Score: " + str(p1score) + " | " + str(p2score)
            bord.write(score)
            reset()
            dvic = random.randint(-179, 179)
    ball.setheading(dvic)
    print(dvic)

turtle.done()
