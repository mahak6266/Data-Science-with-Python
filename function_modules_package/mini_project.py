'''write a python function that accept a hyphen-separated sequence of colors as input and return the colors in a hyphen-separated 
 sequence after them alphabetically.
 constraint: All the colors will ne completely in either lower case or upper case.
 Sample input 1: green-red-yellow-black-white
 Sample output: black-green-red-white-yellow
 Sample input 1: PINK-BLUE-TAN-PIRPLE
 Sample output: BLUE-PINK-PURPLE-TAN'''

def sort_color(colors_sequence):
    colors = colors_sequence.split("-")
    colors.sort()
    sorted_color_sequence = '-'.join(colors)
    return sorted_color_sequence

colors_sequence1 = "green-red-yellow-black-white"
sorted_color_sequence1 = sort_color(colors_sequence1)
colors_sequence2 = "PINK-BLUE-TAN-PIRPLE"
sorted_color_sequence2 = sort_color(colors_sequence2)
print(sorted_color_sequence1)
print(sorted_color_sequence2)

'''Function Name                                         Task
 ispalindrome(name)          Given the user as input, this function should tell us whether the name is a palindrome or not
 count_the_vowel(name)       Given the user as input, this function should tell us hoe many vowel are present in it.
 frequncy_of_letters(name)   Given the user as input, this function should tell us how many times each letter appear in the name.
 Note: name will be completely in either lower case or upper case.
 Import the module in another python script and test the function by passing an appropriate input.
 Sample input: bob
 Sample output:
 yes it is pallindrome
 No. of vowels: 1 
 Frequecy of letter: b-2, o-1'''
 
def ispallindrom(name):
    if name == name[::-1]:
        return "Yes it is pallindrome"
    else:
        return"No it is not pallindrome"
        
def count_the_vowel(name):
    count = 0
    for char in name:
        if char in ['a','e','i','o','u'] and ['A','E','I','O','U']:
            count += 1
    return count

def frequency_of_letter(name):
    name = name.lower()
    freq_letter = {}
    for char in name:
        if 'a' <= char <= 'z':
            freq_letter[char] = name.count(char)
    return freq_letter
 


        
        
        