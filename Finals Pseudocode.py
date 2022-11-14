from psychologyQuestionnaire import Psychology
from nursingQuestionnaire import Nursing
from pharmacologyQuestionnaire import Pharmacology
from medTechQuestionnaire import MedicalTechnology
import time
basisScore = []
sortedScore = []
basisScore.append(Psychology())
basisScore.append(Nursing())
basisScore.append(MedicalTechnology())
basisScore.append(Pharmacology())

for i in sortedScore:
    sortedScore.append(i)
print(basisScore)

courses = ["Pyschology", "Nursing", "Medical Technology", "Pharmacy"]

def insertionSort(arr):
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key > arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
insertionSort(sortedScore)
def linearSearch(basisScore, n, y):
    for i in range(0, n):
        if (basisScore[i] == y):
            return i
    return -1
for y in sortedScore:
    n = len(sortedScore)
    result = linearSearch(basisScore, n, y)
    if(result == -1):
        print("Element not found")
    else:
	    print(courses[result])
