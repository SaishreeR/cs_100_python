"""
Saishree Ramkumar 
CS 100 Room CKB 207
HW 4 Excercise 1 25 Feb 2024 11:01 pm est
"""

# Importing package

print("***Q1***")
#Storing the months
lstMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def search_month_element (lstMonths):
    for strlistVal in lstMonths:
        #print(strlistVal[0:1])
        if strlistVal[0:1].upper()== 'J':
            print("Month that start with letter J are: " + strlistVal)
# Calling the function    
search_month_element(lstMonths)

print("***Q2***")
def find_division (intRange):
    for intRIndex in range(intRange):
        #print("Reminders after dividing by 2: " + str(intRIndex%2))
        #print("Reminders after dividing by 5: " + str(intRIndex%5))
        if ((intRIndex%2 == 0) and (intRIndex%5 == 0)):
            print("Number that are divisible by both 2 & 5: " + str(intRIndex))
find_division (100)

print("***Q3***")
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
# Function to find the vowels from horton
def find_vowels (strInput):
    for strHIndex in horton:
        for strVIndex in vowels:
            if (strHIndex == strVIndex):
                print("Vowels from Horton: " + strHIndex)
            #else:
                #print(strHIndex + " is not a vowel")
            
# Calling the function
find_vowels(horton)
