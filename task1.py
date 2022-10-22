# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).


from random import sample


def list_rand(count):
    if count < 0:
       print('Вводите число больш нуля!')
       return []
       
    list_rand_numb = sample(range(count * 2), count)
    return list_rand_numb


def summ_numb(list_work):
    summ = 0
    for i in range(0, len(list_work), 2):
        summ += list_work[i]
    return summ

my_list = list_rand(int(input('Введите количество чисел в списке: ')))
print(my_list)
print(f'Суммма нечетных элементов списка равна: {summ_numb(my_list)}')

