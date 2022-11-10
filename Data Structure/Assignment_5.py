'''
    QUESTION : Compare Bubble sort and Selection sort based on the following:
1. Number of comparisons
2. Number of swaps
3. Inplace and Outplace implementations

All the comparisons should be made through coding implementations.

'''

# Name - Saket Ahlawat
# SID - 21105105
# Branch - ECE

def bubbleSort(arr):
    ans = []
    swaps = 0
    comparisons = 0
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
                swaps += 1
            comparisons += 1

    ans.append(swaps)
    ans.append(comparisons)

    return ans


def selectionSort(arr):
    ans = []
    swaps = 0
    comparisons = 0
    min_index = 0

    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)-1):
            if arr[j] < arr[min_index] :
                min_index = j
                swaps += 1
            
        comparisons += 1

        arr[i],arr[min_index] = arr[min_index],arr[i]

    ans.append(swaps)
    ans.append(comparisons)

    return ans


# main

n = int(input())
arr = [int(ele) for ele in input().split()]

bubble = bubbleSort(arr)
selection = selectionSort(arr)

print("comparison between Bubble sort and Selection sort : ")
print("1.) On the basis of comparisons : ")
if bubble[1]>selection[1] :
    print("MORE COMPARSIONS ARE REQUIRED FOR BUBBLE SORT.")
elif bubble[1] < selection[1] :
    print("MORE COMPARISONS ARE REQUIRED FOR SELECTION SORT.")
else:
    print("BOTH REQUIRE EQUAL NUMBER OF COMPARISONS.")


print()

print("2. ON THE BASIS OF NUMBE ROF SWAPS : ")

if bubble[0] > selection[0] :
    print("MORE SWAPS ARE REQUIRED FOR BUBBLE SORT.")
elif bubble[0] < selection[0] :
    print("MORE SWAPS ARE REQUIRED FOR SELECTION SORT.")
else:
    print("BOTH REQUIRE EQUAL NUMBER OF SWAPS.")

print("3 . As both BubbleSort and SelectionSort are In-place algorithms, hence both of their Inplace Algorithms have been written above.")
