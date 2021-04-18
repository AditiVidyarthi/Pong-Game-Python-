import turtle as t
playerAscore=0
playerBscore=0
speed=0
start=False

#preparing screen
scrn=t.Screen()
scrn.bgcolor("black")
scrn.title("Pong Game")
scrn.setup(width=800,height=600)
scrn.tracer(0)

#create left paddle
left_paddle=t.Turtle()
left_paddle.color("cyan")
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350,0)

#create rightpaddle
right_paddle=t.Turtle()
right_paddle.color("cyan")
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(350,0)

#creating ball
ball=t.Turtle()
ball.shape("circle")
ball.color("white")
ball.pu()
ball.goto(0,0)
ballxdirection=0.2
ballydirection=0.2

#starting message
draw=t.Turtle()
draw.speed(0)
draw.color("cyan")
draw.width(4)
draw.pu()
draw.goto(-300,200)
draw.pd()
for i in range (2):
    draw.fd(600)
    draw.right(90)
    draw.fd(400)
    draw.right(90)
draw.pu()
draw.goto(0,150)
draw.write("Let's Play",align="center",font=("Times New Roman",30,"bold"))
draw.goto(0,100)
draw.write("Player A                   Player B",align="center",font=("Times New Roman",24,"bold"))
draw.goto(-250,40)
draw.write(" W :  Move Up               UP : Move Up",align="left",font=("Times New Roman",22,"normal "))
draw.goto(-250,10)
draw.write(" S :  Move Down            Down : Move Down",align="left",font=("Times New Roman",22,"normal "))
draw.goto(0,-50)
draw.write("Speed : increase Y    decrease H",align="center",font=("Times New Roman",22,"normal"))
draw.goto(0,-80)
draw.write("Play/Pause : P",align="center",font=("Times New Roman",22,"normal"))
draw.goto(0,-150)
draw.write("Go Buddy (P)",align="center",font=("Times New Roman",30,"bold"))
draw.hideturtle()

pen=t.Turtle()
pen.speed(0)
pen.color("lightgreen")
pen.width(4)
pen.pu()
pen.hideturtle()
#creating scoreboard
def game_on():
    global start
    if start==False:
        global draw
        draw.clear()
        draw.color("lightgreen")
        draw.pu()
        draw.goto(0,290)
        draw.write("Score",align="center",font=("Arial",30,"normal "))

        global pen
        pen.goto(0,250)
        pen.write("Player A:{}       Player B:{}".format(playerAscore,playerBscore),align="center",font=("Arial",30,"normal "))
        start=True
    else:        
        global speed
        if speed != 0:
            speed = 0
        else:
            speed = 1


#move left paddle
def left_paddle_up():
    y=left_paddle.ycor()
    y=y+90
    left_paddle.sety(y)

def left_paddle_down():
    y=left_paddle.ycor()
    y=y-90
    left_paddle.sety(y)


#move right paddle
def right_paddle_up():
    y=right_paddle.ycor()
    y=y+90
    right_paddle.sety(y)

def right_paddle_down():
    y=right_paddle.ycor()
    y=y-90
    right_paddle.sety(y)

#upgrading speed
def speed_increase():
    global speed
    if speed<4:
        speed+=1

def speed_decrease():
    global speed
    if speed>0:
        speed-=1

    
#Asign keys
scrn.listen()
scrn.onkeypress(left_paddle_up,"w")
scrn.onkeypress(left_paddle_down,"s")
scrn.onkeypress(right_paddle_up,"Up")
scrn.onkeypress(right_paddle_down,"Down")
scrn.onkeypress(speed_increase,"y")
scrn.onkeypress(speed_decrease,"h")
scrn.onkeypress(game_on,"p")

while (playerAscore<10)and(playerBscore<10):
    scrn.update()
    #setting boundaries for paddles
    if left_paddle.ycor()>250:
        left_paddle.sety(250)
    if left_paddle.ycor()<-250:
        left_paddle.sety(-250)
    if right_paddle.ycor()>250:
        right_paddle.sety(250)
    if right_paddle.ycor()<-250:
        right_paddle.sety(-250)
    

    ball.setx(ball.xcor()+ballxdirection*speed)
    ball.sety(ball.ycor()+ballydirection*speed)
    #setting boundaries for ball
    if (ball.ycor()>250):
        ball.sety(250)
        ball.right(90)
        ballydirection=ballydirection*-1
    if (ball.ycor()<-250):
        ball.sety(-250)
        ball.right(90)
        ballydirection=ballydirection*-1
    if (ball.xcor()>350):
        ball.goto(0,0)
        ballxdirection=ballxdirection
        playerAscore=playerAscore+1
        pen.clear()
        pen.write("Player A:{}       Player B:{}".format(playerAscore,playerBscore),align="center",font=("Arial",30,"normal "))

    if (ball.xcor()<-350):
        ball.goto(0,0)
        ballxdirection=ballxdirection
        playerBscore=playerBscore+1
        pen.clear()
        pen.write("Player A:{}       Player B:{}".format(playerAscore,playerBscore),align="center",font=("Arial",30,"normal "))

    #collisions with ball
    if (ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<right_paddle.ycor()+50)and(ball.ycor()>right_paddle.ycor()-50):
        ball.setx(340)
        ballxdirection=ballxdirection*-1
    if (ball.xcor()<-340)and(ball.xcor()>-350)and(ball.ycor()<left_paddle.ycor()+50)and(ball.ycor()>left_paddle.ycor()-50):
        ball.setx(-340)
        ballxdirection=ballxdirection*-1

ball.hideturtle()
pen.up()
pen.goto(0,0)
pen.down()
if (playerAscore==10):
    pen.write("PlayerA wins",align="center",font=("Arial",30,"normal "))
else:
    pen.write("PlayerB wins",align="center",font=("Arial",30,"normal "))



