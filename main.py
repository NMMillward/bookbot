def read_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())

def get_char_dict(text):
    lower_string = text.lower()

    char_dict = {}

    for char in lower_string:
        char_dict[char] = char_dict.get(char, 0) + 1

    return char_dict

def sort_char_dict(dict, only_alpha):
    char_count_list = []
    for key in dict.keys():
        if only_alpha:
            if key.isalpha():
                char_count_list.append({"char": key, "count": dict[key]})
        else:
            char_count_list.append({"char": key, "count": dict[key]})

    char_count_list.sort(reverse=True,key=sort_on)

    return char_count_list

def sort_on(dict):
    return dict["count"]

def print_report(book, word_count, char_dict):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document\r\n")

    for char in char_dict:
        print(f"The '{char["char"]}' character was found {char["count"]} times")

    print("--- End report ---")

def main():
    book = "books/frankenstein.txt"
    book_text = read_book_text(book)
    word_count = get_word_count(book_text)
    char_dict = sort_char_dict(get_char_dict(book_text), True)
    print(char_dict)
    print_report(book, word_count, char_dict)

main()