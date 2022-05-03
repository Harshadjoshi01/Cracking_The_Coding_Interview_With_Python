'''
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints: #92, if 110

'''

from tokenize import String


def Str_compress(s):
    comp_str = ""
    count_char = 1
    for i in range(len(s)):               #if i is greater than zero
        if (i > 0 and s[i] == s[i-1]):
            count_char += 1
        elif(i > 0 and s[i] != s[i-1]):
            comp_str += s[i-1] + str(count_char)
            count_char = 1

    final_str = comp_str + s[-1] + str(count_char)         #handling last char of string
    if (len(final_str) > len(s)):
        return s
    else: 
        return final_str

if __name__ == '__main__':
    s = input("Enter string >> ").strip()
    answer = Str_compress(s)
    print(answer)