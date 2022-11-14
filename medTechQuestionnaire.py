
def MedicalTechnology():
    medTechScore = 0
    print("Medical Technology Exam")
    
    #medTechQ1
    print("1. Other name for HCV RNA? \nA.) Viral clade \nB.) Viral load \nC.) Surface antigen \nD.) Core antigen")
    medTechA1 = input("Answer: ")
    if medTechA1 == "B" or medTechA1 == "b":
        print("Correct Answer! \n")
        medTechScore += 1
    elif medTechA1 == "A" or medTechA1 == "a" or medTechA1 == "D" or medTechA1 == "d" or medTechA1 == "C" or medTechA1 == "c":
        print("Incorrect Answer. \n")
    else:
        while medTechA1 != "A" or medTechA1 != "a" or medTechA1 != "B" or medTechA1 != "b" or medTechA1 != "C" or medTechA1 != "c" or medTechA1 != "D" or medTechA1 != "d":
            print("Please input a valid answer.")
            medTechA1 = input("Answer: ")
            if medTechA1 == "B" or medTechA1 == "b":
                print("Correct Answer! \n")
                medTechScore += 1
                break
            elif medTechA1 == "A" or medTechA1 == "a" or medTechA1 == "D" or medTechA1 == "d" or medTechA1== "C" or medTechA1 == "c":
                print("Incorrect Answer. \n")
                break

    #medTechQ2
    print("2. What is a fact about Anti-U? \nA.) most common antibody in the MNSsu system \nB.) found only in black individuals \nC.) naturally occuring antibody \nD.) named “U” for Uruguay")
    medTechA2 = input("Answer: ")
    if medTechA2 == "B" or medTechA2 == "b":
        print("Correct Answer! \n")
        medTechScore += 1
    elif medTechA2== "A" or medTechA2 == "a" or medTechA2 == "D" or medTechA2 == "d" or medTechA2 == "C" or medTechA2 == "c":
        print("Incorrect Answer. \n")
    else:
        while medTechA2 != "A" or medTechA2 != "a" or medTechA2 != "B" or medTechA2 != "b" or medTechA2 != "C" or medTechA2 != "c" or medTechA2 != "D" or medTechA2 != "d":
            print("Please input a valid answer.")
            medTechA2 = input("Answer: ")
            if medTechA2 == "B" or medTechA2 == "b":
                print("Correct Answer! \n")
                medTechScore += 1
                break
            elif medTechA2 == "A" or medTechA2 == "a" or medTechA2 == "D" or medTechA2 == "d" or medTechA2== "C" or medTechA2 == "c":
                print("Incorrect Answer. \n")
                break

    #medTechQ3
    print("3. Blood component given to patient with aplastic anemia? \nA.) FWB (fresh whole blood) \nB washed RBC, less than 7 days old \nC.) PRBC from WB \nD.) Irradiated blood")
    medTechA3 = input("Answer: ")
    if medTechA3 == "C" or medTechA3 == "c":
        print("Correct Answer! \n")
        medTechScore += 1
    elif medTechA3 == "A" or medTechA3 == "a" or medTechA3 == "B" or medTechA3 == "b" or medTechA3 == "D" or medTechA3== "d":
        print("Incorrect Answer. \n")
    else:
        while medTechA3 != "A" or medTechA3 != "a" or medTechA3 != "B" or medTechA3 != "b" or medTechA3 != "C" or medTechA3 != "c" or medTechA3 != "D" or medTechA3 != "d":
            print("Please input a valid answer.")
            medTechA3 = input("Answer: ")
            if medTechA3 == "C" or medTechA3 == "c":
                print("Correct Answer! \n")
                medTechScore += 1
                break
            elif medTechA3 == "A" or medTechA3 == "a" or medTechA3 == "B" or medTechA3 == "b" or medTechA3 == "D" or medTechA3 == "d":
                print("Incorrect Answer. \n")
                break

    #medTechQ4
    print("4. Indication for neocyte transfusion? \nA.) ITP \nB.) HTR \nC.) Hyrdops fetalis \nD.) thalassemia")
    medTechA4 = input("Answer: ")
    if medTechA4 == "D" or medTechA4 == "d":
        print("Correct Answer! \n")
        medTechScore += 1
    elif medTechA4 == "A" or medTechA4 == "a" or medTechA4 == "B" or medTechA4 == "b" or medTechA4 == "C" or medTechA4 == "c":
        print("Incorrect Answer. \n")
    else:
        while medTechA4 != "A" or medTechA4 != "a" or medTechA4 != "B" or medTechA4 != "b" or medTechA4 != "C" or medTechA4 != "c" or medTechA4 != "D" or medTechA4 != "d":
            print("Please input a valid answer.")
            medTechA4 = input("Answer: ")
            if medTechA4 == "D" or medTechA4 == "d":
                print("Correct Answer! \n")
                medTechScore += 1
                break
            elif medTechA4 == "A" or medTechA4 == "a" or medTechA4 == "B" or medTechA4 == "b" or medTechA4 == "C" or medTechA4 == "c":
                print("Incorrect Answer. \n")
                break

    #medTechQ5
    print("5. Famous cook whose reported to be a carrier of a febrile disease, and reported to killed 50 persons. \nA.) Felix \nB Widal \nC.) Mary \nD.) Moley")
    medTechA5 = input("Answer: ")
    if medTechA5 == "C" or medTechA5 == "c":
        print("Correct Answer! \n")
        medTechScore += 1
    elif medTechA5 == "A" or medTechA5 == "a" or medTechA5 == "B" or medTechA5 == "b" or medTechA5 == "D" or medTechA5== "d":
        print("Incorrect Answer. \n")
    else:
        while medTechA5 != "A" or medTechA5 != "a" or medTechA5 != "B" or medTechA5 != "b" or medTechA5 != "C" or medTechA5 != "c" or medTechA5 != "D" or medTechA5 != "d":
            print("Please input a valid answer.")
            medTechA5 = input("Answer: ")
            if medTechA5 == "C" or medTechA5 == "c":
                print("Correct Answer! \n")
                medTechScore += 1
                break
            elif medTechA5 == "A" or medTechA5 == "a" or medTechA5 == "B" or medTechA5 == "b" or medTechA5 == "D" or medTechA5 == "d":
                print("Incorrect Answer. \n")
                break
    return medTechScore
