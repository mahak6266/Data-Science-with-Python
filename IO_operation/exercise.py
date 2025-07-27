# Q1 write a program to read the entire content from a text and display it to the user.

with open("C:\Users\91626\OneDrive\Documents\Desktop\txt file\text_file.txt", "r") as file:
    content = file.read()
    print(content)
    file.close()
    
# Q2 write a program to read first n lines from a txt file. Get n as user input.

def read_n_lines(filepath, n):
    lines_read = []
    with open(filepath, "r") as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            lines_read.append(line)
        file.close()
    return lines_read
file_name = "C:\\Users\\91626\\OneDrive\\Documents\\Desktop\\txt file\\text_file.txt"
num_lines_to_read = int(input("Enter the numner of lines to read: "))
while True:
    if num_lines_to_read < 0:
        print("invalid input. please enter positive integer for the number of lines")
    else:
        break
first_n_lines = read_n_lines(file_name, num_lines_to_read)
for line in first_n_lines:
    print(line)
    
# Q3 write a program to accept a input from user and append it to a text file.

def append_input(filepath, text):
    with open(filepath, "w") as file:
        file.write(text + "/n")
        file.close()
   
user_input = input("Enter the text to be added: ")
file_name = input("enter file path in txt file")
append_input(file_name, user_input)
print("sucessfully append the user input in the given text file")  

# Q4 write a program to read content from a text file and store each line into a list.

file_name = input("enter file path in txt file")
file_lines = []
with open(file_name, "r") as file:
    for line in file:
        file_lines.append(line)
    file.close()
print("content of the file stored in a list")
for line in file_lines:
    print(line)
    
# Q5 write a program to find the longest word from the text content, assuming that the file will have only one longest word in it.

def longest_word(filepath):
    with open(filepath, "r") as file:
        words = file.read().split()
        if not words:
            return "file is empty"
        longest_word = ""
        for word in words:
            cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
            if len(cleaned_word) > len(longest_word):
                longest_word = cleaned_word
        file.close()
    return longest_word
file_name = input("enter file path in txt file") 
result = longest_word(file_name)
print("longest word in a file: ",result)

# Q6 write a program to count frequency of a user entered word in text file.

def count_frequency(filepath, search_word):
    word_count = 0
    with open(filepath, "r") as file:
        for line in file:
            for word in line.split():
                words_in_line = word.strip('.,!?:;"\'()[]{}').lower()
                word_count += words_in_line.count(search_word)
    return word_count
file_name = input("enter file path in txt file")
word = input("enter the word to be search: ")
print(count_frequency(file_name, word))
        

        


