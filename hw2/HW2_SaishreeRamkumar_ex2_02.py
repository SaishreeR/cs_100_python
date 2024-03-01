"""
Saishree Ramkumar 
CS 100 Room CKB 207
HW 2 Excercise 2, 23 Feb 2024 5:37 pm est
"""
# Importing packaging
import turtle
      
tDrawCircle = turtle.Turtle() 
  
# Setting the radius of the circle 
intRadius = 50
  
# For loop for drawing concentric circles 
for intIndex in range(5): 
    tDrawCircle.circle(intRadius * intIndex) 
    tDrawCircle.up() 
    tDrawCircle.sety((intRadius * intIndex)*(-1)) 
    tDrawCircle.down()
   


