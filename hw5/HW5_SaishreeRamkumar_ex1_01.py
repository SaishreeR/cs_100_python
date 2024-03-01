"""
Saishree Ramkumar 
CS 100 Room CKB 207
HW 5 Excercise 1 29 Feb 2024 9:20 pm est
"""

# Importing package

inputLetter1 = 'R'
inputLetter2 = 's'
inputLetter3 = ''
lst1 = ['A', 'B', 'C', 'F']
lst2 = ['a', 'b', 'c', 'h']
lst3 = []

print("***Q1***")
def hasFinalLetter(strList, letters):
    strList.append(letters)
    print("List of all the strings adding letters: ")
    print(strList)
print("***Q1-a***")    
hasFinalLetter(lst1, inputLetter1)
print("***Q1-b***")
hasFinalLetter(lst2, inputLetter2)
hasFinalLetter(lst3, inputLetter3)
        
