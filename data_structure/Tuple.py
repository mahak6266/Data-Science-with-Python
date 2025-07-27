# Q1 write a program to print the 4th element from first and 4th element from last in a tuple.

tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
fourth_element_from_first = tuple[3]
fourth_element_from_last = tuple[-4]
print(fourth_element_from_first, fourth_element_from_last)

# Q2 write a program to check whether an element exist in a tuple or not.

tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
element_to_be_check = 40
if element_to_be_check in tuple:
    print(f"{element_to_be_check} is exist in tuple{tuple}")
else:
    print(f"{element_to_be_check} is not exist in tuple{tuple}")

# Q3 write a program to convert list into tuple

list = [1, 2, 3, 4, 5, 6, 7]
print(type(list))
tuple = tuple(list)
print(type(tuple))

# Q4 write a program to find a index of an item in a tuple.

tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
item_to_be_find = 50
index = tuple.index(item_to_be_find )
print(f"{item_to_be_find} is present at index {index}")

# Q5 write a program to replace last value of tuple in a list to 100
# sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# expected output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

li = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
modified_list = []
for tpe in  li:
    temp_list = list(tpe)
    temp_list[-1] = 100
    temp_tuple = tuple(temp_list)
    modified_list.append(temp_tuple)
print("original list:", li)
print("modified list", modified_list)



