def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(contents):
    words = contents.split()
    return len(words)

""" CH2 L3
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)
"""

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
main() 