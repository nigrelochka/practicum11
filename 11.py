lst = [int(x) for x in input('введите список: ').split()]
command = input('введите команду (R5 или L3): ')

direction = command[0]  # R или L
step = int(command[1:])  # число после буквы

step = step % len(lst)  # если шаг больше длины списка

if direction == 'R':  # сдвиг вправо
    # часть, которая перейдёт в начало
    part1 = lst[-step:]
    # оставшаяся часть
    part2 = lst[:-step]
    new_lst = part1 + part2
else:  # сдвиг влево
    part1 = lst[step:]
    part2 = lst[:step]
    new_lst = part1 + part2

print(*new_lst)