import sys
from stats import count_words, count_characters, sort_dictionary


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        book_path = sys.argv[1]
        print(f"Analyzing book found at {book_path}...")
        book_content = get_book_text(book_path)
        word_count = count_words(book_content)
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")    
        character_count = count_characters(book_content)
        print("--------- Character Count -------")
        sorted_list = sort_dictionary(character_count)
        for d in sorted_list:
            if d["char"].isalpha():
                print(f"{d['char']}: {d['count']}")


main()