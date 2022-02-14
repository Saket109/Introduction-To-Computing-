#1.) Write a python program to count the number of occurences of each character/word in the string entered by the user.
print("THE SOLUTION OF QUESTION 1 :\n")
input_value = input("Enter the string: ").lower().split()
# CHECKING IF INPUT IS SINGLE STRING
if len(input_value) == 1:
    input_value = input_value[0]
# CREATING A DICTIONARY SO THAT WE CAN DEAL WITH 2 VARIABLES TOGETHER
occurences = {}
for i in input_value:
    if i not in occurences:
        occurences[i] = 1
    else:
        occurences[i] += 1
print("The occurence(s) of:")
for i in occurences:
     print(f"\t\t\"{i}\"    is/are   {occurences[i]} ")

##############################################################################################################

#QUESTION 2
print("\nTHE SOLUTION OF QUESTION 2 :\n")
# DEFINING A FUNCTION TO CHECK IF GIVEN YEAR IS LEAP YEAR OR NOT
def is_leap_year(year):                                                                              
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
# CONDITION FOR GIVEN CONSTRAINTS IN THE QUESTION 
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
# CONDITION FOR 31 DAYS IN 30 DAYS MONTH 
    if month in (4,6,9,11) and date == 31:                                                                         
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
# CONDITION FOR FEBRUARY AND LEAP YEAR
    elif month == 2 and date >= 29:                                                                                
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
# DEFINING MAX_DAYS FOR OUR COMFORT
if month == 2:                                                                                                      
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
#  IF DATE IS MAX_DATE THEN CHANGING IT TO 1
if date == max_days:                                                                                               
    date = 1
# IF MONTH IS 12 THEN CHANGING IT TO 1 AND INCREASE THE YEAR BY 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
# IF MONTH IS LESS THAN 10 THEN PRINTING WITH LEADING 0
if month<10:
    print("Next Date is: %d/0%d/%d" % (date,month,year))
else:
    print("Next Date is: %d/%d/%d" % (date,month,year))

###########################################################################################################    

#3.) Write a python program to create a list of tuples with the first element as the number and second element as the square of the number
print("\nTHE SOLUTION OF QUESTION 3 :\n")
# TAKING A LIST INPUT
list_in = eval(input("Enter the list: "))
# IF USER ENTER ONLY ONE INTEGER
if type(list_in) is int:
    print(f"Output: ({list_in},{list_in**2})")

else:
    list_out = []
    for i in list_in:
        # CREATING REQUIRED LIST OF TUPLES (NUMBER,IT'S SQUARE) 
        list_out.append((i, i**2))                                                                                     
    print("Output:", list_out)

################################################################################################################

#4.) Write a program to prompt the user for a grade between 4 and 10 and print the performance
print("\nTHE SOLUTION OF QUESTION 4 :\n")
while True:
    grade=int(input("ENTER YOUR GRADE : "))
    if 4<=grade<=10:
        if grade==10:
            print("YOUR GRADE IS A+ AND OUTSTANDING PERFORMANCE")
            break
        elif 9<=grade<10:
            print("YOUR GRADE IS A AND EXCELLENT PERFORMANCE")
            break
        elif 8<=grade<9:
            print("YOUR GRADE IS B+ AND VERY GOOD PERFORMANCE")
            break
        elif 7<=grade<8:
            print("YOUR GRADE IS B AND GOOD PERFORMANCE")
            break
        elif 6<=grade<7:
            print("YOUR GRADE IS C+ AND AVERAGE PERFORMANCE")
            break
        elif 5<=grade<6:
            print("YOUR GRADE IS C AND BELOW AVERAGE PERFORMANCE")
            break
        elif 4<=grade<5:
            print("YOUR GRADE IS D AND POOR PERFORMANCE")
            break
    else:
        print("ERROR!!")
        print(" PLEASE ENTER GRADE FROM 4 TO 10")

##################################################################################################################

#5.) Write a python program to print following pattern.
print("\nTHE SOLUTION OF QUESTION 5 IS :\n")
# CREATING LOOP FOR ROWS
for i in range(6):
# GETTING ASCII VALUE A
    initial=ord('A')
# CREATING LOOP FOR COLUMNS
    for j in range(11):
        if i<=j<11-i:
# CONVERTING ASCII VALUES TO ALPHABET
         print(chr(initial),end='')
         initial+=1
        else:
            print(" ",end='')
    print()

############################################################################################################################

#6.) Write a python program that repeatedly ask user to enter name and SID of students and store them in a dictionary.

print("\nTHE SOLUTION OF QUESTION 6 IS :\n")
dictionary1=dict()
# CREATING A LOOP FOR ENTERING NAMES AND SIDS
while True:
    name=input("ENTER THE NAME : ")
    sid=int(input(f"ENTER THE SID OF {name}: "))
    dictionary1[sid]=name
    print("\nYou have entered %d value(s) " % len(dictionary1))
# CREATING ANOTHER LOOP TO ASK FOR MORE VALUES
    while True:
        ask_data = input("Do you want to enter more data? ").lower()
        if ask_data in ("n","no"):
            ask_data = 0
            break
        elif ask_data in ("y","yes"):
            ask_data = 1
            break
        else:
            print("\nPlease say yes or no")
            continue
    if ask_data == 0:
        break

print("PART A")
#A.) Print students details stored in the dictionary
for i in dictionary1:
    print(f"\tTHE SID OF \'{dictionary1[i]}\'   is   \'{i}\'")

print("PART B")
#B.) Sort dictionary using Student names
dictionary2=dict()
# SORTING VALUES OF DICTIONARY
for sorted_value in sorted(dictionary1.values()):
    for key,value in dictionary1.items():
        if value==sorted_value:
            dictionary2[key]=value

for i in dictionary2:
    print(f"THE SID OF \'{dictionary2[i]}\'   is   \'{i}\'")

print("PART C")
#C.) Sort dictionary using SID
dictionary3=dict()
# SORTING KEYS OF DICTIONARY
for sorted_key in sorted(dictionary1):
    for key,value in dictionary1.items():
        if key==sorted_key:
            dictionary3[key]=value

for i in dictionary3:
    print(f"THE SID OF \'{dictionary3[i]}\'   is   \'{i}\'")

print("PART D")
#D.) Search a student detail with SID and print name of the student

while True:
    search_sid=int(input("ENTER SID WHICH YOU WANT TO SEARCH : "))
    if search_sid in dictionary1:
        print(f"THE NAME OF THE STUDENT WHOSE SID IS \'{search_sid}\' IS \'{dictionary1[search_sid]}\' ")
        break
    else:
        print(f"PLEASE ENTER A VALID SID\nGIVEN LIST : {list(dictionary1.keys())} ")

#################################################################################################################################

#7.) Write a python program to print Fibonacci sequences also print average of the resultant series.
print("\nTHE SOLUTION OF QUESTION 7 IS :\n")
n=int(input("HOW MANY TERMS OF FIBONACCI SERIES DO YOU WANT : "))
sum=0
# USING RECURSION
def fab(n):
# DEFINING BASE VALUES
    if n==0 or n==1:
        return 1
    else:
# FUNCTION CALLING ITSELF
        return fab(n-1)+fab(n-2)
for i in range(n):
    print(f"{fab(i)}",end=" ")
    sum=sum+fab(i)

average=sum/n
print("\nAverage is : %0.2f" %average)

#######################################################################################################################

#8.) Given the sets below, write python statements to create the following: 

print("\nTHE SOLUTION OF QUESTION 8 :\n")
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

print("PART A ")
#A.) Create a new set of all elements that are in SET 1 and SET 2 but not both 
resultant_set=(set1|set2)-(set1&set2)
print(resultant_set)

print("\nPART B ")
#B.) Create a new set of all elements that are in only one of the three sets SET 1 ,SET 2,SET 3
resultant_set=(set1^set2^set3)
print(resultant_set)

print("\nPART C ")
#C.) Create a new set of elements that are exactly in two of the sets
resultant_set=((set1&set2)|(set2&set3)|(set3&set1))-(set1&set2&set3)
print(resultant_set)

print("\nPART D ")
#D.) Create a new set of all integers in the range 1 to 10 that are not in SET1
s=set() 
for i in range(1,11):
    if i not in set1:
       s.add(i)
new_set=s
print(new_set)

print("\nPART E ")
#E.) Create a new set of all integers in the range 1 to 10 that are not in SET1, SET2 and SET3
a=set()
for i in range(1,11):
    if i not in set1: 
        if i not in set2:
         if i not in set3:
          a.add(i)
new_set=a
print(new_set)
