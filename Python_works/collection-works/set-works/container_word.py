
source_word="chicken"

target_word="hence"

s_word_set=set(source_word)

t_word_set=set(target_word)

is_container_word=t_word_set.issubset(s_word_set)

print(is_container_word)