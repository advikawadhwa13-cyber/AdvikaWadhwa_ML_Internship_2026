#Assignment 2

#a sum of first 10 natural numbers
sum=0
for i in range(1,11):
    sum+=i
print(sum)

#b factorial of a number
factorial=1
num=int(input("Enter number:"))
for i in range(1,num+1):
    factorial*=i
print(factorial)

#c Fibonacci Series
x=[0,1]
n=int(input("Enter number:"))
for i in range(3,n+1):
    y=x[-1]+x[-2]
    x.append(y)
print(x)

#d largest among 3 numbers
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))

if num1>num2:
    if num1>num3:
        print(num1,"is greater") # 1>2>3 or 1>3>2
    elif num3>num1:
        print(num3,"is greater") #3>1>2

if num2>num1:
    if num2>num3:
        print(num2,"is greater") #2>3>1 or 2>1>3
    elif num3>num2:
        print(num3,"is greater") #3>2>1

if num1==num2:
    if num1>num3:
        print(num1,"is greater")
    elif num3>num1:
        print(num3,"is greater")
    elif num1==num3 and num3==num2:
        print("all are equal")

if num2==num3:
    if num1>num2:
        print(num1,"is greater")
    elif num2>num1:
        print(num2,"is greater")

if num1==num3: 
    if num3>num2:
        print(num3,"is greater")
    elif num2>num3:
        print(num2,"is greater")

# using max() function
maximum=max(num1,num2,num3)
print(maximum,"is greater")

#e Student Report
# Inputting Student's Detail
student_name=input("Enter Student's Name:")
student_city=input("Enter Student's City:")

#Inputting student's marks
sub1=int(input("Enter marks of subject 1:"))
sub2=int(input("Enter marks of subject 2:"))
sub3=int(input("Enter marks of subject 3:"))
sub4=int(input("Enter marks of subject 4:"))

#Calculating Result
total_marks=sub1+sub2+sub3+sub4
percentage=(total_marks/400)*100

#Calculating Grade
if percentage >= 90:
    print(student_name, "living in", student_city, "scoring", percentage, "has got A+ grade")

elif percentage >= 85:  # 85 <= percentage < 90
    print(student_name, "living in", student_city, "scoring", percentage, "has got A grade")

elif percentage >= 80:  # 80 <= percentage < 85
    print(student_name, "living in", student_city, "scoring", percentage, "has got B+ grade")

elif percentage<80:
    print(student_name,"living in",student_city,"must try for improvement")



