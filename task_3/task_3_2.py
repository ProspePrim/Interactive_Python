from random import random
n = 10
arr = [0]*n
even = []
for i in range(n):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)