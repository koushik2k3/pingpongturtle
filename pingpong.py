import turtle
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor("pink")

mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
    
p1=turtle.Turtle()
shape =((0, 0), (50, 0), (50, 10), (0,10))
turtle.register_shape('player',shape)
p1.shape('player')
p1.up()
p1.goto(-190,0)

ball=turtle.Turtle()
ball.color('white')
ball.shape('circle')
ball.up()

speedx=-10
speedy=1
y1=0
y2=0
t=0
s=0
def up1():
    global t
    t=t+10
def down1():
    global t
    t=t-10

turtle.listen()
turtle.onkey(up1, "Up")
turtle.onkey(down1, "Down")

p2=turtle.Turtle()
p2.shape('player')
p2.up()
p2.goto(190,0)

def up2():
    global s
    s=s+10
def down2():
    global s
    s=s-10
flag=0
turtle.listen()
turtle.onkey(up2, "w")
turtle.onkey(down2, "s")

print('start')
while True:
    if flag==1:
        p1.goto(-190,0)
        p2.goto(190,0)
        ball.goto(0,0)
        t=0
        s=0
        flag=0
    p1.goto(-190,y1+t)
    p2.goto(190,y2+s)
    ball.setx(ball.xcor()+speedx)
    ball.sety(ball.ycor()+speedy)
    if ball.xcor()in range(p1.xcor()-10,p1.xcor()+10) and ball.ycor()in range(p1.ycor()-50,p1.ycor()+50):
        if ball.ycor()in range(p1.ycor(),p1.ycor()+25):
            speedx=speedx*-1
            speedy=speedy*-1
            continue
        speedx=speedx*-1   
    if ball.xcor()in range(p2.xcor()-5,p2.xcor()+5) and ball.ycor()in range(p2.ycor()-25,p2.ycor()+25):
        if ball.ycor()in range(p2.ycor(),p2.ycor()+25):
            speedx=speedx*-1
            speedy=speedy*-1
            continue
        speedx=speedx*-1
    elif ball.ycor()>290 or ball.ycor()<-290:
        speedy=speedy*-1

    elif ball.xcor()>290 or ball.xcor()<-290:
        flag=1
        print('restart')
        continue
done()