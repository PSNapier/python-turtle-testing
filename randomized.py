# IMPORTS
# normally I lay out my imports in the order they are used, but it is popular to lay them out alphabetically
import turtle
import random

# GLOBAL VARIABLES
WIDTH, HEIGHT = 700, 600  # for window size
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
TURTLE_COUNT = 3


# FUNCTIONS
# function to take in window size and return a coordinate with that range as a tuple[int, int]
def random_coords(width, height):
    coords = random.randint(0, width), random.randint(0, height)

    return coords


# function to create turtle a turtle with random color and starting location
def create_turt(colors):
    turt = turtle.Turtle()

    # initial setup
    turt.hideturtle()  # using this temp hide so that it doesn't flash on screen before it's ready
    turt.shape('circle')
    turt.color(random.choice(colors))

    # randomize starting location
    turt.speed(20)
    turt.penup()
    turt.goto(create_destination())

    # setup for how it will move during run_turt()
    turt.speed(2)
    turt.showturtle()
    turt.pendown()

    return turt


# function to return destination
def create_destination():
    destination = random_coords(WIDTH, HEIGHT)

    return destination


# function to move turtle to multiple randomized locations
def run_turt(turt):
    turt.goto(create_destination())
    turt.goto(create_destination())
    turt.goto(create_destination())


# DO THE DO
# window setup
screen = turtle.Screen()
turtle.screensize(WIDTH, HEIGHT)
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
screen.title('Turtle Test')

# run x amount of times and wait for click to exit
for x in range(TURTLE_COUNT):
    run_turt(create_turt(COLORS))
screen.exitonclick()
