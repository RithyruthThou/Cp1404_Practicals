word_to_count = {}
sentence = "this is a collection of words of nice words this is a fun thing it is"
words = sentence.split()
for word in words:
    word_count = word_to_count.get(word, 0)
    word_to_count[word] = word_count + 1
print(word_to_count.keys())
words = list(word_to_count.keys())
print(word_to_count)
print(words)
words.sort()
print(words)
length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, length, word_to_count[word]))

