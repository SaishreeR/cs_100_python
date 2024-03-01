"""
Saishree Ramkumar 
CS 100 Room CKB 207
HW 0 Excercise 2.2, 23 Feb 24 10:50 pm est
"""
import datetime
print("*** Q1 ***")
# Volume of sphere
print("Volume of sphere with radius 5: " + str(1.3*3.14*(5**3)))
print("*** Q2 ***")

copy_1 = (((25.95*0.4) + 3)*1)
copy_2 = (((25.95*0.4) + 0.75)*59)
print("The total wholesale cost is: " + str(copy_1 + copy_2))
print("*** Q3 ***")

intPaceminutes = ((2*495 ) + (3*432))//60
datePace = datetime.datetime(2024, 1, 6, 6, 52, 0)
dateRun = datetime.timedelta(minutes = intPaceminutes)
new_time = datePace + dateRun
print("Get home time for breakfast: " + str(new_time))
