print("Введите два числа через пробел")
a, b = input().split()
a, b = int(a), int(b)

    


while True:
    print("Введите знак ('0 (для выхода из программы)', '+', '-', '*', '/')")
    sign = input()
    if sign == '0' : break

    elif sign in ('+', '-', '*', '/'):
        if sign == '+':
            print("{} + {} = {}".format(a,b,a+b)) 
        elif sign == '-':
            print("{} - {} = {}".format(a,b,a-b)) 
        elif sign == '*':
            print("{} * {} = {}".format(a,b,a*b))
        elif sign == '/':
            if a != 0 or b != 0:
                print("{} / {} = {}".format(a,b,a/b)) 
            else:
                print("Ошибка!")
    else:
        print("Введен неверный знак ")