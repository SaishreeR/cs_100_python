"""
Saishree Ramkumar 
CS 100 Room CKB 207
HW 2 Excercise 1, 21 Feb 2024 10:17 pm est
"""
# Importing packaging
import turtle

# Variable declaration
intEqTrRange = 3
intSqRange = 4
intPtgRange = 5


# Function to create Eq Triangle
def draw_eqTriangle (intRange):
    intSize = 100
    intTrAngle = 120
    strColor = 'orange'
    intWidth = 10
    # Setting up turtle properties
    tEqTriangle = turtle.Turtle()
    tEqTriangle.color(strColor)
    tEqTriangle.width(intWidth)
    for intLenght in range(intRange):
        tEqTriangle.forward(intSize)
        tEqTriangle.right(intTrAngle)

# Function to create Square
def draw_square (intRange):
    intSize = 100
    intSqAngle = 90
    strColor = 'green'
    intWidth = 10
    # Setting up turtle properties
    tSquare = turtle.Turtle()
    tSquare.penup()
    tSquare.goto (100, 150)
    tSquare.pendown()
    tSquare.color(strColor)
    tSquare.width(intWidth)
    for intLenght in range(intRange):
        tSquare.forward(intSize)
        tSquare.right(intSqAngle)
        
# Function to create Pentagon
def draw_pentagon (intRange):
    intSize = 100
    intPtgAngle = 72
    strColor = 'purple'
    intWidth = 10
    # Setting up turtle properties
    tPtg = turtle.Turtle()
    tPtg.penup()
    tPtg.goto (-100, 150)
    tPtg.pendown()
    tPtg.color(strColor)
    tPtg.width(intWidth)
    for intLenght in range(intRange):
        tPtg.forward(intSize)
        tPtg.right(intPtgAngle)
        
        
# Calling functions
draw_eqTriangle(intEqTrRange)
draw_square(intSqRange)
draw_pentagon(intPtgRange)



