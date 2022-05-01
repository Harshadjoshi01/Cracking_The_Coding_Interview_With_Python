'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
Hints: #1, #84, #122, #131
'''
'''
PS: Assuming String to be 256 unicoded
'''

def Check_Permutation(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    
    #edge case
    if(len(str1) != len(str2)):
        return False

    count = [0] * 256

    for i in range(len(str1)):
        count[ord(str1[i])] += 1
        count[ord(str2[i])] -= 1
    
    for i in range(256):
        if (count[i] != 0):
            return False
    
    return True

if __name__ == '__main__':
    str1 = input("Enter First Word >> ")
    str2 = input("Enter Second Word >> ")
    answer = Check_Permutation(str1.strip(), str2.strip())
    print(answer)