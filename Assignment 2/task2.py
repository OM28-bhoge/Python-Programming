string = input("String: ")
word = input("Word: ")

string_lower = string.lower()
word_lower = word.lower()

words = string_lower.split()
count = 0
for w in words:
    if word_lower in w:
        count += 1

print(f"How many times the search word appears in the string: {count}")
