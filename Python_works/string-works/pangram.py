
"""text = "the quick brown for jumbs over lazy do"

alphabets ="abcdefghijklmnopqrstuvwxyz"

is_pangram =True

for al in alphabets:

    if al not in text:

        is_pangram = False

        break

print(is_pangram)"""

def is_pangram(word):

    flag = True

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for al in alphabets:

        if al not in word.lower():

            flag = False

            break

    return flag

print(is_pangram("hello world"))

print(is_pangram("abcdefghijklmnopqrstuvwxyz"))