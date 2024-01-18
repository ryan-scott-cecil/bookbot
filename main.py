def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print_report(char_count, num_words, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    count = {}
    for char in text.lower():
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    return count

def print_report(char_count, num_words, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    list = []
    for char in char_count:
        list.append(char)
    list.sort()
    for char in list:
        if char.isalpha():
            print(f"The '{char}' character was found {char_count[char]} times")
    print("--- End report---")

main()
