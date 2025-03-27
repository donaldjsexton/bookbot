import sys
from stats import get_num_words, count_letters, get_character_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]    
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    char_counts = count_letters(book_text)
    sorted_chars = get_character_report(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()
