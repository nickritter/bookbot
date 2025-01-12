import string

def sort_on(dict):
    return dict["num"]

def dict_to_list(d):
    final_list = []
    for c, n in d.items():
        final_list.append({"char":c, "num": n})
    return final_list

def word_count(s):
    return len(s.split())

def unique_char_count(s):
    chars = {}
    for c in s:
        c_lower = c.lower()
        if c_lower in string.ascii_lowercase:
            if c_lower not in chars:
                chars[c_lower] = 1
            else: #elif c in chars:
                chars[c_lower] += 1
    return chars

def display_word_count(n):
    print(f"{n} words found in the document")

def display_unique_char_count(char_count_list):
    for item in char_count_list:
        char = item["char"]
        num = item["num"]
        print(f"The '{char}' character was found {num} times")

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words = word_count(file_contents)
    dict_chars = unique_char_count(file_contents)
    sorted_chars = dict_to_list(dict_chars)
    sorted_chars.sort(reverse = True, key = sort_on)
    print("--- Begin report of books/frankenstein.txt ---")

    display_word_count(words)

    print("")

    display_unique_char_count(sorted_chars)

    print("--- End Report ---")
