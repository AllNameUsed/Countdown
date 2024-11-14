import json

with open('words.txt', 'r') as file:
    english_words = list(set(word.strip().lower() for word in file))
    
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