import load_diction

word_list = load_diction.load("2of4brif.txt")

anagram_list = []

name = input("Enter a word or name ")
print("Input name = {}".format (name))
name = name.lower()
print("Using name = {}".format(name))

# sort name & find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

# print anagram
print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams =", *anagram_list, sep='\n')
