import turtle
import time
import random
import math

delay=0.025
deathcounter=0

screen=turtle.Screen()
screen.title("Ninja Ned")
screen.bgcolor("deepskyblue")

screen.setup(width=1920, height=1080)
screen.tracer(0)

ned=turtle.Turtle()
screen.addshape("ned.gif")
ned.shape("ned.gif")
ned.penup()
ned.goto(0, -520)
x = ned.xcor()
y = ned.ycor()
ned.vy = 0
ned.vx = 0


def checkwalls():
    global y, x
    x=ned.xcor()
    y=ned.ycor()
    if x>900 or x<-900:
        resetgame()
    if y>540 or y <-550:
        resetgame()



def resetgame():
    global score, delay, segments
    time.sleep(1)
    ned.goto(0, -520)
    score=0
    delay=0.025


ned.vy=0
inair= True

def floor():
    if ned.ycor() < -520:
        inair = False
        ned.sety(-520)



def physics():
    global y
    y = ned.ycor()
    if inair==True:
        ned.vy-=1
    if inair==False:
        ned.vy = 0
    ned.sety(y+ned.vy)

def nedr():
    x = ned.xcor()
    ned.setx(ned.xcor() + 20)

def nedl():
    print("eijhrsio")
    x = ned.xcor()
    ned.setx(ned.xcor() - 20)

def nedj():
    global y
    y = ned.ycor()
    ned.vy = 15
    ned.sety(y+ned.vy)






screen.listen()
screen.onkeypress(nedr, 'd')
screen.onkeypress(nedl, 'a')
screen.onkeypress(nedj, 'w')




while True:
    screen.update()
    checkwalls()
    physics()
    floor()
    time.sleep(delay)
screen.mainloop()