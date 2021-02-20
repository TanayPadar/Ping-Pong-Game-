#========================Ping-Pong Game===============================

#Import Module
import turtle as t

# Score variables
player_a_score = 0
player_b_score = 0

# Creating Box
win = t.Screen()   
win.title("Ping-Pong Game by JP") 
win.bgcolor('grey12')    
win.setup(width=800,height=600) 
win.tracer(0)   

# Creating left paddle 
paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.shapesize(stretch_wid=7,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

# Creating a right paddle 
paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=7,stretch_len=1)
paddle_right.color('white')
paddle_right.penup()
paddle_right.goto(350,0)

# Creating a Ball
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball_dx = 1.5   
ball_dy = 1.5

# Updating Score
pen = t.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0 ",align="center",font=('Comic Sans',25,"italic"))


# Moving the left Paddle up
def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)

# Moving the left paddle down
def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 15
    paddle_left.sety(y)

# Moving the right paddle up
def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)

# Moving right paddle down
def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 15
    paddle_right.sety(y)

# Keyboard binding
win.listen()
win.onkeypress(paddle_left_up,"Right")
win.onkeypress(paddle_left_down,"Left")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")

# Main Game Loop
while True:
    win.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

     # Right top paddle Border
    if ball.ycor() > 290:   
        ball.sety(290)
        ball_dy = ball_dy * -1
        
     # Left top paddle Border
    if ball.ycor() < -290:  
        ball.sety(-290)
        ball_dy = ball_dy * -1
        
     # right width paddle Border
    if ball.xcor() > 390:   
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Comic Sans',25,"italic"))

     # Left width paddle border
    if (ball.xcor()) < -390:  
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Comic Sans',25,"italic"))

     # Handling the collisions with paddles.
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        




