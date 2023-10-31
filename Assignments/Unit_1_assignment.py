
# Define three variables to hold each sentence string
sentence1 = "Python was created in the 1890’s by Guido van Rossum."
sentence2 = "Python is maintained as an 'open source' project by a group that is called the Python Software Foundation."
sentence3 = "He is affectionately known as Python's \"Benevolent Dictator for Life.\""

# Apply the appropriate string functions to correct the first sentence
sentence1 = sentence1.replace("1890’s", "1990’s")

# Concatenate the sentences into a single paragraph
paragraph = sentence1 + " " + sentence2 + " " + sentence3

# Print the concatenated paragraph
print(paragraph)
