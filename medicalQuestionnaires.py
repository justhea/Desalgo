#Questionnaires 

#Pahrmacology Questions
def Pharmacology():
    print("Pharmacology Exam")
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


def Nursing():
    print("Nursing Exam")
    nursingScore = 0
    #nursQ1
    print("1. The registered nurse planning to delegate tasks to unlicensed assistive personnel (UAP). Which of the following task could the registered nurse safely assigned to a UAP? \nA.) Monitor the I&O of a comatose toddler client with salicylate poisoning \nB.) Monitor the I&O of a comatose toddler client with salicylate poisoning \nC.) check the IV of a preschooler with Kawasaki disease \nD.) Give an oatmeal bath to an infant with eczema")
    nursA1 = input("Answer: ")
    if nursA1 == "D" or nursA1 == "d":
        print("Correct Answer! \n")
        nursingScore += 1 
    elif nursA1 == "A" or nursA1 == "a" or nursA1 == "B" or nursA1 == "b" or nursA1 == "C" or nursA1 == "c":
        print("Incorrect Answer. \n")
    else:
        while nursA1 != "A" or nursA1 != "a" or nursA1 != "B" or nursA1 != "b" or nursA1 != "C" or nursA1 != "c" or nursA1 != "D" or nursA1 != "d":
            print("Please input a valid answer.")
            nursA1 = input("Answer: ")
            if nursA1 == "D" or nursA1 == "d":
                print("Correct Answer! \n")
                nursingScore += 1 
                break
            elif nursA1 == "A" or nursA1 == "a" or nursA1 == "B" or nursA1 == "b" or nursA1 == "C" or nursA1 == "c":
                print("Incorrect Answer. \n")
                break

    #nursQ2
    print("2. A nurse manager assigned a registered nurse from telemetry unit to the pediatrics unit. There were three patients assigned to the RN. Which of the following patients should not be assigned to the floated nurse? \nA.) A 9-year-old child diagnosed with rheumatic fever \nB.) A young infant after pyloromyotomy \nC.) A 4-year-old with VSD following cardiac catheterization \nD.) A 5-month-old with Kawasaki disease")
    nursA2 = input("Answer: ")
    if nursA2 == "B" or nursA2 == "b":
        print("Correct Answer! \n")
        nursingScore += 1 
    elif nursA2 == "A" or nursA2 == "a" or nursA2 == "D" or nursA2 == "d" or nursA2 == "C" or nursA2 == "c":
        print("Incorrect Answer. \n")
    else:
        while nursA2 != "A" or nursA2 != "a" or nursA2 != "B" or nursA2 != "b" or nursA2 != "C" or nursA2 != "c" or nursA2 != "D" or nursA2 != "d":
            print("Please input a valid answer.")
            nursA2 = input("Answer: ")
            if nursA2 == "B" or nursA2 == "b":
                print("Correct Answer! \n")
                nursingScore += 1 
                break
            elif nursA2 == "A" or nursA2 == "a" or nursA2 == "D" or nursA2 == "d" or nursA2== "C" or nursA2 == "c":
                print("Incorrect Answer. \n")
                break

    #nursQ3
    print("3. A nurse in charge in the pediatric unit is absent. The nurse manager decided to assign the nuse in the obstetrics unit to the pediatrics unit. Which of the following patients could the nurse manager safely assign to the float nurse? \nA.) A child who had multiple injuries from a serious vehicle accident \nB.) A child diagnosed with Kawasaki disease and with cardiac complications \nC.) A child who has a nephrectomy for Wilm's tumor \nD.) A child receiving an IV chelating therapy for lead poisoning")
    nursA3 = input("Answer: ")
    if nursA3 == "C" or nursA3 == "c":
        print("Correct Answer! \n")
        nursingScore += 1 
    elif nursA3 == "A" or nursA3 == "a" or nursA3 == "B" or nursA3 == "b" or nursA3 == "D" or nursA3== "d":
        print("Incorrect Answer. \n")
    else:
        while nursA3 != "A" or nursA3 != "a" or nursA3 != "B" or nursA3 != "b" or nursA3 != "C" or nursA3 != "c" or nursA3 != "D" or nursA3 != "d":
            print("Please input a valid answer.")
            nursA3 = input("Answer: ")
            if nursA3 == "C" or nursA3 == "c":
                print("Correct Answer! \n")
                nursingScore += 1 
                break
            elif nursA3 == "A" or nursA3 == "a" or nursA3 == "B" or nursA3 == "b" or nursA3 == "D" or nursA3 == "d":
                print("Incorrect Answer. \n")
                break

    #nursQ4
    print("4. The registered nurse is planning to delegate task to a certified nursing assistant. Which of the following clients should not be assigned to a CAN? \nA.) A client diagnosed with diabetes and who has an infected toe \nB.) A client who had a CVA in the past two months \nC.) A client with Chronic renal failure \nD.) A client with chronic venous insufficiency ")
    nursA4 = input("Answer: ")
    if nursA4 == "A" or nursA4 == "a":
        print("Correct Answer! \n")
        nursingScore += 1 
    elif nursA4 == "D" or nursA4 == "d" or nursA4 == "B" or nursA4 == "b" or nursA4 == "C" or nursA4 == "c":
        print("Incorrect Answer. \n")
    else:
        while nursA4 != "A" or nursA4 != "a" or nursA4 != "B" or nursA4 != "b" or nursA4 != "C" or nursA4 != "c" or nursA4 != "D" or nursA4 != "d":
            print("Please input a valid answer.")
            nursA4 = input("Answer: ")
            if nursA4 == "A" or nursA4 == "a":
                print("Correct Answer! \n")
                nursingScore += 1 
                break
            elif nursA4 == "D" or nursA4 == "d" or nursA4 == "B" or nursA4 == "b" or nursA4 == "C" or nursA4 == "c":
                print("Incorrect Answer. \n")
                break

    #nursQ5
    print("5. The nurse in the medication unit passes the medications for all the clients on the nursing unit. The head nurse is making rounds with the physician and coordinates clients' activities with other departments. The nurse assistant changes the bed lines and answers call lights. A second nurse is assigned for changing wound dressings; a licensed practitioner nurse takes vital signs and bathes the clients. This illustrates of what method of nursing care? \nA.) Case management method \nB.) Primary nursing method \nC.) Team method \nD.) Functional Method")
    nursA5 = input("Answer: ")
    if nursA5 == "D" or nursA5 == "d":
        print("Correct Answer! \n")
        nursingScore += 1 
    elif nursA5 == "A" or nursA5 == "a" or nursA5 == "B" or nursA5 == "b" or nursA5 == "C" or nursA5 == "c":
        print("Incorrect Answer. \n")
    else:
        while nursA5 != "A" or nursA5 != "a" or nursA5 != "B" or nursA5 != "b" or nursA5 != "C" or nursA5 != "c" or nursA5 != "D" or nursA5 != "d":
            print("Please input a valid answer.")
            nursA5 = input("Answer: ")
            if nursA5 == "D" or nursA5 == "d":
                print("Correct Answer! \n")
                nursingScore += 1 
                break
            elif nursA5 == "A" or nursA5 == "a" or nursA5 == "B" or nursA5 == "b" or nursA5 == "C" or nursA5 == "c":
                print("Incorrect Answer. \n")
                break
    return nursingScore


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