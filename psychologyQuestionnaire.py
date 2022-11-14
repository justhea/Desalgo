
import textwrap
import time, threading
import sys,time,random
def Psychology():
    print("Psychology Exam")
    psychologyScore = 0
    #psychQ1
    print("1. Forming a hypothesis is the ___ step to the scientific method. \nA.) final \nB.) second \nC.) third \nD.) first")
    psychA1 = input("Answer: ")
    if psychA1 == "D" or psychA1 == "d":
        print("Correct Answer! \n")
        psychologyScore += 1
    elif psychA1 == "A" or psychA1 == "a" or psychA1 == "B" or psychA1 == "b" or psychA1 == "C" or psychA1 == "c":
        print("Incorrect Answer. \n")
    else:
        while psychA1 != "A" or psychA1 != "a" or psychA1 != "B" or psychA1 != "b" or psychA1 != "C" or psychA1 != "c" or psychA1 != "D" or psychA1 != "d":
            print("Please input a valid answer.")
            psychA1 = input("Answer: ")
            if psychA1 == "D" or psychA1 == "d":
                print("Correct Answer! \n")
                psychologyScore += 1
                break
            elif psychA1 == "A" or psychA1 == "a" or psychA1 == "B" or psychA1 == "b" or psychA1 == "C" or psychA1 == "c":
                print("Incorrect Answer. \n")
                break

    #pyschQ2
    print("2. Psychologist Stanley Milgram conducted an experiment in which participants were instructed to administer ___ to 'learners' in another room. \nA.) Psychotherapy \nB.) Sleeping Pills \nC.) Electric Shocks \nD.) Hearing Test")
    psychA2 = input("Answer: ")
    if psychA2 == "C" or psychA2 == "c":
        print("Correct Answer! \n")
        psychologyScore += 1
    elif psychA2 == "A" or psychA2 == "a" or psychA2 == "B" or psychA2 == "b" or psychA2 == "D" or psychA2 == "d":
        print("Incorrect Answer. \n")
    else:
        while psychA2 != "A" or psychA2 != "a" or psychA2 != "B" or psychA2 != "b" or psychA2 != "C" or psychA2 != "c" or psychA2 != "D" or psychA2 != "d":
            print("Please input a valid answer.")
            psychA2 = input("Answer: ")
            if psychA2 == "C" or psychA2 == "c":
                print("Correct Answer! \n")
                psychologyScore += 1
                break
            elif psychA2 == "A" or psychA2 == "a" or psychA2 == "B" or psychA2 == "b" or psychA2 == "D" or psychA2 == "d":
                print("Incorrect Answer. \n")
                break

    #psychQ3
    print("3. The study of psychology looks past ___ to better understand unconscious drives. \nA.) Dreams \nB.) Outward Behaviors \nC.) Health \nD.) Words and writing")
    psychA3 = input("Answer: ")
    if psychA3 == "B" or psychA3 == "b":
        print("Correct Answer! \n")
        psychologyScore += 1
    elif psychA3 == "A" or psychA3 == "a" or psychA3 == "C" or psychA3 == "c" or psychA3 == "D" or psychA3 == "d":
        print("Incorrect Answer. \n")
    else:
        while psychA3 != "A" or psychA3 != "a" or psychA3 != "B" or psychA3 != "b" or psychA3 != "C" or psychA3 != "c" or psychA3 != "D" or psychA3 != "d":
            print("Please input a valid answer.")
            psychA3 = input("Answer: ")
            if psychA3 == "B" or psychA3 == "b":
                print("Correct Answer! \n")
                psychologyScore += 1
                break
            elif psychA3 == "A" or psychA3 == "a" or psychA3 == "C" or psychA3 == "c" or psychA3 == "D" or psychA3 == "d":
                print("Incorrect Answer. \n")
                break

    #psychQ4
    print("4. Danesha took her sick cat to the veterinarian and was informed that her pet has kidney disease. Danesha reacts angrily and refuses to believe the diagnosis. A different vet confirms the diagnosis, but Danesha tells herself that the vets are just trying to get her to purchase expensive medicine for her healthy pet. According to Freud, this is an example of what defense mechanism? \nA.) Humor \nB.)Sublimation \nC.) Passive Aggression \nD.) Denial")
    psychA4 = input("Answer: ")
    if psychA4 == "D" or psychA4 == "d":
        print("Correct Answer! \n")
        psychologyScore += 1
    elif psychA4 == "A" or psychA4 == "a" or psychA4 == "B" or psychA4 == "b" or psychA4 == "C" or psychA4 == "c":
        print("Incorrect Answer. \n")
    else:
        while psychA4 != "A" or psychA4 != "a" or psychA4 != "B" or psychA4 != "b" or psychA4 != "C" or psychA4 != "c" or psychA4 != "D" or psychA4 != "d":
            print("Please input a valid answer.")
            psychA4 = input("Answer: ")
            if psychA4 == "D" or psychA4 == "d":
                print("Correct Answer! \n")
                psychologyScore += 1
                break
            elif psychA4 == "A" or psychA4 == "a" or psychA4 == "B" or psychA4 == "b" or psychA4 == "C" or psychA4 == "c":
                print("Incorrect Answer. \n")
                break

    #psychQ5
    print("5. Marco has been practicing a violin piece for several hours. He is very tired but he feels he should not stop until he has perfectly mastered the song. Which Freudian part of personality would describe this strong feeling of self-control? \nA.) Alter Ego \nB.) Pro-ego \nC.) Super Ego \nD.) ID")
    psychA5 = input("Answer: ")
    if psychA5 == "C" or psychA5 == "c":
        print("Correct Answer! \n")
        psychologyScore += 1
    elif psychA5 == "A" or psychA5 == "a" or psychA5 == "B" or psychA5 == "b" or psychA5 == "D" or psychA5 == "d":
        print("Incorrect Answer. \n")
    else:
        while psychA5 != "A" or psychA5 != "a" or psychA5 != "B" or psychA5 != "b" or psychA5 != "C" or psychA5 != "c" or psychA5 != "D" or psychA5 != "d":
            print("Please input a valid answer.")
            psychA5 = input("Answer: ")
            if psychA5 == "C" or psychA5 == "c":
                print("Correct Answer! \n")
                psychologyScore += 1
                break
            elif psychA5 == "A" or psychA5 == "a" or psychA5 == "B" or psychA5 == "b" or psychA5 == "D" or psychA5 == "d":
                print("Incorrect Answer. \n")
                break
    return psychologyScore