from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        

        self.color("white")
        self.penup()
        self.goto(0, - 400)
        self.setheading(90)
        self.pensize(3)
        for i in range(100):
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)