#write a program to create a list of 5 integer and display the list items. Access individual 
# elements through index
list = [2, 4, 6, 8, 10]
print("The list is ", list)
print("The element at 0th index:", list[0])
print("The element at 1th index:", list[1])
print("The element at 2th index:", list[2])
print("The element at 3th index:", list[3])
print("The element at 4th index:", list[4])

# write a program to append a new item at the end of the list

list = [2, 4, 6, 8, 10]
list.append(12)
print("appended list- ", list)

# write a program to reverse the order of the items in the list.

list = [2, 4, 6, 8, 10]
reverse_list =[]
for i in range(len(list)-1,-1,-1):
    reverse_list.append(list[i])
print(reverse_list)

# write a program to print a number of occurence of a specified element in a list

list = [1,1,2,3,2,4,3,6,6,4,4]
ele = 3
count = 0
for element in list:
    if element == ele:
        count += 1
print(count)

# write a program to append the items of list1 to list2 in the front

list1 = [2, 4, 4, 6, 5]
list2 =[6, 7]

for item in reversed(list1):
    list2.insert(0, item)
print(list2)

# write a program to insert a new item before the second element in existing list.

list = [2,4,5,7,5]
new_item = 3
list.insert(1, new_item)
print(list)

# write a program to remove the item from a specified index in a list.

list = [2,4,5,7,5]
index_to_remove = 2
list.remove(list[index_to_remove])
print(list)

# write a program to remove the first occurrence of a specified element from a list.

list = [1,1,2,3,2,4,3,6,6,4,4]
ele_to_rem = 3
index = list.index(ele_to_rem)
list.pop(index)
print(list)



