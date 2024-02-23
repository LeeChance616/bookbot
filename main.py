with open("books/frankenstein.txt") as f:
     file_contents = f.read()

def count_words(file_contents):
     words = file_contents.split()
     return len(words)
print(count_words(file_contents))



charCount = {}
lowerText = file_contents.lower()
for char in lowerText:
     charCount[char] = charCount.get(char, 0) + 1
print(charCount)

char_dicts = [{'char': c, 'num': count} for c, count in charCount.items()]

def sort(char_dicts):
     return char_dicts["num"]
print(char_dicts)
char_dicts.sort(key=sort, reverse=True)
print(char_dicts)

for dictionary in char_dicts:
     if dictionary['char'].isalpha():
          print("The '{}' character was found {} times".format(dictionary['char'], dictionary['num']))