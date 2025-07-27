# Q1 write a program to accept two numbers as command line argument and display their sum.

import sys
if len(sys.argv) != 3:
    print("number is reguired")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    sum = num1 + num2
    print(sum)
    
# Q2 write a program to accept a welcome message through command line argument and display the file name along with the welcome message.

import sys
import os
def greet():
    file_name = os.path.basename(sys.argv[0])
    if len(sys.argv) > 1:
        welcome_message = " ".join(sys.argv[1:])
        print(f"File Name: {file_name}")
        print(f"welcome message: {welcome_message}")
    else:
        print("please provide a welcome message as a command line argument.")
        
# Q3 write a program to accept 10 number through command line argument and calculate the sum of prime number among them.

import sys
def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2,(num**0.5)-1):
            if i%num == 0:
                return False
    return True

if len(sys.argv) != 11:
    print("program required: num1 num2 num3 ---num10")
    sys.exit(1)
prime_sum = 0
for i in range(1, 11):
    num = int(sys.argv[i])
    if is_prime(num):
        prime_sum += num
print(f"The sum of prime number is: {prime_sum}")