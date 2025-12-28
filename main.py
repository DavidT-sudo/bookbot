from stats import get_num_words, count_char, chars_dict_to_sorted_list
import sys

def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as book_file:
        return book_file.read()

def main():
    if len(sys.argv) != 2:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = count_char(book_text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
