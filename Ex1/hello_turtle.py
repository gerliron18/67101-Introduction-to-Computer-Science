#############################################################
# FILE : hello_turtle.py
# WRITER : Liron Gershuny , gerliron18 , 308350503
# EXERCISE : intro2cs ex1 2017-2018
# DESCRIPTION: A program that print three flowers to
# the standard output (screen).
#############################################################
import turtle


def draw_petal():
    """This function draw a one flower petal"""
    turtle.down()
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_flower():
    """This function draw one flower"""
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)


def draw_flower_advanced():
    """This function draw one flower and then change
    the position of the turtle head so you can draw
    another flower"""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    """This function draw three flower's"""
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()


draw_flower_bed()
turtle.done()
