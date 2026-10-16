# Text Statistics

sentence = input("Enter a multi-word sentence: ")

words = sentence.split()

characters = len(sentence)
total_words = len(words)
vowels = 0
non_space = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1
    if char != " ":
        non_space += 1

average_length = non_space / total_words

print("Total characters:", characters)
print("Total words:", total_words)
print("Number of vowels:", vowels)
print("Non-space characters:", non_space)
print(f"Average word length: {average_length:.2f}")
print("First word:", words[0])
print("Last word:", words[-1])
print("Sentence reversed:", sentence[::-1])