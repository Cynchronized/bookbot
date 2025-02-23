from stats import get_num_words, get_chars_dict, dict_to_list
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_location = sys.argv[1]

    with open(file_location) as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        chars_dict = get_chars_dict(file_contents)
        list_of_dicts = dict_to_list(chars_dict)
        get_report(num_words, list_of_dicts, file_location)


# This generates a report of the frequency of alphabetical letters
def get_report(num_words, list_dicts, file_location):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in list_dicts:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")


main()
