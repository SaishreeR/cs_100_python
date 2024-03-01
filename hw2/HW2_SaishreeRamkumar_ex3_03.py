"""
Saishree Ramkumar 
CS 100 Room CKB 207
HW 2 Excercise 3, 23 Feb 2024 5:50 pm est
"""
# Importing packaging
import math

intFactInput = 100
     
# Computing factorial
intOutput = math.factorial(intFactInput)
print("The factorial of 100 is : " + str(intOutput))

intArgument = 1000000
intLogOutput = math.log2(intArgument)
print ("The log(base 2) of 1000000 is : " + str(intLogOutput))


intGcfInput1 = 63
intGcfInput2 = 49
intGcfOutput = math.gcd(intGcfInput1, intGcfInput2)
print ("Greatest Common Factor of 63 & 49 is " + str(intGcfOutput))