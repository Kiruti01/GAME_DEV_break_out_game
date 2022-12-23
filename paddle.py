from turtle import Turtle
from screen_pars import *

STEP = 60
W = 1  # width factor, 20px
L = [8, 5]  # length factor, 160px , 120px

PADDLE_W = W * 20
POSITION = (PADDLE_X, PADDLE_Y)  # (0,-250)

RIGHT_BORDER = WIN_WIDTH / 2 - 10
LEFT_BORDER = -1 * RIGHT_BORDER


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape('square')
        self.color('indigo')
        self.reset()

# reset paddle shape and position
    def reset(self):
        self.goto(POSITION)
        self.shapesize(stretch_wid=W, stretch_len=L[0])
        self.paddle_l = L[0] * 20
        self.is_pause = False

# set paddle state 
    def pause(self, is_paused):
        self.is_pause = is_paused

#  move paddle left with key press
    def go_left(self):
        if not self.is_pause:
            edge = self.xcor() - self.paddle_l / 2
            if edge > LEFT_BORDER:
                self.bk(STEP)

#  move paddle right with key press
    def go_right(self):
        if not self.is_pause:
            edge = self.xcor() + self.paddle_l / 2
            if edge < RIGHT_BORDER:
                self.fd(STEP)

                
# move paddle with mouse click & drag. y cor is constant
    def mouse_drag(self, x, y):
        y = PADDLE_Y
        if not self.is_pause:
            # self.ondrag(None)
            edge_l = LEFT_BORDER + self.paddle_l / 2
            edge_r = RIGHT_BORDER - self.paddle_l / 2
            if x < edge_l:
                self.goto(edge_l, y)
            elif x > edge_r:
                self.goto(edge_r, y)
            else:
                self.goto(x, y)
            # self.ondrag(self.mouse_drag)

# maximal distance hit on the paddle middle
    def max_dis_mid(self):
        return int(((self.paddle_l // 2 - 20) ** 2 + (PADDLE_W // 2 + 10) ** 2) ** 0.5)

#  maximal distance hit on the paddle corner 
    def max_dis_cor(self):
        return int(((self.paddle_l // 2 + 10) ** 2 + (PADDLE_W // 2 + 10) ** 2) ** 0.5)

# resize paddle for level 2 
    def resize(self):
        self.shapesize(stretch_wid=W, stretch_len=L[1])
        self.paddle_l = L[1] * 20
        self.goto(POSITION)
