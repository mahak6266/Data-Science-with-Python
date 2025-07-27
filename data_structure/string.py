# Q1 write a program to count the number of upper and lower case letter in a string.

string = "This is Data Science With Python"
upper_count = 0
lower_count = 0
for char in string:
    if "a" < char < "z":
        upper_count += 1
    if "A" < char < "Z":
        lower_count += 1
print("number of upper case letter in a string: ",upper_count)
print("number of lower case letter in a string: ",lower_count)

# Q2 write a program that will check whether a given string is pallindrome or not.

string = "Madam"
s = string.lower(string)
if s == s[::-1]:
    print("given string is pallindrome")
else:
    print("given string is  not pallindrome")
    
# Q3 given a string, return a new string made of n copies of the first 2 char of the 
# original string where n is the length of the string. The string length will be >=2. 
# If input is "Wipro", then output should be "WiWiWiWiWi".

string = "Wipro"
first_two_char = string[:2]
n = len(string)
print(first_two_char * n)

# Q4 given a string, if the first or last character is "x" , return the string without those "x" 
# character, else return the string unchanged. If the input is "xHix", then output is "Hi".

string = "xHix"
n = len(string) -1
if string[0] == "x" and string[-1] == "x":
    print(string[1:(len(string)-1)])
else:
    print(string)
    
# Q5 given a string and a integer n, return a string made of n repetitions of the last n character of 
# the string. You may assume that n is between 0 and the length of the string inclusive. For exampler
# if the input "wipro" and 3, then the out should be "propropro"

string = "Wipro"
n = 3
if 0 < n < len(string):
    sub_string = string[len(string)-n:]
    print(sub_string * n)
else:
    print("invalid the value nof n")