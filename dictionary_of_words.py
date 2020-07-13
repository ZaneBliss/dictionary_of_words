"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["log"] = "a part of the trunk or a large branch of a tree that has fallen or been cut off"
word_definitions["laptop"] = "a computer that is portable and suitable for use while traveling"
word_definitions["cat"] = "a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["log"])
print(word_definitions["laptop"], "\n")

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for word, definition in word_definitions.items():
    print(f"The definition of {word} is {definition} \n")
