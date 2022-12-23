elem = input('Введите цифры через запятую: ')
first_lst = elem.split(',')
elem = input('Введите цифры через запятую: ')
second_lst = elem.split(',')
a = first_lst.copy()
for elem in a:
    if elem in second_lst:
        first_lst.remove(elem)
print(first_lst)
print(second_lst)
# 4,9,6,8,8,9,1,2,5
# 5,9,4,2,3,6,9,4,8,3