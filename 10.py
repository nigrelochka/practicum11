lst1 = [int(x) for x in input('введите первый список: ').split()]
lst2 = [int(x) for x in input('введите второй список: ').split()]
start, end = map(int, input('введите начало и конец диапазона: ').split())

start_index = start - 1
end_index = end - 1

extracted_elements = lst1[start_index:end_index + 1][::-1]

lst1 = lst1[:start_index] + lst1[end_index + 1:]

for element in extracted_elements:
    lst2.append(element)

print(*lst1)
print(*lst2)