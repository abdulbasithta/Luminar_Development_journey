# consonant count

text="python has more than  3 frameworks 1 django 2 flask >@"

consonant_count =0

vowels = "aeiou"

for ch in text:

    if ch.isalpha() and ch not in vowels:

        consonant_count +=1
    
print("Consonant count:", consonant_count)