list_of_10numbers = [int(x) for x in input('введите числа: ').split()]

if len(list_of_10numbers) == 10:
    list_of_8numbers = []
    for _ in range(9):
        num = list_of_10numbers[_] + list_of_10numbers[_ + 1]
        list_of_8numbers.append(num)
    print(*list_of_8numbers)
else:
    print('не 10 чисел')
