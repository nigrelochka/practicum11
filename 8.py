def string_of_characters(string):
    new_text = [char for char in string]
    new_text = sorted(new_text)
    ultra_new_text = ''

    for char in new_text:
        ultra_new_text += char

    return ultra_new_text

text = input('введите текст: ')
print(string_of_characters(text))
