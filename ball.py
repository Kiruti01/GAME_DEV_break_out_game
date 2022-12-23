from turtle import Turtle
from screen_pars import *
from random import choice

STEP = 20
Y_POS = PADDLE_Y + 22

UP = 90  # or -270 north
DOWN = 270  # or -90 south
RIGHT = 0  # or 360 east
LEFT = 180  # or -180 west
UP_RIGHT = 45  # or -315 north east
DOWN_RIGHT = -45  # or 315  south east
UP_LEFT = 135  # or -225 north west
DOWN_LEFT = -135  # or 225 south west


# initializing Ball object
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape('circle')
        self.color('white')
        self.reset(0, 1)

#reset ball position & speed 
    def reset(self, x, level):
        self.head_start()
        self.goto(x, Y_POS)
        if level == 1:
            self.move_speed = 0.08
        else:
            self.move_speed *= 0.9

            
# set random inital ball direction
    def head_start(self):
        heading = choice([UP_RIGHT, UP_LEFT])
        self.setheading(heading)

    def move(self):
        ''' move ball '''
        self.fd(STEP)

# bounce ball off of  top wall / paddle middle / bricks
    def bounce_top_bottom(self):
        self.setheading(-1 * self.heading())

# bounce ball off of side walls
    def bounce_sides(self):
        self.setheading(180 - self.heading())

        
# bounce ball off of paddle corners
    def bounce_corners(self):
        self.setheading(self.heading() - 180)

# returns ball speed
    def get_speed(self):
        return self.move_speed
