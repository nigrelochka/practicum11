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

ultra_new_text = []

for word in new_text:
    if word not in ultra_new_text:
        ultra_new_text.append(word)

print(*ultra_new_text)
