def get_num_words(text):
    words = text.split()
    print(len(words))

def get_chars_dict(text):
    lower_text = text.lower()
    characters = {}
    
    for char in lower_text:
        if char in characters:
            characters[char] = characters[char] + 1
        else:
            characters[char] = 1
    
    print(characters)

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        number_of_words(file_contents)
        number_of_characters(file_contents)
main()
