# 6,3,9,7,1,1,2,4,8,3,8
numbers = input('Введите цифры через запятую: ')
lst = numbers.split(',')
new_lst = set(lst)
print(lst)
print(new_lst)

result = []
for elem in lst:
    if lst.count(elem) == 1:
        result.append(elem)
print(result)