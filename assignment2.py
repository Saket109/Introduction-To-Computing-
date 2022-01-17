print("QUESTION 1.)")
input_string="Python is a case sensitive language"
#a.) FIND THE LENGTH OF THE INPUT STRING.
print("PART A")
print(len(input_string))

#b.) REVERSE THE ORDER OF THE STRING IN ONE LINE CODE.
print("PART B")
print(input_string[::-1])

#c.) USING SLICING FUNCTION STORE "A CASE SENSITIVE" IN NEW STRING.
print("PART C")
sliced_string=input_string[10:26]
print(f"SLICED STRING IS:  {sliced_string}")

#d.) REPLACE "A CASE SENSITIVE" WITH "OBJECT ORIENTED".
print("PART D")
print(input_string.replace("a case sensitive","object oriented"))

#e.) FIND INDEX OF SUBSTRING "A" IN THE GIVEN INPUT STRING.
print("PART E")
print(input_string.find("a"))

#f.) REMOVE THE WHITE SPACES FROM THE GIVEN INPUT STRING.
print("PART F")
print(input_string.replace(" ",""))


##################################################################################################

print("QUESTION 2.)")
# STORE YOUR NAME,SID,DEPARTMENT,CGPA INTO DIFFERENT VARIABLE.THEN PRINT WITH THE HELP OF STRING FORMATTING
name="Saket Ahlawat"
SID=21105105
department="ECE"
CGPA=10
print(f"Hey,{name} Here!\nMy SID is {SID}\nI am from {department} department and my CGPA is {CGPA}")

####################################################################################################


print("QUESTION 3.)")
# FOR A=56 AND B=10 WITH THE HELP OF BITWISE OPERATOR CALCULATE THE FOLLOWING:
a=56
b=10
print("a&b is: ",a&b)
print("a|b is: ",a|b)
print("a^b is: ",a^b)
print("a<<2:",a<<2,"\tb<<2: ",b<<2)
print("a>>2:",a>>2 ,"\tb>>4: ",b>>4)

########################################################################################################

print("QUESTION 4.)")
# WRITE A PYTHON PROGRAM TO FIND THE GREATEST OF THREE NUMBERS ENTERED BY THE USER.
num1=int(input("ENTER THE FIRST NUMBER: "))
num2=int(input("ENTER THE SECOND NUMBER: "))
num3=int(input("ENTER THE THIRD NUMBER: "))
if(num1>num2):
    if(num1>num3):
        print(f"THE GREATEST NUMBER IS {num1}")
    else:
        print(f"THE GREATEST NUMBER IS {num3}")
else:
    if(num2>num3):
        print(f"THE GREATEST NUMBER IS {num2}")
    else:
        print(f"THE GREATEST NUMBER IS {num3}")

###########################################################################################################

print("QUESTION 5.)")
# WRITE A PYTHON PROGRAM TO CHECK IF THE WORD "NAME" IS PRESENT IN THE STRING ENTERED BY THE USER.
string=input("ENTER ANY STRING")
s=string.find("name")
if s==-1:
    print("NO")
else:
    print("YES")   

#############################################################################################################

print("QUESTION 6.)")
a=int(input("ENTER LENGTH OF FIRST SIDE OF TRIANGLE: "))
b=int(input("ENTER LENGTH OF SECOND SIDE OF TRIANGLE: "))
c=int(input("ENTER LENGTH OF THIRD SIDE OF TRIANGLE: "))
if a+b>c and b+c>a and a+c>b:
    print("YES")
else:
    print("NO")
