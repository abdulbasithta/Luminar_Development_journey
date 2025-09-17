# program to count the frequency of each character in a given string

def char_frequency(string):

    frequency = {}

    for ch in string:

        if ch in frequency:

            frequency[ch] += 1

        else:
            
            frequency[ch] = 1

    return frequency

print(char_frequency("hello world"))