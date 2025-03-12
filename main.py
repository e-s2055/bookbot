
def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    words = text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

main()