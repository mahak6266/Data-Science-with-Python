'''You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.
You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after discount?
Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.
Note:
  i. Data is stored in a text file purchase-1.txt
  ii. Each line contains one item's details.
  iii. Item name and price is separated by a space.
  iv. You have to enter the file name during run time.
Sample input:
purchase-1.txt
Biscuit 35
icecream 50
(blank line)
milk free
soup free
(blank line)
Discount 5
Sample output:
Enter a file name: purchase-1
No. of items purchase: 3
No. of free items: 2
Amount to pay: 135
Discount given: 5
Final amount paid: 130
'''
def purchase_file(filename):
    total_items = 0
    free_items = 0
    total_amount = 0
    discount = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                item_name = parts[0]
                if item_name.lower() == "discount":
                    try:
                        discount = int(parts[1])
                    except ValueError:
                        print(f"Warning: Invalid discount value {parts[1]}. skipping dicount")
                    continue
                if parts[1] == "free":
                    free_items += 1
                else:
                    total_items += 1
                    try:
                        price = int(parts[1])
                        total_amount += price
                    except ValueError:
                        print(f"Warning. Invalid price value {parts[1]}. skipping this item from the total amount")
                        total_items -= 1
                file.close()
    except FileNotFoundError:
        print(f"ERROR: file {filename} not exist")
        return None
    except Exception as e:
        print(f"ERROR: An unexpected error occured: {e}")
        return None
    final_amount = total_amount - discount
    return total_items, free_items, total_amount, discount, final_amount

file_name = input("Enter a file name: ")
details = purchase_file(file_name)
if details:
    total_items, free_items, total_amount, discount, final_amount = details
    print(f"No. of items purchase: {total_items}")
    print(f"No. of free items: {free_items}")
    print(f"Amount to pay: {total_amount}")          
    print(f"Discount given: {discount}")        
    print(f"Final amount paid: {final_amount}")