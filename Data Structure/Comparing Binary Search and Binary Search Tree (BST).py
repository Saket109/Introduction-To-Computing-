'''

    Name = Saket Ahlawat
    Branch = ECE
    SID = 21105105

    Question : 1. Take an array of numbers.
               2. Use it to construct a BST.
               3. Write separate functions to delete a node from BST and Array.
               4. Now compute the space complexity of both structures.
'''

# Function for deleting the element from the array

def deleteArr(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            arr.pop(i)



# Creating the binary tree node

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

# Constructing the BST (Binary Search Tree)

class BST:
    def __init__(self):                 # constructor
        self.root=None

    def printTreeHelper(self,root):             # using helper function to use recursion
        if root==None:
            return
        print(root.data,end=":")
        if root.left!=None:
            print("L",root.left.data,end=",")
        if root.right!=None:
            print("R",root.right.data,end="")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
        
    def printTree(self):                        # function for printing the BST
        self.printTreeHelper(self.root)


    def insertHelper(self,root,value):           # creating the helper function to use recursion
        if root == None:
            node = BinaryTreeNode(value)
            return node
        if root.data > value:
            root.left = self.insertHelper(root.left,value)
            return root
        else:
            root.right = self.insertHelper(root.right,value)
            return root

    def insert(self,value):          # function for inserting the data into BST
        self.root = self.insertHelper(self.root,value)

    def min(self,root):             # function for finding the minimum element in the BST
        if root == None:
            return 10000
        if root.left == None:
            return root.data
        return self.min(root.left)

    def deleteDataHelper(self,root,value):       # creating the helper function for using recursion
        if root == None:
            return None
        if root.data < value:
            newRightNode = self.deleteDataHelper(root.right,value)
            root.right = newRightNode
            return root
        if root.data > value:
            newLeftNode = self.deleteDataHelper(root.left,value)
            root.left = newLeftNode
            return root

        #root is leaf
        if root.left==None and root.right==None:
            return None

        # root has one child
        if root.left==None:
            return root.right
        if root.right==None:
            return root.left

        #root has 2 children
        replacement=self.min(root.right)
        root.data=replacement
        newRightNode=self.deleteDataHelper(root.right,replacement)
        root.right=newRightNode
        return root

    def deleteData(self,data):                  # function for deleting the element of the BST
        newRoot=self.deleteDataHelper(self.root,data)
        self.root=newRoot
        

# I have printed BST as   ->   root : L (left data) , R (right data)

# ARRAY : 
n = int(input("enter the length of the array : "))
arr = [int(ele) for ele in input("write elements of the array separated by space").split()]
deleteArr(arr)
print(arr)


# BST :
b=BST()
b.insert(10)
b.insert(5)
b.insert(7)
b.insert(6)
b.insert(8)
b.insert(12)
b.insert(11)
b.insert(15)
b.printTree()

b.deleteData(10)
b.printTree()


'''
    Space Complexity : if we have n elements then the space complexity of both the array and the
    binary search tree has space complexity of O(n).
'''
