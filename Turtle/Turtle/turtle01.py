import turtle
import time
"""


def expPen():
        turtle=Turtle()   # IN module turtle :->Pen = class Turtle(RawTurtle)
        #turtle=Pen()
        color("black", "red")
        begin_fill()
        circle(60)
        end_fill()
        forward(25)
"""
"""
classTurtle1:-
        begin_fill,end_fill
        clear
        color
        circle
classTurtle2:
        #turtle arrow Sign Called as Stamp 
        clearstamp(stampid),stamp()
classTurtle3:
        clearstamps(n=None),stamp()
classTurtle4:
        dot(self, size=None, *color)
classTurtle5:
        filling(self)     #Return fillstate (True if filling, False else).

"""
'''
reaction due
        begin_poly()
        end_poly()
        getpen = getturtle(self)
'''
def classTurtle1():
        tr=turtle.Pen(shape='classic', undobuffersize=1000, visible=False)
        tr.color("black", "red")
        tr.begin_fill()
        tr.circle(60)
        tr.end_fill()
        tr.clear()
def classTurtle2():
        tr=turtle.Pen(shape='classic', undobuffersize=1000, visible=True)
        tr.color("blue")
        astamp = tr.stamp()
        tr.fd(50)
        tr.clearstamp(astamp)
def classTurtle3():
        tr=turtle.Pen(shape='classic', undobuffersize=1000, visible=True)
        for i in range(8):
                tr.stamp()
                tr.fd(30)
        tr.clearstamps(2)
        tr.clearstamps(-2)
        #tr.clearstamps()

def classTurtle4():
        tr=turtle.Pen(shape='classic', undobuffersize=1000, visible=True)
        tr.dot()
        tr.fd(50)
        tr.dot(20, "blue")
        tr.fd(50)
def classTurtle5():
        tr=turtle.Pen(shape='classic', undobuffersize=1000, visible=True)
        turtle.begin_fill()
        if turtle.filling():
             turtle.pensize(5)
        else:
             turtle.pensize(3)
def classTurtle6():
        tr1=turtle.Pen(shape='classic', undobuffersize=1000, visible=True)
        p = tr1.get_poly()
        print(p)

def classTurtle9():
        tr1=turtle.Pen(shape='classic', undobuffersize=1000, visible=True)
        tr1.shape("square")     #'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
        #tr1.shapetransform(4, -1, 0, 2)
        tr1.get_shapepoly()
def classTurtle6():
        tr1=turtle.Pen(shape='classic', undobuffersize=1000, visible=True)
        pet = getturtle()
        pet.fd(50)
        pet
        turtles()
        tr1.get_shapepoly()
def classTurtle6():
        tr1=turtle.Pen(shape='classic', undobuffersize=1000, visible=True)
        ts = tr1.getscreen()
        ts.bgcolor("pink")
        print(ts)
class MyTurtle(turtle.Pen):
     def glow(self,x,y):
             self.fillcolor("red")
     def unglow(self,x,y):
             self.fillcolor("")
             
def classTurtle6():
        joe = MyTurtle()
        joe.onclick(joe.glow)
        joe.onrelease(joe.unglow)
        joe.ondrag(turtle.goto)

def classTurtle6():
        tr1=turtle.Pen(shape='classic', undobuffersize=1000, visible=True)
        print(tr1.position(45,56))
        print(tr1.heading())
        print(tr1.reset())
        print(tr1.position())
        print(tr1.heading())




def main():
        classTurtle9()
if __name__ == '__main__':
    main()
