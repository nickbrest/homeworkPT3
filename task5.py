# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    list = [0]
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a - b
        list.append(a)
    list1 = list[::-1]
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
        list1.append(a)
    return list1

num = int(input("Введите число: "))
print(*fib(num))