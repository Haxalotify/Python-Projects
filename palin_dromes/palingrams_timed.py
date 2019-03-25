"""Find all word pair palingrams in a dictionary file."""
import time

import load_diction

word_list = load_diction.load('2of4brif.txt')

#find word pair palingrams
def find_palingrams():
    """Find dictionary palingrams"""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]#word.join(reversed(word)) produces different result, not sure why
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-1]and rev_word[end-1:] in word_list:
                    pali_list.append((word, rev_word[end-1:]))
                if word[:i] == rev_word[end-1:]and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-1], word))
    return pali_list
start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()
#sort palingrams alphabetically
palingrams_sorted = sorted(palingrams)

#display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))

print("Runtime for this program was {} seconds.".format(end_time - start_time))
