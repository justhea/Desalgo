#Impoprt printSlow
import textwrap
import time, threading
import sys,time,random

#Print slow stuff
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

#Main UI of the program
def userInterface():

    #Print Opening 
    print("=====================================")
    printSlow("Medical Specification Assessment Exam")
    print("=====================================")
    print("")

    #While loop if user is not picking from list
    userChoice = False #Counter
    while userChoice == False: 

        #Reprint menu while user is still not done
         printSlow("What would you like to do?")
         time.sleep(0.5)
         print("1. Take exam")
         print("2. About application")
         print("3. Credits")
         print("4. Exit")

         #take user input for while loop
         userChoice = int(input())
         
         #Take exam print the questionnaire
         if userChoice == 1:
             print("Goodluck!")
             time.sleep(0.5)
         
         #Print The about application
         elif userChoice == 2:
            printSlow("About Application")
            time.sleep(1)
            printSlow("The application is modeled after the national career assessment examination of the")
            printSlow("Philippines given to highschool students. This is a 20 question multiple choice ")
            printSlow("examination meant to evaluate a suitable course based on the user's performance")
            printSlow("and knowledge in the specific courses")
            time.sleep(0.5)
            printSlow("Returning to main menu")
            userChoice = False

         #Print Credits
         elif userChoice == 3:
            printSlow("Alexandra Paculan - Lead Documentation")
            printSlow("Carl Justin Bustamante - Lead Programmer")
            printSlow("Jethro Rae Garcia - Leader")
            printSlow("Yuri Laigo - Lead Programmer")
            time.sleep(0.5)
            printSlow("Returning to Main Menu")
            userChoice = False

         #Exit Program
         elif userChoice == 4:
            printSlow("Goodbye!")
            exit() #exit
         
         #If none of the elifs reloop
         else:
            print("Enter again")
