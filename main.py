from stats import count_words, count_characters, sort_char_count


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    character_counts = count_characters(book_text)
    sortedlist = sort_char_count(character_counts)
    print_report(book_path, num_words, sortedlist)



def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        return f.read()

def print_report(book_path, num_words, sortedlist):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sortedlist:
        if char_dict["character"].isalpha():
            print(f"{char_dict["character"]}: {char_dict["count"]}")
    print("============= END ===============")


main() 