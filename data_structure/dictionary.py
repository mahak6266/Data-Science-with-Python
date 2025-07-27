# Q1 write a program to add a key and value to a dictionary

dictionary = {0: 10, 1: 20}
dictionary[2] = 30
print(dictionary)

# Q2 write a program to concatenate the following dictionaries to create a new one.
# sample dictionary :
# dic1 = {1:10, 2:20} dic2 = {3:30, 4:40} dic3 = {5:50, 6:60}
# expected result : {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
concatenate_dic = {**dic1, **dic2, **dic3}
print(concatenate_dic)

# Q3 write a program to check if a given key already exist in a dictionary
dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = 3
if key in  dict:
    print(f"given key {key} already exist in a dictionary{dictionary}")
else:
    print(f"given key {key} does not exist in a dictionary{dictionary}")

# Q4 write a program to iterate over a dictionary using loop and print the key alone , value alone 
# and both key and values.

dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("The keys are:")
for key in dictionary:
    print(key)
print("The values are:")
for value in dictionary.values():
    print(value)
print("Both keys and values are:")
for key, value in dictionary.items():
    print(f"{key}:{value}")
    
# Q5 write a program to prepare a dictionary where the keys are numbers between 1 and 15 
# (both include) and the values are square of the keys

dict = {}
for i in range(1, 16):
    dict[i] = i*i
print(dict)

# Q6 write a program to sum all values in a dictionary, considering the values will be of int type

dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
sum = 0
for value in dict.values():
    sum += value
print(sum)

