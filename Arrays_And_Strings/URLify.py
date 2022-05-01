'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr 3ohn Smit h 13
Output: "Mr%203ohn%20Smith"
Hints: #53,0118 

'''

def Urlify(string):
    return "%20".join(tuple(string.strip().split(" ")))

if __name__ == '__main__':
    str1 = input("Enter String >> ")
    answer = Urlify(str1)
    print(answer)