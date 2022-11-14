from psychologyQuestionnaire import Psychology
from nursingQuestionnaire import Nursing
from pharmacologyQuestionnaire import Pharmacology
from medTechQuestionnaire import MedicalTechnology

def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
    
        key = arr[i]
    
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
def search(arr, N, x):
 
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
 
# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)
    
    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
    
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])

#Instructions
print("Instructions:")
print("Multiple Choice. Choose the most suitable choice for the given question/situation.")
print("Your score will be tallied and sorted to procure your suitable course based on your scores. \n")

Psychology()
Nursing()
Pharmacology()
MedicalTechnology()
