import time
from psychologyQuestionnaire import Psychology
from nursingQuestionnaire import Nursing
from pharmacologyQuestionnaire import Pharmacology
from medTechQuestionnaire import MedicalTechnology
def userInterface():
    print("=====================================")
    print("Medical Specification Assessment Exam")
    print("=====================================")
    print("")
    userChoice = 0
    while userChoice == 0:
         print("What would you like to do?")
         print("1. Take exam")
         print("2. About application")
         print("3. Exit")
         userChoice = int(input())
         if userChoice == 1:
             print("Goodluck!")
         elif userChoice == 2:
            print("About Application")
            time.sleep(1)
            print("Returning to main menu")
            userChoice = 0
         elif userChoice == 3:
            print("Goodbye!")
            exit()
         else:
            print("Enter again")
