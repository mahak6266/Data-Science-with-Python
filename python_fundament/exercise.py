#Q1. write a program to check if a given number is positive, negative or zero.

num = input("Enter a number:")
if num<0:
    print(f"{num} is a negative number")
elif num>0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a zero")  

#Q2. write a program to check if a given number is odd or even.

num = input("Enter a number:")
if num%2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd nukmber")

#Q3. given two non negative values, print true if they have the last digit.

num1 = input("Enter a first number:")
num2 = input("Enter a second number:")
if num1[-1] == num2[-1]:
    print("true")
    
#Q4 write a program to print number from 1 to 10 in a single row with one tab space.

for i in range(1,11):
    print(i,end=" ")
    
#Q5 write a program to print even number between 23 and 57. Each number should be printed in a seperate row.

for i in range(23,57):
    if i%2==0:
        print(i)
        
#Q6 write a program to check if a given number is prime or not.
def check_prime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
number = input("Enter a number: ") 
if check_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
    
#Q7 write a program to print prime number between 10 and 99.
def check_prime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
for i in range(10,100):
    if check_prime(i):
        print(i, end=" ")
        
#Q8 write a program to print the sum of all the digits of a given number.
number = input("Enter a number:")
sum = 0
for digit in number:
    sum += digit
print(sum)

#Q9 write a program to reverse a given number and print

num = input("Enter a number:")
rev_number = 0
while num>0:
    remainder = number%10
    rev_number = rev_number*10+remainder
    num //= 10
print(rev_number)

#Q10. write a program to find if the given number is pallindron or not.

num = input("Enter a number:")
rev_number = 0
while num>0:
    remainder = number%10
    rev_number = rev_number*10+remainder
    num //= 10
if number == rev_number:
    print("given number is pallindron")
else:
    print("given number is not pallindron")