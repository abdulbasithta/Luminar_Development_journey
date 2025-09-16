
"""word1 ="silent"

word2 ="listen"

if sorted(word1) == sorted(word2):

    print("anagram")

else:

    print("not anagram")"""


def is_anagram(word1,word2):

    is_anagram = True

    if sorted(word1) != sorted(word2):

        is_anagram = False

    return is_anagram

print(is_anagram("silent","listen"))