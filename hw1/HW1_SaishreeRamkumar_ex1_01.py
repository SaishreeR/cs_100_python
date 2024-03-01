"""
Saishree Ramkumar 
CS 100 Room CKB 207
HW 0 Excercise 1, 20 Feb 24 10:17 pm est
"""
# Grade list
lstGrades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
lstFrequency = []
print("Grades are: " + str(lstGrades))
lstCnt_A = (lstGrades.count('A'))
lstCnt_B = (lstGrades.count('B'))
lstCnt_C = (lstGrades.count('C'))
lstCnt_D = (lstGrades.count('D'))
lstCnt_F = (lstGrades.count('F'))

# Frequencies 
lstFrequency.append(lstCnt_A)
lstFrequency.append(lstCnt_B)
lstFrequency.append(lstCnt_C)
lstFrequency.append(lstCnt_D)
lstFrequency.append(lstCnt_F)
print("Frequencies are: " + str(lstFrequency))




