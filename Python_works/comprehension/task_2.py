
words=["hai","hello","goodevening","hello","hai","goodmorning"]

# create a new words convert all words into uppercase

upper_words=[w.upper() for w in words]
print(upper_words)

# create a new dictionary from words set word as key and value as lenght of that word

dic_words={w:len(w) for w in words}
print(dic_words)

