def main():
    chars = []

    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars = get_char_dict(chars)
    char_freq = get_char_freq(text, chars)
    char_freq.sort(reverse=True, key=sort_on)
    print(f"{char_freq}")

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(chars):
    dd = {}
    alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
    i=0
    for c in alpha:
        dd["name"]=c
        dd["num"]=0
        chars.append(dd.copy())
    print(chars)
    return chars

def get_char_freq(text, chars):
    text=text.lower()
    for dd in chars: 
        dd["num"]=text.count(dd["name"])
    return chars

if __name__ == '__main__':
    main()
