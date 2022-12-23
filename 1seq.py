lst = []
elem_lst = int(input('Введите количество элементов: '))
for elem in range(elem_lst):
    elem = int(input(f'Введите {elem+1} элемент: '))
    lst.append(elem)
print(lst)