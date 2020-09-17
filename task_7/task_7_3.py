#Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. 
#Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
#в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

#Вариант 1

m = int(input('Введите m'))
size = 2 * m + 1 
a = [0]*size
for i in range(size):
    a[i] = int(random.randint(0,49))
print(a)

a.sort()
mediana_1 = a[m]

#Вариант 2

size = 11 
b = [0]*size
for i in range(size):
    b[i] = int(random.randint(0,49))
print(b)

b.sort()
mediana_2 = b[int(len(b)/2)]

#Вариант 3

def median(array):
    half = len(array) // 2
    array.sort()
    if not len(array) % 2:
        return (array[half - 1] + array[half]) / 2
    return array[half]
    
mediana_3 = median(b)