from psychologyQuestionnaire import Psychology
from nursingQuestionnaire import Nursing
from pharmacologyQuestionnaire import Pharmacology
from medTechQuestionnaire import MedicalTechnology
import textwrap
import time, threading
import sys,time,random

def printSlow(text):
    for line in textwrap.wrap(text,120):
        slowPrint(line)
        print()
    print("")

def slowPrint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

def userInterface():
    print("=====================================")
    printSlow("Medical Specification Assessment Exam")
    print("=====================================")
    print("")
    userChoice = 0
    while userChoice == 0:
         printSlow("What would you like to do?")
         time.sleep(0.5)
         print("1. Take exam")
         print("2. About application")
         print("3. Credits")
         print("4. Exits")
         userChoice = int(input())
         if userChoice == 1:
             print("Goodluck!")
             time.sleep(0.5)
         elif userChoice == 2:
            printSlow("About Application")
            time.sleep(1)
            printSlow("The application is modeled after the national career assessment examination of the")
            printSlow("philippines given to highschool students. This is an 20 question multiple choice ")
            printSlow("examination meant to evaluate a suitable course based on the user's performance")
            printSlow("and knowledge in the specific courses")
            time.sleep(0.5)
            printSlow("Returning to main menu")
            userChoice = 0
         elif userChoice == 3:
            printSlow("Alexandra Paculan - Lead Documentation")
            printSlow("Carl Justin Bustamante - Lead Programmer")
            printSlow("Jethro Rae Garcia - Leader")
            printSlow("Yuri Laigo - Lead Programmer")
            time.sleep(0.5)
            printSlow("Returning to Main Menu")
         elif userChoice == 4:
            printSlow("Goodbye!")
            exit()
         else:
            print("Enter again")