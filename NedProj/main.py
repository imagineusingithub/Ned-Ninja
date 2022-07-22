
import turtle
import time
import random
import math
import os
import atexit

def exit_handler():
    os.system("pkill aplay")

atexit.register(exit_handler)

file="levelonestagemusic.wav"
os.system("aplay "+file+" &")

deathcount = 0

pen = turtle.Turtle()
pen.color("black")
pen.hideturtle()

def deathcounter():
    pen.goto(0,250)
    pen.clear()
    pen.write("Deaths: {}"
              .format(deathcount),
              align="center",
              font=("Dreamscar", 24, "bold"))





level = 1

bgs = [ "stagezero.gif", "stageone.gif","stagetwo.gif", "stagezero.gif", "stagefour.gif"]

screen=turtle.Screen()
screen.title("Ninja Ned")
screen.bgcolor("dodgerblue")
screen.bgpic(bgs[0])

screen.setup(width=960, height=600)
screen.tracer(0)

ned=turtle.Turtle()
screen.addshape("ned.gif")
ned.shape("ned.gif")
ned.penup()
ned.goto(-450, -150)
x = ned.xcor()
y = ned.ycor()
ned.vy = 0
ned.vx = 0

turtles = []

def checkwalls():
    global y, x, level
    x=ned.xcor()
    y=ned.ycor()
    if x<-450:
        ned.goto(ned.xcor()-ned.vx, ned.ycor())
        ned.vx = 0
    if x > 450:
        if level < len(bgs):
            ned.goto(-450, -150)
            level+=1
            screen.bgpic(bgs[level-1])
            drawlevel(level)
        else:
            ned.goto(ned.xcor() - ned.vx, ned.ycor())
            ned.vx = 0
    if y>300 or y <-300:
        resetgame()

def drawlevel(level):
    global turtles

    for turt in turtles:
        turt.goto(5000,5000)
    turtles = []
    if level == 3:
        turtles.append(turtle.Turtle())
        turtles[0].penup()
        turtles[0].goto(50, -150)
        turtles[0].shape("square")
        turtles[0].color("lime")
    if level == 4:
        os.system("pkill aplay")
        os.system("aplay leveltwostagemusic.wav &")
    if level == 5:
        turtles.append(turtle.Turtle())
        turtles[0].penup()
        turtles[0].goto(80, -156)
        turtles[0].shape("square")
        turtles[0].color("lime")

def resetgame():
    global score, delay, segments,level, deathcount
    time.sleep(1)
    score=0
    delay=0.025
    ned.goto(-450, -150)
    level=1
    screen.bgpic(bgs[level-1])
    drawlevel(level)
    deathcount+=1
    os.system("pkill aplay")
    os.system("aplay " + file + " &")

def checkenemies():
    for turt in turtles:
        if ned.distance( turt )<10:
            resetgame()

ned.timer=0
ned.vy=0
ned.xy=0
inair= True

def floor():
    global inair
    x = round((ned.xcor()+480)/38)
    if ned.ycor() > ta[level-1][x]:
        inair = True
    elif ned.ycor() < ta[level-1][x]:
        inair = False
        ned.sety(ta[level-1][x])

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
    ned.vx = 10

def nedl():
    x = ned.xcor()
    ned.vx = -10

def nedrs():
    x = ned.xcor()
    ned.vx = 0

def nedls():
    x = ned.xcor()
    ned.vx = 0

def nedj():
    global y, inair
    if not inair:
        inair=True
        y = ned.ycor()
        ned.vy = 10

screen1 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

ta = [[-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156],
     [-196,-196,-196,-196,-196,-196,-156,-300,-300,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156],
     [-196,-196,-196,-196,-196,-196,-156,-300,-156,-300,-156,-156,-300,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156,-156],
      [-156,-156,-156,-156,-156,-156,-156,-156,-156,-300,-156,-156,-156,-156,-156,-156,-156,-300,-156,-156,-156,-156,-300,-156,-156,-156,-156,-156,-156],
      [-196,-196,-196,-196,-196,-196,-156,-300,-156,-300,-156,-300,-300,-300,-156,-156,-300,-300,-300,-300,-156,-156,-156,-156,-156,-156,-156,-156,-156]]

jumptiles = []
walltiles = []
rendered = []

def render(screen):
    rendererY = 365
    rendererX = -520
    for i in screen:
        rendererY -= 40
        rendererX = -540
        for j in i:
            rendererX += 40
            if j == 1:
                grass = turtle.Turtle()
                grass.penup()
                grass.color("green")
                grass.turtlesize(2)
                grass.shape("square")
                grass.goto(-480,365)

screen.listen()
screen.onkeypress(nedr, 'd')
screen.onkeyrelease(nedrs, 'd')
screen.onkeypress(nedl, 'a')
screen.onkeyrelease(nedls, 'a')
screen.onkeypress(nedj, 'w')

#render(screen1)

def updategame():
    global x, y, inair, turtles
    x = ned.xcor()
    y = ned.ycor()
    if not y < ta[level-1][round((x+ned.vx+480)/38)]:
        ned.setpos(x + ned.vx, y + ned.vy)
    checkwalls()
    deathcounter()
    checkenemies()
    dograv = True
    for turtle in turtles:
        if ned.distance(turtle) < 30:
            if y > turtle.ycor():
                inair = False
                dograv = False
                ned.vy = 0
                print("inarea")
                turtle.goto(5000, 5000)
                ned.sety(turtle.ycor()+30)
            break
    if dograv:
        floor()
        physics()



    screen.update()
    screen.ontimer(updategame, 30)

screen.ontimer(updategame, 30)
screen.mainloop()
