def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    lower_text = text.lower()
    characters = {}

    for char in lower_text:
        if char in characters:
            characters[char] = characters[char] + 1
        else:
            characters[char] = 1

    return characters    

def dict_to_list(dict):
    list = []

    for d in dict:
        list.append({ "char": f"{d}", "num": dict[d]})

    list.sort(reverse=True, key=sort_on)

    return list

def sort_on(dict):
    return dict["num"]


def get_report(num_words, list_dicts, file_location):
    print(f"--- Begin report of {file_location} ---")
    print(f"{num_words} words found in the document \n")  

    for dict in list_dicts:
        if dict["char"].isalpha():
            print(f"The '{dict["char"]}' was found {dict["num"]} times")
    

    print("--- End report ---")

def main():
    file_location = "./books/frankenstein.txt"
    with open(file_location) as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        chars_dict = get_chars_dict(file_contents)
        list_of_dicts = dict_to_list(chars_dict)
        get_report(num_words, list_of_dicts, file_location)

main()
