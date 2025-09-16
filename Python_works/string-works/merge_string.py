
# Merge string

"""word1 ="ABCD"

word2 ="PQRS"

merged_st =""

for index in range(0,len(word1)):

    concat_char = word1[index] + word2[index]

    merged_st += concat_char

print(merged_st)"""



def merge_string(word1,word2):

    result =""

    for index in range(0,len(word1)):

        concat_char = word1[index] + word2[index]

        result += concat_char

    return result

print(merge_string("ABCD","PQRS"))