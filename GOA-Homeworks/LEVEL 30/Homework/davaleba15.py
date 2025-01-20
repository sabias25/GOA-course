# Count the number of times the word "the" appears in a given paragraph.

def count_the(paragraph):
    num = paragraph.lower().split() 
    return num.count("the")

paragraph = input("Enter a paragraph: ")
print("The word 'the' appears", count_the(paragraph), "times.")