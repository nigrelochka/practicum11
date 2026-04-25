list_of_numbers = [int(x) for x in input('введите числа: ').split()]
sum_even, sum_odd = 0, 0

for num in list_of_numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print(f'сумма четных: {sum_even}, сумма нечетных: {sum_odd}')
