import sys


def memory_count(lst): 
    memory = 0

    for var in lst:
        print('***********')
        print(f'Переменная: {var}') #Выводит переменную
        print('Весит: ', sys.getsizeof(var)) #Показзывает размер переменной
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

hundred = a // 100
dozen = (a // 10) % 10
unit = a % 10

summa = hundred + dozen + unit
mult = hundred * dozen * unit
print(f'Сумма цифр в числе: {summa}')
print(f'Произведение цифр в числе: {mult}')

    
_variable = []              #Пустой лист
for i in dir():             
    if i[0] != '_' and not hasattr(locals()[i], '__name__'): 
        _variable.append(locals()[i]) #поочередно добавляет все переменные в список _variable_ 

# dir() возвращает все список атрибутов и методов любого объекта
#Функция locals() возвращает словарь(dict) локальных переменных и их значений, текущей области

print('\nПеременные: ', _variable, '\n')
print('\nЗатраты памяти программы: ', memory_count(_variable))

#Введите целое трехзначное число:456
#Сумма цифр в числе: 15
#Произведение цифр в числе: 120

#Переменные:  [456, 5, 4, 120, 15, 6]

#***********
#Переменная: 456
#Весит:  28
#***********
#Переменная: 5
#Весит:  28
#***********
#Переменная: 4
#Весит:  28
#***********
#Переменная: 120
#Весит:  28
#***********
#Переменная: 15
#Весит:  28
#***********
#Переменная: 6
#Весит:  28

#Затраты памяти программы:  168