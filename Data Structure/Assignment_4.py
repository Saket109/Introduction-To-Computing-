'''
    QUESTION 1 : What is the difference between in-place and out-place sorting algorithms?
'''

# ANSWER :
'''
    In place sorting is sorting without using extra memory (mostly swapping elements till getting it right).
    but usually in place sorting indicates to constant extra memory. Hence In place sorting
    required O(1) space complexity.

    Whereas in An out-of-place sorting algorithm needs extra space to put the elements in as it's sorting them. Usually this means O(n) extra space.
'''

'''
    QUESTION 2 : Implement Insertion sort in both (in-place and out-place) manner.
'''

# ANSWER :

# Implementation of insertion sort by in-place manner.

# defining the function 
def insertion_sort(arr):
    # si = starting index 
    for si in range(1,len(arr)):
        val = arr[si]
        curr = si-1

        while curr>=0 and val<arr[curr] :
            arr[curr+1] = arr[curr]
            curr-=1

        arr[curr+1] = val

    # space complexity = O(1)
    # time complexity = O(n)


# if we want to implement the insertion sort by out place manner then we have to use an extra array

# defining the out-place insertion sort function
def insertion_sort_out_place(arr,si,ei):

    # si = starting index
    # ei = end index

    # base case
    if si == ei:
        return
    
    curr = si+1
    temp = arr[curr]

    while(si>=0) :
        if arr[si] > temp :
            arr[si+1] = arr[si]
            si-=1

        if si == -1:
            arr[0] = temp
            break

        if arr[si] <= temp :
            arr[si+1] = temp
            break

    insertion_sort_out_place(arr,si+1,ei)       # calling the function again 

    # space complexity = O(n)
    # time complexity = O(1)

arr1 = [int(ele) for ele in input("Enter the input array separated by spaces : ").split()]        # taking the array input in a single line
insertion_sort(arr1)            # calling the simple in-place insertion sorting algorithm
print("sorted array is : ")
print(arr1) 

arr2 = [int(ele) for ele in input("Enter the input array separated by spaces : ").split()]
insertion_sort_out_place(arr2,0,len(arr2)-1)
print("Sorted array is : ")
print(arr2)

        
'''
    QUESTION 3 :  Suggest some practical examples of using in-place and out-place techniques.
'''

# ANSWER :

'''

In-place techniques have lesser space complexity but are difficult to 
apply in algorithm whereas out-place techniques are easy to aplly but 
increases the space complexity of algorithm.

For exapmle if we want to reverse an array then its in-place algorithm
will be swaping the first and last element of array until we reach the 
middle of array,If we want to solve the same problem using out-place 
algorithm we have to create one extra array of same size and copy 
elements of original array from back to the front of new array,this 
algorith increases the space complexity to O(n) as we have creaed an 
extra array.

Examples of In-Place algorithm : Selection sort , Insertion sort , Bubble sort , Heapsort.

Examples of Out-Place algorithm : Merge sort , Radix sort.
'''
        
