import turtle
window = turtle.getscreen
sides = int(input("number of sides?"))
length = int(input("length?"))
t = turtle.Turtle()
turtle.color("pink")
turtle.get_shapepoly()
angles = 360/sides
def make_shape(x):
    d = 0
    while d < x:
        t.fd(length)
        t.rt(angles)
        d+=1
make_shape(sides)
turtle.exitonclick()