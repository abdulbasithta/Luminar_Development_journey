
# alphabetic count

text="python has more than  3 frameworks 1 django 2 flask >@"

alpha_count =0

for ch in text:

    if ch.isalpha():

        alpha_count +=1

print("Alphabetic count:", alpha_count)