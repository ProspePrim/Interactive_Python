import sys


def memory_count(lst):
    memory = 0

    for var in lst:
        print('***********')
        print(f'Переменная: {var}')
        print('Весит: ', sys.getsizeof(var))
        spam = sys.getsizeof(var)

        if hasattr(var, '__iter__') and not isinstance(var, str): #Если объект итерируемый, но не строка

            if hasattr(var, 'keys'):   # Для словарей
                for key, value in var.items():
                    print(f'\nКлюч: \'{key}\' значение {value}')
                    spam += memory_count([key]) + memory_count([value])

            else:
                spam += memory_count(var)

        memory += spam

    return memory


print("Введите число")
a = int(input())
b = 0
c = 0
d = 1

while a > 0:
    b = a%10
    a = a // 10
    c = c + b
    d = d * b
    
_variable = []
for i in dir():
    if i[0] != '_' and not hasattr(locals()[i], '__name__'):
        _variable.append(locals()[i])

print('\nПеременные: ', _variable, '\n')
print('\nЗатраты памяти программы: ', memory_count(_variable))


#Переменные:  [0, 4, 15, 120]

#***********
#Переменная: 0
#Весит:  24
#***********
#Переменная: 4
#Весит:  28
#***********
#Переменная: 15
#Весит:  28
#***********
#Переменная: 120
#Весит:  28

#Затраты памяти программы:  108