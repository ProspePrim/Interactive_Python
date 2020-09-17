from random import random
n = round(random() * 100)
i = 1
print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
while i <= 10:
    a = int(input(str(i) + '-я попытка: '))
    if a > n:
        print('Слишком больше число')
    elif a < n:
        print('Слишком маленькое число')
    elif a == n:
        print('Вы угадали с {}-й попытки'.format(i))
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', n)