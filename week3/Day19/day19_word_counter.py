# This is a word counter application

print("===== WORD COUNTER TOOL =====")

text = input("Enter a sentence: ")

words = text.split()

word_count = len(words)

character_count = len(text)

sentence_count = text.split(".")

print("\nAnalysis Result: ")
print("Word Count: ", word_count)
print("Character Count (including spaces): ", character_count)
print(f"Sentence Count: ", sentence_count)