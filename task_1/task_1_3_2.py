import random

print("Число с плавающей точкой в пределах заданного промежутка")
print("Введите промежуток вещественных чисел")

a,b = input().split()

print("Вывод случайного вещественного числа: ", round((random.uniform(float(a), float(b))),3))

