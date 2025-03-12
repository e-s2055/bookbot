def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_chars(text):
    chars = {}  # Empty dictionary to store counts
    for letter in text.lower():
        if letter.isalpha():
            if letter in chars:
                chars[letter] += 1
            else: 
                chars[letter] = 1
    return chars

def sort_on(chars):
    char_list = [{"letter": letter, "count": count} for letter, count in chars.items()]
    char_list.sort(reverse=True, key=lambda char: char["count"])
    return char_list