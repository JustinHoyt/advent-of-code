from typing import Set, Dict, Tuple, List
input = ["as", "fawe"]

num_valid_passphrases = 0

for phrase in input:
    is_valid_phrase = True
    words = phrase.split(" ")
    myset = set()  # type: Set[str]
    for word in words:
        if word in myset:
            is_valid_phrase = False
        else:
            myset.add(word)
    if is_valid_phrase:
        num_valid_passphrases += 1

print(num_valid_passphrases)
