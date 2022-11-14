def Pharmacology():
    print("Pharmacology")
    pharmacologyScore = 0
    #pharmaQ1
    print("1. Group of elements which is the considered to be the most reactive of all metallic elements: \nA.) Group O \nB.) Group IA \nC.) Group IB \nD.) Group II")
    pharA1 = input("Answer: ")
    if pharA1 == "B" or pharA1 == "b":
        print("Correct Answer! \n")
        pharmacologyScore += 1
    elif pharA1 == "A" or pharA1 == "a" or pharA1 == "D" or pharA1 == "d" or pharA1 == "C" or pharA1 == "c":
        print("Incorrect Answer. \n")
    else:
        while pharA1 != "A" or pharA1 != "a" or pharA1 != "B" or pharA1 != "b" or pharA1 != "C" or pharA1 != "c" or pharA1 != "D" or pharA1 != "d":
            print("Please input a valid answer.")
            pharA1 = input("Answer: ")
            if pharA1 == "B" or pharA1 == "b":
                print("Correct Answer! \n")
                pharmacologyScore += 1
                break
            elif pharA1 == "A" or pharA1 == "a" or pharA1 == "D" or pharA1 == "d" or pharA1 == "C" or pharA1 == "c":
                print("Incorrect Answer. \n")
                break

    #pharmaQ2
    print("2. Preparations used for brain scanning to determine the presence and location of neo-plastic lesion: \nA Gold Au198 Injection \nB.) Chlormerodrin Hg 197 Injection \nC.) Technetium Tc 99 Injection \nD.) Sodium Phosphate P23 Solution")
    pharA2 = input("Answer: ")
    if pharA2 == "C" or pharA2 == "c":
        print("Correct Answer! \n")
        pharmacologyScore += 1
    elif pharA2 == "A" or pharA2 == "a" or pharA2 == "D" or pharA2 == "d" or pharA2 == "B" or pharA2 == "b":
        print("Incorrect Answer. \n")
    else:
        while pharA2 != "A" or pharA2 != "a" or pharA2 != "B" or pharA2 != "b" or pharA2 != "C" or pharA2 != "c" or pharA2 != "D" or pharA2 != "d":
            print("Please input a valid answer.")
            pharA2 = input("Answer: ")
            if pharA2 == "C" or pharA2 == "c":
                print("Correct Answer! \n")
                pharmacologyScore += 1
                break
            elif pharA2 == "A" or pharA2 == "a" or pharA2 == "D" or pharA2 == "d" or pharA2 == "B" or pharA2 == "b":
                print("Incorrect Answer. \n")
                break

    #pharmaQ3
    print("3. In REDOX reaction, the oxidizing agent: \nA.) Is oxidizedt \nB Loses electrons \nC.) Is reduced \nD.) Increased in oxidation state")
    pharA3 = input("Answer: ")
    if pharA3 == "C" or pharA3 == "c":
        print("Correct Answer! \n")
        pharmacologyScore += 1
    elif pharA3 == "A" or pharA3 == "a" or pharA3 == "B" or pharA3 == "b" or pharA3 == "D" or pharA3== "d":
        print("Incorrect Answer. \n")
    else:
        while pharA3 != "A" or pharA3 != "a" or pharA3 != "B" or pharA3 != "b" or pharA3 != "C" or pharA3 != "c" or pharA3 != "D" or pharA3 != "d":
            print("Please input a valid answer.")
            pharA3 = input("Answer: ")
            if pharA3 == "C" or pharA3 == "c":
                print("Correct Answer! \n")
                pharmacologyScore += 1
                break
            elif pharA3 == "A" or pharA3 == "a" or pharA3 == "B" or pharA3 == "b" or pharA3 == "D" or pharA3 == "d":
                print("Incorrect Answer. \n")
                break

    #pharmaQ4
    print("4. The Which of the following glass types makes use of water attack test type? \nA.) Type I \nB.) Type I \nC.) Type III \nD.) None of these")
    pharA4 = input("Answer: ")
    if pharA4 == "B" or pharA4 == "b":
        print("Correct Answer! \n")
        pharmacologyScore += 1
    elif pharA4 == "D" or pharA4 == "d" or pharA4 == "A" or pharA4 == "a" or pharA4 == "C" or pharA4 == "c":
        print("Incorrect Answer. \n")
    else:
        while pharA4 != "A" or pharA4 != "a" or pharA4 != "B" or pharA4 != "b" or pharA4 != "C" or pharA4 != "c" or pharA4 != "D" or pharA4 != "d":
            print("Please input a valid answer.")
            pharA4 = input("Answer: ")
            if pharA4 == "B" or pharA4 == "b":
                print("Correct Answer! \n")
                pharmacologyScore += 1
                break
            elif pharA4 == "D" or pharA4 == "d" or pharA4 == "A" or pharA4 == "a" or pharA4 == "C" or pharA4 == "c":
                print("Incorrect Answer. \n")
                break

    #pharmaQ5
    print("5. An example of glycine conjugation pathway: \nA.) Phenol to phenolsulfate \nB.) Benzoic acid to hippuric acid \nC.) Noradrenaline to epinephrine \nD.) Antabuse to dithiocarbamic acid")
    pharA5 = input("Answer: ")
    if pharA5 == "B" or pharA5 == "b":
        print("Correct Answer! \n")
        pharmacologyScore += 1
    elif pharA5== "A" or pharA5 == "a" or pharA5 == "D" or pharA5 == "d" or pharA5 == "C" or pharA5 == "c":
        print("Incorrect Answer. \n")
    else:
        while pharA5 != "A" or pharA5 != "a" or pharA5 != "B" or pharA5 != "b" or pharA5 != "C" or pharA5 != "c" or pharA5 != "D" or pharA5 != "d":
            print("Please input a valid answer.")
            pharA5 = input("Answer: ")
            if pharA5 == "B" or pharA5 == "b":
                print("Correct Answer! \n")
                pharmacologyScore += 1
                break
            elif pharA5 == "A" or pharA5 == "a" or pharA5 == "D" or pharA5 == "d" or pharA5== "C" or pharA5 == "c":
                print("Incorrect Answer. \n")
                break
    return pharmacologyScore
