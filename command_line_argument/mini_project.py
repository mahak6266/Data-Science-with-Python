'''Through commnad line argument three string separated by space to you. Each string is a series of number by hyphen(-). You like all 
the number in string 1 and dislike all number in string 2.
Third string contain the number given to you. Your intial happiness is 0. When you encounter a number which is present in string 1, 
add 1 to your happiness, if it is present in string 2, add -1 to your happiness. Otherwisae, your happiness does not change. Output your 
final happiness at the end
'''
import sys

def happiness(string1, string2, string3):
    liked_number = set(map(int, string1))
    disliked_number = set(map(int, string2))
    evaliated_number = list(map(int, string3))
    happiness = 0
    
    for num in evaliated_number:
        if num in liked_number:
            happiness += 1
        elif num in disliked_number:
            happiness -= 1
    return happiness

if len(sys.argv) != 4:
    print("<string1> <string2> <string3> is required")
    sys.exit(1)
    
s1 = sys.argv[1]
s2 = sys.argv[2]
s3 = sys.argv[3]
happiness = happiness(s1, s2, s3)
print(f"final happiness: {happiness}")


        