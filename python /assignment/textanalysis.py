def count_words(text):
    word_count = 0
    in_word = False
    for char in text:
        if char != ' ':
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False
    return word_count

def count_sentences(text):
    sentence_count = 0
    for char in text:
        if char == '.':
            sentence_count += 1
    return sentence_count

def average_word_length(text):
    total_length = 0
    word_length = 0
    word_count = 0
    in_word = False
    for char in text:
        if char != ' ':
            word_length += 1
            in_word = True
        else:
            if in_word:
                total_length += word_length
                word_count += 1
                word_length = 0
                in_word = False
    if in_word:
        total_length += word_length
        word_count += 1
    return total_length / word_count if word_count > 0 else 0

def word_count(text):
    frequency = {}
    word = ""
    text = text.lower()
    for char in text:
        if char != ' ':
            word += char
        else:
            if word:
                if word in frequency:
                    frequency[word] += 1
                else:
                    frequency[word] = 1
            word = ""
    if word:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

text_input = input("Enter a text: ")

print(f"Total words: {count_words(text_input)}")
print(f"Total sentences: {count_sentences(text_input)}")
print(f"Average word length: {average_word_length(text_input):.2f}")
print(f"Word frequencies: {word_count(text_input)}")