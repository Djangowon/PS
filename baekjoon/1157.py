word = input().upper()
unique_words = list(set(word))

word_count = []
for i in unique_words:
    count = word.count(i)
    word_count.append(count)

if word_count.count(max(word_count)) > 1:
    print("?")

else:
    max_index = word_count.index(max(word_count))
    print(unique_words[max_index])
