from stats import count_words, count_characters, sort_char_count
import sys
import math


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    character_counts = count_characters(book_text)
    sortedlist = sort_char_count(character_counts)
    print(f"Char count: {sortedlist}")
    print_report(book_path, num_words, sortedlist)



def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        return f.read()

def print_report(book_path, num_words, sortedlist):
    total_char = 0
    num_sentences = math.ceil(num_words / 15)
    num_paragraphs = math.ceil(num_sentences / 5)
    num_pages = math.ceil(num_words / 300)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"Which is about {num_sentences} sentences")
    print(f"Which is about {num_paragraphs} paragraphs")
    print(f"Which is about {num_pages} pages")
    print("--------- Character Count -------")
    for char_dict in sortedlist:
        if char_dict["character"].isalpha():
            total_char += char_dict["count"]
            print(f"{char_dict["character"]}: {char_dict["count"]}")
    print(f"Total: {total_char}")
    print("============= END ===============")


main()