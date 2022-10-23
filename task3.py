# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.

def convert_dec_bin(numb):
   list = []
   while numb > 0:
      temp = numb % 2
      list.append(temp)
      # list.insert(0, temp)
      numb //=2
   return list[::-1]
   # return list
 
number = int(input('Введите число для преобразования: '))
print(*convert_dec_bin(number))
# print(*convert_dec_bin(number), sep='')

