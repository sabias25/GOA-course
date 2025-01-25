# Write a function that takes a sentence, a word, and an index, and inserts the word into the sentence at the given index.

def insert_word(sentence, word, index):
    part1 = sentence[:index]
    part2 = sentence[index:]
    new_sentence = part1 + word + part2
    print(new_sentence)


insert_word("მე მიყვარს პროგრამირება.", "Python ", 9)