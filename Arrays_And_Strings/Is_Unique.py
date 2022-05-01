'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Hints: #44, #117, #132 

'''
'''
PS: Assuming String to be 256 unicoded
'''
from unicodedata import name


def is_Unique(string):
    
    #edge case
    if (len(string) == 1):
        return True
    
    unique_char = [False] * 256

    for char in string:
        if(unique_char[ord(char)] == False):
            unique_char[ord(char)] = True
        else:
            return False
    
    return True

if __name__ == '__main__':
    str1 = input("Enter String >> ")
    answer = is_Unique(str1.strip())
    print(answer)