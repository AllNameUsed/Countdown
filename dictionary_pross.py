import json

def get_first_words(filename):
    first_words = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Remove leading and trailing whitespace
            line = line.strip()
            if line:
                # Split the line into words based on whitespace
                words_in_line = line.split()
                if words_in_line:
                    # Extract the first word
                    first_word = words_in_line[0]
                    # Remove any trailing punctuation from the word
                    first_word = first_word.strip('.,;:')
                    if len(first_word) > 1 and first_word.isalpha():
                        first_words.append(first_word.lower())
    return first_words


# with open('Oxford English Dictionary.txt', 'r') as file:
#     english_words = list(set(word.strip().lower() for word in file))

english_words = get_first_words("Oxford English Dictionary.txt")
print(english_words)


dic = {}
for word in english_words:
    if len(word) <= 9:
        key = ''.join(sorted(word))
        if key in dic:
            dic[key].append(word)
        else:
            dic[key] = [word]
print(dic)
# Saving to a JSON file
with open("data.json", "w") as file:
    json.dump(dic, file)