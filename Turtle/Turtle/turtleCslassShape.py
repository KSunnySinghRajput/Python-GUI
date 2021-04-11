import turtle
import time

def classTurtle():
        tk=turtle.Pen()
        s=turtle.Shape("compound")
        poly = ((0,0),(10,-5),(0,10),(-10,-5))
        s.addcomponent(poly, "red", "blue")
        print(tk.shape())
        tk.shape(poly)
        print(tk.shape())
def main():
        classTurtle()
if __name__ == '__main__':
    main()
