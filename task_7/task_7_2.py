# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
#заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

size = 10
a = [0]*size
for i in range(size):
    a[i] = int(random.randint(0,49))
print(a)

def merge_sort(array):
    if len(array) > 1:
        center = len(array) // 2
        left = array[:center]
        right = array[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array



print('Сортировка слиянием:', merge_sort(a))
