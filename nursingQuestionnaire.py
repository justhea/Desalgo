
import textwrap
import time, threading
import sys,time,random
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
