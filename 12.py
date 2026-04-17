def count_holes(word):
    """Считает количество букв с отверстиями в слове"""
    hole_letters = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']
    count = 0
    for char in word:
        if char in hole_letters:
            count += 1
    return count


def count_letters_without_holes(word):
    """Считает количество букв без отверстий в слове"""
    hole_letters = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']
    count = 0
    for char in word:
        if char not in hole_letters:
            count += 1
    return count


text = input('введите текст: ').split()

total_holes = 0
total_without_holes = 0
words_with_two_or_more_holes = []

for word in text:
    holes = count_holes(word)
    without_holes = count_letters_without_holes(word)

    total_holes += holes
    total_without_holes += without_holes

    if holes >= 2:
        words_with_two_or_more_holes.append(word)

print(total_holes, total_without_holes)
print(*words_with_two_or_more_holes)