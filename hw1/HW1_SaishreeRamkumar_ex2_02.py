"""
Saishree Ramkumar 
CS 100 Room CKB 207
HW 1 Excercise 2, 20 Feb 24 10:17 pm est
"""

# List for dog breeds
lstDogBreeds = ['Collie', 'Sheepdog', 'Chow','Chihuahua']
print("a. Dog breeds list: " + str(lstDogBreeds))
lstTinyDogs = []
lstHerdingDogs = lstDogBreeds[0:2]
print("b. Dog breeds after slicing: " + str(lstHerdingDogs))

lstTinyDogs.append(lstDogBreeds[3])
print("c. Tiny dogs using the last element of list dog breeds: " + str(lstTinyDogs))
# Function to search value in list
def search_list (lstDogBreeds):
    for strlistVal in lstDogBreeds:
        if (strlistVal.lower() == 'persian'):
            return True
        else:
            return False
        
blnOutput = search_list(lstDogBreeds)
print("d. Persian exist in the list of dog breeds: " + str(blnOutput))

