text=[]
print("введите текст (пустая строка для завершения):")
while True:
    line = input()
    text += line.split()
    if line == "":
        break

text_no_punctuation=[]

for word in text:
    new_word=''
    for char in word:
        if char.isalpha():
            new_word += char
    text_no_punctuation.append(new_word)

count_words=[]

for num_word in range(len(text_no_punctuation)-1):
    counter=0
    for num_word2 in range(len(text_no_punctuation)):
        if text_no_punctuation[num_word]==text_no_punctuation[num_word2]:
            counter += 1
    if [text_no_punctuation[num_word], counter] not in count_words:
        count_words.append([text_no_punctuation[num_word], counter])

sorted_text=sorted(count_words, key=lambda x: x[1], reverse=True)

for num in range(len(sorted_text)):
    print(sorted_text[num][0])
