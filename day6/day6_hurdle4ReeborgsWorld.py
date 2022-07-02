# https://reeborg.ca/reeborg.html

# Functions defined in the Reeborg's Library
def move():
    return


def turn_left():
    return


# Functions built by the programmer
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def get_through():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for i in range(6):
    get_through()
