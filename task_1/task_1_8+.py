print('Введите три числа: ')
a,b,c = input().split()
a,b,c = int(a), int(b), int(c)

 
if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)