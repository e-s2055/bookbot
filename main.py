import sys
from stats import get_num_words
from stats import get_chars
from stats import sort_on

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")


    char_counts = get_chars(text)
    sorted_char_counts = sort_on(char_counts)
    print("--------- Character Count -------")
    for char_entry in sorted_char_counts:
        print(f"{char_entry['letter']}: {char_entry['count']}")
    print("============= END ===============")
main()