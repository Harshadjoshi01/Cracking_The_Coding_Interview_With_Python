'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations : "taco cat" , "atco cta" , etc. )
Hints: #106, h 0134, § 136
'''

#Solution 1

from operator import countOf
from collections import Counter

def Even_palindrome_check(str):
    count = [0] * 256

    for i in range(len(str)):
        if(count[ord(str[i])] == 0):
            count[ord(str[i])] += 1
        else:
            count[ord(str[i])] -= 1
    
    for i in range(256):
        if (count[i] != 0):
            return False
    
    return True

def Odd_palindrome_check(str):
    count = [0] * 256

    for i in range(len(str)):
        if(count[ord(str[i])] == 0):
            count[ord(str[i])] += 1
        else:
            count[ord(str[i])] -= 1
    
    if (count.count(1) == 1):
        return True
    else:
        return False    

def Palindrome_Permutation_1(str1):
    str1 = "".join(tuple(str1.strip().lower().split(" ")))
    if (len(str1) % 2 == 0):
        return Even_palindrome_check(str1)
    else:
        return Odd_palindrome_check(str1)


def Pal_Per(s):
    cnt = Counter(s)
    odd = 0
    for freq in cnt.values():
        if freq % 2 != 0:
            odd = odd + 1
            if odd > 1:
                return False
    return True


if __name__ == '__main__':
    str = input("Enter String >> ")
    answer = Pal_Per(str)
    print(answer)