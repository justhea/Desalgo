'''
BROgrammers program for finals requirement for DESALGO
BSCS - SF211
The program uses Insertion sort and Arrays to help medical undergraduates to choose their most suited course. More information can be seen on the paper itself and comments all
throughout the entire programs
'''

#import slow text loading effects
import textwrap
import time, threading
import sys,time,random

#import functions from questionnaires and ui
from medicalQuestionnaires import Pharmacology, Nursing, MedicalTechnology, Psychology
from mainUI import userInterface

#Start main program
userInterface()
print("")

#Sorting and algorithm proper
courses = ["Pyschology", "Nursing", "Medical Technology", "Pharmacy"] #Use to label scores
basisScore = [] #empty array for score of each courses

#Print Exam proper
printSlow("Loading Psychology exam")
basisScore.append(Psychology()) #append score to array from function
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

#zip scores and courses for easier sorting and searching
sortedScore = list(zip(basisScore, courses))

#Insertion sort proper
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

#Sort sortedScore array
insertionSort(sortedScore)

#Determine top score
topScore = None
for score, course in sortedScore: #for loop to look at highest value
    topScore = topScore or score
    if score == topScore:
        printSlow(f"Your most recommended {course = } with a {score = }.") #print highest score with the course for the most recommended course
    else:
        printSlow(f"Your next recommended {course = } with a score of {score = } ") #print next recommended courses

#End of program code
time.sleep(0.5)
printSlow("Exiting Program")
printSlow("Goodbye")
exit() #exit program