# program to check if a string is a palindrome (ignore spaces and case)

def is_palindrome(string):

    flag = True

    clean_string = string.lower().replace(" ","")

    if clean_string != clean_string[::-1]:

        flag = False

    return flag

print(is_palindrome("Mala yaLam"))


