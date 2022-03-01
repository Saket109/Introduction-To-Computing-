print("QUESTION 1 :\n")
# Write a recursive python program to solve the problem of tower of hanoi

def TowerOfHanoi(source,support,destination,n):
    # Creating the base condition
    if n==0:
        return
    # Again calling the function for moving n-1 disks from source to support
    TowerOfHanoi(source,destination,support,n-1)
    # Printing the last move step 
    print(f"Move {n}th disk from {source} to {destination}")
    # Again calling the function for moving n-1 disks from support to destination
    TowerOfHanoi(support,source,destination,n-1)

TowerOfHanoi("A","B","C",3)

##############################################################################################################

print("\nQUESTION 2 :\n")

n=int(input("ENTER A NUMBER :"))
print("\nUsing Loop\n")
# Creating a function to get factorial
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

# Creating a function to get the value of nCr
def combination(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))

def pascalsTriangel(n):
    # Loop for rows
    for i in range(1,n+1):
        # Creating k for even odd print or not
        k=1
        r=0
        # Loop for columns
        for j in range(1,2*n):
            # Condition for printing
            if n+1-i<=j and j<=n-1+i and k:
                print(combination(i-1,r),end="")
                k=0
                r+=1
            else:
                print(" ",end='')
                k=1
        print("\n",end="")

pascalsTriangel(n)

       
print("\nUsing recursions:\n")
def pascal(n, startingn=n):
    # Base Condition
    if n == 0:
        return
    pascal(n-1,startingn)
    #For spaces
    print('  '*(startingn-n), end='')

    entry = 1
    for i in range(1, n+1):
        print(entry, end ='   ')
        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()


pascal(n)

################################################################################################################

print("\nQUESTION 3\n")

m,n = list(int(i) for i in input("ENTER TWO INTEGERS SEPERATED BY SPACE : ").split(" "))
# Using DIVMOD function for getting a tuple of quotient and remainder
val = divmod(m,n)
print(val)

print("Part A")
# Checking whether the function is callable or not by using CALLABLE FUNCTION
print(callable(divmod))

print("\nPart B")
# Checking all values are non-zero or not
k=0
for i in val:
    if i == 0:
        print("False")
        break
    k+=1
if k==len(val):
    print("True")


print("\nPart C")
new_val=val+(4,5,6)
print(f"New Tuple : {new_val}")
empty_list=[]
for i in new_val:
    if i>4:
        empty_list.append(i)
print(f"Greater Than 4 : {empty_list}")

print("\nPart D")
set_data=set(new_val)
print(set_data)

print("\nPart E")
# Frozen the set by using FROZENSET FUNCTION
frozen=frozenset(set_data)
print(f"FROZEN SET : {frozen}")

print("\nPart F")
mylist=[]
for j in set_data:
    mylist.append(j)

for i in range(len(mylist)-1):
    if mylist[i]>mylist[i+1]:
        mylist[i],mylist[i+1]=mylist[i+1],mylist[i]

x=mylist[-1]
print(hash(x))

###############################################################################################################

print("\nQUESTION 4 :")

class student:
    # Creating the instance attributes
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def __del__(self):
        print("Object Destroyed!!")

# Creating the object named STUDENT
Student=student("Saket",21105105) 
print("Object Created!!")  

print(f"The name of the student is {Student.name} and it's rollno is {Student.rollno}")

del Student

########################################################################################################################

print("\nQUESTION 5 :")

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def print_data(self):
        print(f"{self.name} record deleted!!")

# Creating objects of Employee
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)
print("\nPart A")

# Updating salary of Mehak

employee1.salary = 70000
print(f"The updated salary of {employee1.name} is {employee1.salary}")
print("\nPart B")

# Deleting the record of Employee Viren

del employee3

###########################################################################################################################

#Question 6
print("\nQUESTION 6\n")

# Creating a function to convert string to list of letters
def list_letters(string):                                 
    list_new = []
    for i in string:
        list_new.append(i)
    return list_new

while True:          
    wordGeorge = input("Enter word uttered by George: ").lower().split()
    if len(wordGeorge) == 1:
        wordGeorge = wordGeorge[0]
        break
    else:
        print("ERROR!!  Only one word is to be entered\nPlease try again!")

while True:                
    wordBarbie = input("Enter word made by Barbie: ").lower().split()
    if len(wordBarbie) == 1:
        wordBarbie = wordBarbie[0]
        break
    else:
        print("ERROR!!  Only one word is to be entered\nPlease try again!")

letters_in_wordGeorge = list_letters(wordGeorge)
letters_in_wordBarbie = list_letters(wordBarbie)

while True: 
    # Asking the shopkeeper if he want to consider same no. of letters                        
    same_letters = input("\nDo you want to consider same no. of letters also? ")
    if same_letters in ("N","n","No","NO","no"):
        same_letters = False
        break
    elif same_letters in ("YES","Yes","Y","y","yes"):
        same_letters = True
        break
    else:
        print("Please enter 'Yes' or 'No'")

if same_letters:
    # Comparing letters of GEORGIE AND BARBIE
    if sorted(letters_in_wordBarbie) == sorted(letters_in_wordGeorge):
        word_created = True
    else:
        word_created = False
else:
    # Comparing letters of set because number of letters doesn't matter
    if set(letters_in_wordBarbie) == set(letters_in_wordGeorge):        
        word_created = True
    else:
        word_created = False

if word_created:
    print("\nBarbie has made a valid word!  HENCE THEIR FRIENDSHIP IS TRUE.")
else:
    print("\nBarbie fails to form a word!  HENCE THEIR FRIENDSHIP IS FAKE.")
