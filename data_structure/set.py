# Q1 write a program to remove a given item from the set.

set = {"apple", "banana", "pineapple", "watermelon", "jackfruit"}
item_to_removed = "jackfruit"

set.discard(item_to_removed)
print(f"set after remove {item_to_removed}: {set}")

# Q2 write a program to create a union of sets.

set1 = {2, 4, 6, 8, 10}
set2 = {1, 4, 3, 5, 7, 9}
set3 = set1.union(set2)
print(set3)

# Q3 write a program to create a intersection of sets.

set1 = {2, 4, 6, 8, 10}
set2 = {1, 4, 3, 5, 7, 9}
set3 = set1.intersection(set2)
print(set3)

# Q4 write a program to find the maximum and minimum value in a set.

set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
maximum_value = max(set)
minimum_value = min(set)
print("maximum value in a set: ",maximum_value)
print("minimum value in a set: ",minimum_value)