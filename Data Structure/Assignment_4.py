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

def insertion_sort(arr):
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

def insertion_sort_out_place(arr,si,ei):
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

    insertion_sort_out_place(arr,si+1,ei)

arr1 = [int(ele) for ele in input().split()]
insertion_sort(arr1)
print(arr1)

arr2 = [int(ele) for ele in input().split()]
insertion_sort_out_place(arr2,0,len(arr2)-1)
print(arr2)

        
