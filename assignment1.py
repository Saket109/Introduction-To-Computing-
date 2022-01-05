# 1.) WRITE A PYTHON PROGRAM TO FIND THE AVERAGE OF THREE NUMBERS ENTERED BY THE USER.
num1=int(input("ENTER FIRST NUMBER: "))
num2=int(input("ENTER SECOND NUMBER: "))
num3=int(input("ENTER THIRD NUMBER: "))
average=(num1+num2+num3)/3
print(f"the average of these three numbers is: {average}")

# 2.) WRITE A PYTHON PROGRAM TO COMPUTE A PERSON'S INCOME TAX. 
gross_income=float(input(" ENTER THE GROSS INCOME TO THE NEAREST PENNY: "))
dependents=int(input(" ENTER NUMBER OF DEPENDENTS: "))
standard_deduction= 10000
dependent_deduction= 3000
tax_rate=0.2
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependents)
tax=taxable_income*tax_rate
print(f" THE TAX IS : {tax}")

# 3.) WRITE A PYTHON PROGRAM TO STORE DIFFERENT DATA TYPE VALUES INTO A LIST.
print(" THE BELOW IS THE LIST OF DIFFERENT DATA TYPE VALUES : ")
student=[21105105,"saket",'male',"ECE",9.8]
print(student)

# 4.) WRITE A PYTHON PROGRAM TO ENTER MARKS OF 5 STUDENTS INTO A LIST AND DISPLAY THEM IN A SORTED MANNER.
m1=int(input("ENTER MARKS OF STUDENT 1: "))
m2=int(input("ENTER MARKS OF STUDENT 2: "))
m3=int(input("ENTER MARKS OF STUDENT 3: "))
m4=int(input("ENTER MARKS OF STUDENT 4: "))
m5=int(input("ENTER MARKS OF STUDENT 5: "))
list=[m1,m2,m3,m4,m5]
list.sort()
print(list)

# 5.) (a):
list_color=['RED','GREEN','WHITE','BLACK','PINK','YELLOW']
list_color.pop(3)
print(list_color)

#  (b)
list_color=['RED','GREEN','WHITE','BLACK','PINK','YELLOW']
list_color[3:5]=['PURPLE']
print(list_color)
