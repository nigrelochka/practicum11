text = input('введите текст: ').split(' ')

new_text = []
punctuation_marks = ['.', ',', '?', '!', ';', ':', '-',
                     '(', ')', '[', ']', '"']

for word in text:
    new_word = ''
    for char in word:
        if char not in punctuation_marks:
            new_word += char
    new_text.append(new_word)

print(*new_text)
