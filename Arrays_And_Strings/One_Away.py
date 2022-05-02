'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale , ple - > true
pales , pale - > true
pale , bale - > true
pale , bake - > false
Hints: #23, #97, it 130 

'''
def Replace_str(str1, str2):
    foundDifference = False
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            if(foundDifference):
                return False
            
            foundDifference = True
    return True


def Insert_Remove(str1, str2):
    index1 = 0
    index2 = 0
    while ((index2 < len(str2)) and (index1 < len(str1))):
        if (str1[index1] != str2[index2]):
            if (index1 != index2):
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True  


def One_Away(str1, str2):
    if (str1 == str2):
        return True
    elif (len(str1) == len(str2)):
        return Replace_str(str1, str2)
    elif(len(str1) == len(str2) + 1):
        return Insert_Remove(str2, str1)
    elif(len(str1) + 1 == len(str2)):
        return Insert_Remove(str1, str2)
    else:
        return False

if __name__ == '__main__':
    str1 = input("Enter First String >> ").strip()
    str2 = input("Enter Second String >> ").strip()
    answer = One_Away(str1, str2)
    print(answer)