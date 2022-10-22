# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


from random import uniform


def rand(count):
    if count < 0:
       print('Вводите число больш нуля!')
       return [0.0]

    list_rand = []
    for i in range(count):
        list_rand.append(round(uniform(0, 10),2))
    return list_rand

def calc_dec(list_work):
    list_num = []
    for i in range(len(list_work)):
        list_num.append((list_work[i]) - int(list_work[i]))
    result = round((max(list_num) - min(list_num)), 2)
    return result, round(max(list_num),2), round(min(list_num),2)

my_list = rand(int(input('Введите количество чисел в списке: ')))
print(my_list)
diff, max, min = calc_dec(my_list)
print(f'Max: {max}, Min: {min}, Difference: {diff}')

