def count_word_occurrences(text, word):
    text = text.lower()  # Convert the text to lowercase for case-insensitive matching
    word = word.lower()  # Convert the target word to lowercase
    return text.count(word) if text else 0
