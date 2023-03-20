import turtle
WINDOW = turtle.getscreen
DEFAULT_LENGTH = 5
DEFAULT_START_POS = (0,100)
DEFAULT_MOVE_LENGTH = 25 #length turtle moves on default between revolutions
DEFAULT_ROTATION = 15
t = turtle.Turtle(shape="turtle", visible=False)
def prompts():
    '''
    This function prompts other functions and 
    saves return values as variables.
    No arguments.
    Returns = None.
    '''
    spikiness1 = spikiness()
    revolutions1 = revolutions()
    scale1 = scale()
    make_shape(spikiness1,revolutions1,scale1)
def spikiness():
    '''
    This function prompts user input for
    how spiky the spirograph should be
    and ensures current parameters.
    No arguments.
    Returns = INT spikiness1
    '''
    spikiness1 = int(input("How spiky would you like your graph? Enter a number between 20 and 65."))
    if spikiness1 < 20 or spikiness1 > 65:
        while spikiness1 < 20 or spikiness1 > 65:
            print("Your answer was invalid. Please try again.")
            spikiness1 = int(input("How spiky would you like your graph? Enter a number between 20 and 65."))
    return spikiness1
def revolutions():
    '''
    This function prompts user input for
    how many revolutions the turtle should
    make and ensures current parameters.
    No arguments.
    Returns = INT revolutions1
    '''
    revolutions1 = int(input("How many revolutions would you like to make on your spirograph? (I recommend at least 25 for most spirographs.)"))
    if revolutions1 < 1:
        while revolutions1 <1:
            print("Your answer was invalid. Please try again.")
            revolutions1 = int(input("How many revolutions would you like to make on your spirograph? (I recommend at least 25 for most spirographs.)"))
    return revolutions1
def scale():
    '''
    This function prompts user input for
    how big the spirograph should be
    and ensures current parameters.
    No arguments.
    Returns = INT scale1
    '''
    scale1 = int(input("How big would you like your spirograph? Enter a number between 1 and 7."))
    if scale1 < 1 or scale1 > 7:
        while scale1 < 1 or scale1 > 7:
            print("Your answer was invalid. Please try again.")
            scale1 = int(input("How big would you like your spirograph? Enter a number between 1 and 7."))
    return scale1
def rotate_and_draw(spikiness, scale):
    '''
    This function performs each revolution
    of the spirograph.
    Arguments are all INT: spikiness and scale gathered from
    user input in prompts() and carried over by
    make_shape().
    Returns = None.
    '''
    t.color("green","green")
    t.showturtle()
    t.pendown()
    turn = 0
    number_needed = 180/spikiness
    #the number of rotations needed to make 180 degrees
    while turn < number_needed:
        t.rt(spikiness)
        t.fd(DEFAULT_LENGTH*scale)
        turn += 1
def make_shape(spikiness,revolutions,scale):
    '''
    This function begins and ends the drawing
    as well as carries over values of variables
    from prompts() to rotate_and_draw().
    Arguments are all INT: spikiness, revolutions, and scale from 
    user input in prompts().
    Returns = None
    '''
    count = 0
    while count < revolutions:
        t.rt(DEFAULT_ROTATION)
        t.fd(DEFAULT_MOVE_LENGTH*scale)
        rotate_and_draw(spikiness, scale)
        t.fd(DEFAULT_MOVE_LENGTH*scale)
        count += 1
def main():
    t.penup()
    t.setpos(DEFAULT_START_POS)
    turtle.title("Spirograph")
    prompts()
    turtle.exitonclick()
main()