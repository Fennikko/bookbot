def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_letters = get_letter_count(text)
    # print(f"{num_words} words found in the document")
    # print(num_letters)
    report(book_path,num_words,num_letters)

def word_count(contents):
    count = 0
    words = contents.split()
    for word in words:
        count += 1
    return len(words)

def get_book_text(path):
        with open(path) as f:
            return f.read()
        
def get_letter_count(contents):
    letter_count = {}
    contents = contents.lower()
    for char in contents:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1
    return letter_count

def report(book_path,num_words,num_letters):
    alpha_characters = {}
    for l in num_letters:
        if l.isalpha():
            if l not in alpha_characters:
                alpha_characters[l] = num_letters[l]
    sorted_characters = dict(sorted(alpha_characters.items(), key=lambda item: item[1], reverse=True))
    character_string = ""
    total_letters = len(sorted_characters)
    begin = print(f"--- Begin report of {book_path} ---")
    words = print(f"{num_words} words found in the document\n")
    for idx, (c, count) in enumerate(sorted_characters.items()):
        character_string += f"The '{c}' character was found {num_letters[c]} times"
        
        if idx < total_letters -1:
            character_string += "\n"
    characters = print(character_string)
    end = print("--- End Report ---")
    return begin, words, characters, end

main()
