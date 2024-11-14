import random
import json
from itertools import combinations

# Loading from a JSON file
with open("data.json", "r") as file:
    DATA = json.load(file)
    
VOWELS = ['A', 'E', 'I', 'O', 'U']
CONS = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

def generate_letters(selections):
    # Placeholder for generating letters based on selections
    # 'selections' is a list like ['Vowel', 'Cons', ...]
    letters_values = []
    for s in selections:
        if s == "Vowel":
            char = random.choice(VOWELS)
            letters_values.append(char)
        elif s == "Cons":
            char = random.choice(CONS)
            letters_values.append(char)
        else:
            print("Selection " + str(s)+" is not valid!!")
    return letters_values

def find_top_words(letters):
    # Placeholder for finding the longest word from letters
    ans = []
    seen = set()
    for i in range(len(letters),0, -1):
        temp = list(combinations(letters, i))
        for ls in temp:
            key = ''.join(sorted(ls)).lower()
            if key in DATA and not key in seen:
                seen.add(key)
                for word in DATA[key]:
                    ans.append(word.upper())
    return ans[:5]


# find_longest_word(['u','e','o','i','g','r','x','c','v'])