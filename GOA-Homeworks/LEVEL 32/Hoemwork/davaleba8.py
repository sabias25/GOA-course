# Write a function that takes a paragraph and splits it into sentences based on periods.

def split_into_sentences(paragraph):
    sentences = paragraph.split(".")
    sentences = [i.strip() for i in sentences if i.strip()]
    print(sentences)

split_into_sentences("Python არის სასარგებლო.")