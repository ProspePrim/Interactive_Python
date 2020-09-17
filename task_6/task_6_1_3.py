import sys


def memory_count(lst):
    memory = 0

    for var in lst:
        print('***********')
        print(f'Переменная: {var}')
        print('Весит: ', sys.getsizeof(var))
        spam = sys.getsizeof(var)

        if hasattr(var, '__iter__') and not isinstance(var, str):

            if hasattr(var, 'keys'):
                for key, value in var.items():
                    print(f'\nКлюч: \'{key}\' значение {value}')
                    spam += memory_count([key]) + memory_count([value])

            else:
                spam += memory_count(var)

        memory += spam

    return memory


a = int(input('Введите целое трехзначное число:'))

print(f'Сумма цифр в числе: {(a // 100) + ((a // 10) % 10) + (a % 10)}')
print(f'Произведение цифр в числе: {(a // 100) * ((a // 10) % 10) * (a % 10)}')


    
_variable = []
for i in dir():
    if i[0] != '_' and not hasattr(locals()[i], '__name__'):
        _variable.append(locals()[i])

print('\nПеременные: ', _variable, '\n')
print('\nЗатраты памяти программы: ', memory_count(_variable))

#Сумма цифр в числе: 15
#Произведение цифр в числе: 120

#Переменные:  [456]

#***********
#Переменная: 456
#Весит:  28

#Затраты памяти программы:  28
