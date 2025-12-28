def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def count_char(book_text):
    book_text = book_text.lower()
    counts = {}

    for char in book_text:
        counts[char] = counts.get(char, 0) + 1
        
    return counts

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list