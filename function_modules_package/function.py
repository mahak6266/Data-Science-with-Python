# Q1 write a function to return the sum of all number in a list

def sum(list):
    sum = 0
    for num in list:
        sum += num
    return sum
list = [8, 2, 3, 0, 7]
print(sum(list))

# Q2 write a function to return the reverse of a string.

def reverse(string):
    reverse_string = string[::-1]
    return reverse_string
string = "1234abcd"
print(reverse(string))

# Q3 write a function to calculate and return the factorial of a number(a non negative integer)

def factorial(n):
    if n < 0:
        return "factorial is not define for negative integer"
    elif n ==0:
        return 1
    else:
        res = 1
        for i in  range(1, n+1):
            res *= i
    return res

# Q4 write a function that accept a string and print the number of upper case letter and lower case 
# letter in it 

def upper_lower(string):
    uppercase_count = 0
    lowercase_count = 0
    for char in string:
        if "A" < char < "Z":
            uppercase_count += 1
        if "a" < char <"z":
            lowercase_count += 1
    print("Number of upper case letter in a given string: ",uppercase_count)
    print("Number of lower case letter in a given string: ",lowercase_count)
    
# Q5 write a function to print the even number from a given list. List is passed to the function as an argument.
# sample list: [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
# Expected result: [2, 4, 6, 8]

def even(list):
    res = []
    for i in list:
        if i%2 == 0:
            res.append(i)
    return res
list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
print(even(list))

# Q6 write a function that take a number as a parameter and check whether the number is prime or not

def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2,(num**0.5)-1):
            if i%num == 0:
                return False
    return True
    
        
    