import random
import json
from itertools import combinations

# Loading from a JSON file
with open("data.json", "r") as file:
    DATA = json.load(file)
    
def get_random_vowel():
    vowels = ['A', 'E', 'I', 'O', 'U']
    # Frequencies of vowels in English (approximate, normalized)
    vowel_frequencies = [8.17, 12.70, 6.97, 7.51, 2.76]
    total = sum(vowel_frequencies)
    weights = [freq / total for freq in vowel_frequencies]
    return random.choices(vowels, weights=weights, k=1)[0]

def get_random_consonant():
    consonants = [
        'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
        'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
    ]
    consonant_frequencies = [
        2.49, 4.64, 7.10, 3.73, 3.37, 10.17, 0.25, 1.29, 6.73, 4.03,
        11.28, 3.22, 0.17, 10.00, 10.57, 15.14, 1.64, 3.94, 0.25, 3.29, 0.12
    ]
    total = sum(consonant_frequencies)
    weights = [freq / total for freq in consonant_frequencies]
    return random.choices(consonants, weights=weights, k=1)[0]

VOWELS = ['A', 'E', 'I', 'O', 'U']
CONS = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

def generate_letters(selections):
    # Placeholder for generating letters based on selections
    # 'selections' is a list like ['Vowel', 'Cons', ...]
    letters_values = []
    for s in selections:
        if s == "Vowel":
            char = random.choice(VOWELS)
            letters_values.append(get_random_vowel())
        elif s == "Cons":
            char = random.choice(CONS)
            letters_values.append(get_random_consonant())
        else:
            print("Selection " + str(s)+" is not valid!!")
    return letters_values

def find_top_words(letters):
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
                if len(ans) == 5:
                    return ans
                    
    return ans[:5]


# find_longest_word(['u','e','o','i','g','r','x','c','v'])