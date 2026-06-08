#Assignment 3

#a print first 10 natural numbers
def display():
    for i in range(1,11):
        print(i)
display()

#b sum of first N natural numbers
def sum(n):
    return (n*(n+1))/2
print(sum(5))

#c reversing a number
def reverse(num):
   if num>0:
       return int(str(num)[::-1])
   elif num<0:
       return int(str(abs(num))[::-1])
print(reverse(21))

#d counting digits in a number
def count_digits(num1):
    count=0
    while num1 !=0:
        num1//=10
        count+=1
    print(count)
count_digits(123)

#e palindrome number
def check_palindrome(num2):
    if str(num2)==str(num2)[::-1]:
        print(num2,"is a palindrome")
    else:
        print(num2,"is not a palindrome")
check_palindrome(121)

#f Fibonacci Series
def fibb_series(n):
    a=[0,1]
    for i in range(3,n+1):
        b=a[-1]+a[-2]
        a.append(b)
        print(a)
fibb_series(5)  

#g reading data from file
with open("Student.txt","r") as file:
    content=file.read()
print(content)

#h division by 0 using exception handling
num_1=int(input("Enter number1:"))
num_2=int(input("Enter number2:"))
try:
    div=num_1/num_2
    print(div)
except ZeroDivisionError:
    print("division by zero is not possible")

#i Student class with name and marks
class student:
    def __init__(self,name,marks):
        self.name=name
        print(self.name)
        self.marks=marks
        print(marks)
student1=student("Ria",90)       
student2=student("Rohan",89) 



