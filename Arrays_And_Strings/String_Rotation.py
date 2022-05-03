'''
String Rotation; Assume you have a method isSubs t rin g which checks if one word is a substring
of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one
call to isSubs t rin g [e.g., "wate r bottle " is a rotation oP'erbottlewat"),
Hints: #34, #88,#W4 

'''
def String_Rotation(s1, s2):
    #edge case
    if(len(s1) != len(s2)):
        return False
    
    indx = s1.index(s2[0])
    rot_string = s1[indx:] + s1[:indx]
    
    if (rot_string == s2):
        return True
    else:
        return False

if __name__ == "__main__":
    s1 = input("Enter First String >> ").strip()
    s2 = input("Enter Second String >> ").strip()

    answer = String_Rotation(s1, s2)
    print(answer)