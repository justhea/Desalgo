from psychologyQuestionnaire import Psychology
from nursingQuestionnaire import Nursing
from pharmacologyQuestionnaire import Pharmacology
from medTechQuestionnaire import MedicalTechnology
from mainUI import userInterface, printSlow, slowPrint
import textwrap
import time, threading
import sys,time,random
userInterface()
print("")
courses = ["Pyschology", "Nursing", "Medical Technology", "Pharmacy"]
basisScore = []
printSlow("Loading Psychology exam")
basisScore.append(Psychology())
time.sleep(1)
printSlow("Loading Nursing exam")
basisScore.append(Nursing())
time.sleep(1)
printSlow("Loading Medical Technology exam")
basisScore.append(MedicalTechnology())
time.sleep(1)
printSlow("Loading Pharmacology exam")
basisScore.append(Pharmacology())
time.sleep(1)

sortedScore = list(zip(basisScore, courses))




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
for courses, basisScore in sortedScore [1:]:
    print("Your highest score is {} "
    
exit()