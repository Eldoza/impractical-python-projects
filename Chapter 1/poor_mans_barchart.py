# The six most commonly used letters in the english language can be remembered with the mnemonic "etaoin". Write a python script that takes a sentence (string) as input and returns a simple bar chart type display. Hint: I used dictionary data structure and two modules that I havent covered yet, pprint, and collections/default/dict

"""Map letters from string into dictionary & print bar chart of frequency."""
import sys
import pprint
from collections import defaultdict

text = "The most terrifing thing in the world is seeing things for how they truly are. "

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# defaultdict module lets you build dictionary keys on the fly!
mapped = defaultdict(list)

for char in text:
    char = char.lower()
    if char in ALPHABET:
        mapped[char].append(char)

# pprint lets you print stacked output
print("\n You may need to strech terminal window")
print("text = ", end='')
print("{}\n".format(text), file=sys.stderr)
pprint.pprint(mapped, width=110)