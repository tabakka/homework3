import random
#dict = {'Pushkin': '06.06.1799',
#        'Gogol': '01.04.1809',
#       'Tolstoy': '09.09.1828',
#        'Chehov': '29.01.1860',
#       'Dostoevskiy': '11.11.1821'}
poets = ['Pushkin', 'Gogol', 'Tolstoy', 'Chehov', 'Dostoevskiy']
dates = ['06.06.1799', '01.04.1809', '09.09.1828', '29.01.1860', '11.11.1821']
result = random.sample(poets, 2)
name_1 = poets.index(result[0])
name_2 = poets.index(result[1])
date_1 = dates[name_1]
date_2 = dates[name_2]
effort = 0
right = 0
wrong = 0
user = input(f'Введите дату рождения {result[0]} ')
effort += 1
if user != date_1:
    print(f'Неверно! Верный ответ {date_1}')
    wrong += 1
else:
    print('Верно!')
    right +=1
user = input(f'Введите дату рождения {result[1]} ')
effort += 1
if user != date_2:
    print(f'Неверно! Верный ответ {date_2}')
    wrong += 1
else:
    print('Верно!')
    right += 1

print('количество правильных ответов:', right)
print('количество ошибок', wrong)
print('процент правильных ответов', right / effort * 100)
print('процент неправильных ответов', wrong / effort * 100)