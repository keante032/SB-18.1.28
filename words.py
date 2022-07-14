def print_upper_words(words, must_start_with):
    """Given list of words, print each word in uppercase on its own line."""

    for letter in must_start_with:
        letter = letter.upper()
        for word in words:
            word = word.upper()
            if word[0] == letter:
                print(word)




print_upper_words(["hi", "bye", "g'day", "hellerrrrrrrrrr", "eesh"], ["h", "b"])