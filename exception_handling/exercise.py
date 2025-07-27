# Q1 write a program to accept two number from the user and perform division. If any exception occurs, print an error message or 
# else print the result

def division():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
       
        result = num1 / num2
        print(result)
    except ValueError:
        print("ERROR: Invalid input. Please enter numeric value")
    except ZeroDivisionError:
        print("ERROR: cannot divided by zero.")
    except Exception as e:
        print("program intrupt due to unexpected error: ",e)
        
division()
        
# Q2 write a program to accept a number from the user and check whether it is prime or not. If user enter anything other than number, 
# handle the exception and print an error message.

def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2,(num**0.5)-1):
            if i%num == 0:
                return False
    return True
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
except ValueError:
    print("ERROR: Invalid input. Please enter a valid integer")
except Exception as e:
    print("unexcepted error ocurred: ",e)
    
# Q3 write a program to accept a file name to be opened from the user. If file exist print the content of the file in title case or 
# else handle the exception and print error message.

def print_file_content():
    try:
        filename = input("Enter the file name: ")
        with open(filename, "r") as file:
            content = file.read()
            print(content.title())
    except FileNotFoundError:
        print(f"ERROR: file '{filename}' is not exist in you directory")
    except Exception as e:
        print("unexcepted error ocurred: ",e)
print_file_content()

# Q4 Declare a list with 10 integer and ask the user to enter an index. Check whether the number in that index is positive or negative
# number. If any invalid index is entered, handle the exception and print an error message

def check_index(list):
    try:
        
        index = int(input("Enter an index: "))
        num = list[index]
        if num < 0:
            print(f"{num} is a negative number.")
        elif num > 0:
            print(f"{num} is a positive number.")
        else:
            print(f"{num} is zero")
    except IndexError:
        print("ERROR: Invalid index. Please enter an index within the list range.")
    except ValueError:
        print("ERROR: Invalid input. Please enter an integer for the index.")
list = [1, 3, -5, 3, -8, 7, 0, -4, 6, -2]
check_index(list)