num = int(input('введите число: '))
del_num = set()

for delit in range(1,(num//2)+2): #+2 чтобы у 1 был делитель
    if num%delit==0:
        del_num.add(delit)
        del_num.add(num//delit)

print(*sorted(del_num))
