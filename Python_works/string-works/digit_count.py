
# Digit count

text="python has more than  3 frameworks 1 django 2 flask >@"

digit_count =0

for ch in text:

    if ch.isdigit():

        digit_count +=1

print("Digit count:", digit_count)