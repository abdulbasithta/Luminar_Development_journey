# words =["hai","hello","hai","goodmorning","hello","morning"]

# write a program to display frequency

text ="this is python program this python program is simple"

words=text.split(" ") # ['this', 'is', 'python', 'program', 'this', 'python', 'program', 'is', 'simple']

word_count ={}

for w in words:

    if w in word_count:

        word_count[w] +=1

    else:

        word_count[w] =1

print(word_count)

for k,v in word_count.items():

    if v>1:

        print(k,v)