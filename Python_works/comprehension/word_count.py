
words=["hai","hello","goodmorning","hai","goodevening","hello","hai"]

# word_count={}

# for w in words:

#     if w in word_count:

#         word_count[w]+=1
    
#     else:

#         word_count[w]=1

# print(words.count("hai"))
# print(words.count("hello"))

words_count={w:words.count(w) for w in words}

print(words_count)
