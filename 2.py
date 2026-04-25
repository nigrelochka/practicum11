list_of_numbers = [int(x) for x in input('введите числа: ').split()]
new_list_of_numbers = []

for i in range(len(list_of_numbers)):
    if list_of_numbers[i] != 3:
        new_list_of_numbers.append(list_of_numbers[i])

print(*new_list_of_numbers)
