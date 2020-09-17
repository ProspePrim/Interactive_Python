#1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). 
#Выведите на экран исходный и отсортированный массивы.


import random

size = 10
a = [0]*size
for i in range(size):
    a[i] = int(random.randint(-100,99))
print(a)

b = [0]*size
for i in range(size):
    b[i] = int(random.randint(-100,99))
print(b)

def bubble_sort(array): #вариант 1
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1 
    print(array)
    
def bubble_sort_2(array): #Вариант 2
    for i in range(9):
        for j in range(9-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j+1], array[j]
    print(array)
    
bubble_sort(a)
bubble_sort_2(b)