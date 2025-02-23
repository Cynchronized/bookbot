# Takes in the text of a file
#
# Returns: number of words
def get_num_words(text):
    words = text.split()
    return len(words)


# Takes in the text of a file then creates a dictionary counting the number of each character
#
# Returns: Dictionary of characters and their frequency
def get_chars_dict(text):
    lower_text = text.lower()
    characters = {}

    for char in lower_text:
        if char in characters:
            characters[char] = characters[char] + 1
        else:
            characters[char] = 1

    return characters


# Converts a dictionary of characters into a list of dictionaries
# Filters out non alphabetical characters and sorts numerically from largest to smallest
#
# Returns: a list of dictionaries
def dict_to_list(dict):
    list = []

    for d in dict:
        list.append({"char": f"{d}", "num": dict[d]})

    list.sort(reverse=True, key=sort_on)

    return list


# Sort by number
def sort_on(dict):
    return dict["num"]
