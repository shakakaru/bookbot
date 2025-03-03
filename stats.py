def count_words(contents):
    words = contents.split()
    return len(words)

def count_characters(contents):
    lowercase_contents = contents.lower()
    character_counts = {}
    for char in lowercase_contents:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def sort_on(dict):
    return dict["count"]

def sort_char_count(dictionary):
    listofdics = []
    for char_key in dictionary:
        listofdics.append({"character":char_key, "count": dictionary[char_key]})
        #char_dict = {}
        #char_dict["character"] = char_key
        #char_dict["count"] = dictionary[char_key]
        #listofdics.append(char_dict)
    listofdics.sort(reverse=True, key=sort_on)
    return listofdics


"""
for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

planets = {}
planets["Earth"] = True
planets["Pluto"] = False
print(planets["Pluto"])
# Prints False
"""