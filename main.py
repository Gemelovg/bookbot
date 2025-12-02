import sys

from stats import get_num_words, number_of_chars, sorted_number_of_chars


def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) == 1:
        sys.exit(1)
    else:
        FILEPATH = sys.argv[1]
        # FILEPATH = "./books/frankenstein.txt"
        # print(get_book_text("FILEPATH"))
        # print(f"Found {get_num_words(FILEPATH)} total words")
        total_words = get_num_words(FILEPATH)
        items_n = number_of_chars(FILEPATH)
        items = sorted_number_of_chars(items_n)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {FILEPATH}...")
        print("----------- Word Count ----------")
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")

        for k, v in items.items():
            if k.isalpha():
                print(f"{k}: {v}")
            else:
                pass


main()
