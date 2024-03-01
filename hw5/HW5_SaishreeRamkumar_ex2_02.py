"""
Saishree Ramkumar 
CS 100 Room CKB 207
HW 5 Excercise 2 29 Feb 2024 9:41 pm est
"""

# Importing package




print("***Q2-A***")
def isDivisible(maxInt, twoInts):
    lstReturn = []
    print("Max int value: " + str(maxInt))
    print("Tuple value : " + str(twoInts))
    for intMaxIndex in range(1, maxInt):
        #print(intMaxIndex)
        intTotalCnt = 0
        #lstReturn.append(intMaxIndex)
        for intTpIndex in twoInts:
            #print("Max index value: " + str(intMaxIndex))
            #print(intTpIndex)
            print("Answer = " + str(intMaxIndex) + "/" + str(intTpIndex) + ": " + str(intMaxIndex%intTpIndex))
            if (intMaxIndex%intTpIndex) == 0:
                intTotalCnt = intTotalCnt + 1
        if (intTotalCnt == len(twoInts)):
            lstReturn.append(intMaxIndex)
    print("Divisible by tuple: ")
    print(lstReturn)

#Calling the function
print("***TEST CASE 1***")
maxIntValue = 7
tpTwoValue = (2, 3)
isDivisible(maxIntValue, tpTwoValue)
print("***Q2-B***")
print("***TEST CASE 2***")
maxIntValue = 6
tpTwoValue = (2, 3)
isDivisible(maxIntValue, tpTwoValue)
print("***TEST CASE 3***")
maxIntValue = 14
tpTwoValue = (2, 3)
isDivisible(maxIntValue, tpTwoValue)
        
        