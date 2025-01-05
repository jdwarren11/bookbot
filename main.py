def count_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

def count_unique_chars(text):
    char_dict = {}
    for char in text:
        low_char = char.lower()
        if low_char in char_dict:
            char_dict[low_char] += 1
        else:
            char_dict[low_char] = 1
    return char_dict

def sort_on(d):
    return d["num"]

def sort_dict(char_dict):
    sorted = []
    for char in char_dict:
        sorted.append({"char": char, "num": char_dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    word_count = count_words(book_text)
    unique_chars = count_unique_chars(book_text)
    sorted_char_list = sort_dict(unique_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

main()
