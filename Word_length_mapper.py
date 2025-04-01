sentence = input("Enter a sentence: ")
words = sentence.split()

# map fn to get the length of each word in the list
lengths = list(map(len, words))

print("Words:", words)
print("Lengths:", lengths)
