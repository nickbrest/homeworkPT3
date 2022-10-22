# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from random import sample


def list_rand(count):
    if count < 0:
       print('Вводите число больш нуля!')
       return []
       
    list_rand_numb = sample(range(count * 2), count)
    return list_rand_numb


def mult_pair(list_work):
    result = []
    if len(list_work) % 2:
        for i in range(len(list_work) // 2):
            result.append(list_work[i] * list_work[len(list_work) - i - 1])
        result.append(list_work[len(list_work) // 2])
    else:
        for i in range(len(list_work) // 2):
            result.append(list_work[i] * list_work[len(list_work) - i - 1])

    return result


my_list = list_rand(int(input('Введите количество чисел в списке: ')))
print(my_list)
print(mult_pair(my_list))

