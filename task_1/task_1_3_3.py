from random import randint

print("Введите промежуток символов")

a,b = input().split()

print("Вывод случайного символа: ", chr(randint(ord(a),ord(b))))

