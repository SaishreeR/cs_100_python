"""
Saishree Ramkumar 
CS 100 Room CKB 207
HW 3 Excercise 1, 2, & 3, 23 Feb 2024 6:09 pm est
"""

# Importing package
import math
import turtle

print("***** Q1 *****")
# Setting variables
a = 3
b = 4
c = 5

#Validation
if(a < b):
    print("OK")
    
if(c < b):
    print("OK")
    
if(a + b == c):
    print("OK")
    
if(math.sqrt(a)+math.sqrt(b) == math.sqrt(c)):
    print("OK")
    
print("***** Q2 *****")   
if(a < b):
    print("OK")
else:
    print("NOT OK")
    
if(c < b):
    print("OK")
else:
    print("NOT OK")
    
if(a + b == c):
    print("OK")
else:
    print("NOT OK")
    
if(math.sqrt(a)+math.sqrt(b) == math.sqrt(c)):
    print("OK")
else:
    print("NOT OK")
    

print("***** Q3 *****")

strColorValue = input("What is the color: (eg black)")
print("Color  is: " + strColorValue)
strLineWidthValue = input("What is the line width (in numbers)?")
print("Line Width  is: " + strLineWidthValue)
strLineLengthValue = input("What is the line length (in numbers)?")
print("Line Length  is: " + strLineLengthValue)
strShapeValue= input("What is the shape? Type line, triangle or square:")



# Function to create Square
def draw_square (intRange,intLineLengthValue,strColor, intWidth):
    intSize = 100
    intSqAngle = 90
    # Setting up turtle properties
    tSquare = turtle.Turtle()
    tSquare.penup()
    tSquare.goto (100, 150)
    tSquare.pendown()
    tSquare.color(strColor)
    tSquare.width(intWidth)
    for intLenght in range(intRange):
        tSquare.forward(intLineLengthValue)
        tSquare.right(intSqAngle)
        

# Function to create Eq Triangle
def draw_eqTriangle (intRange,intLineLengthValue,strColor, intWidth):
    intSize = 100
    intTrAngle = 120
    # Setting up turtle properties
    tEqTriangle = turtle.Turtle()
    tEqTriangle.color(strColor)
    tEqTriangle.width(intWidth)
    for intLenght in range(intRange):
        tEqTriangle.forward(intLineLengthValue)
        tEqTriangle.right(intTrAngle)
        
        
if(strShapeValue.lower() == 'line'):
    print("Shape is: " + strShapeValue)
    tDrawShape = turtle.Turtle()
    tDrawShape.penup()
    tDrawShape.goto (100, 150)
    tDrawShape.pendown()
    tDrawShape.color(strColorValue)
    tDrawShape.width(int(strLineWidthValue))
    tDrawShape.forward(int(strLineLengthValue))

if(strShapeValue.lower()=='triangle'):
    print("Shape is: " + strShapeValue)
    draw_eqTriangle(3,int(strLineLengthValue), strColorValue, int(strLineWidthValue))
    
if(strShapeValue.lower()=='square'):
    print("Shape is: " + strShapeValue)
    draw_square(4,int(strLineLengthValue), strColorValue, int(strLineWidthValue))
