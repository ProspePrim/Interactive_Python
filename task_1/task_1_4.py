print("Введите буквы через 'пробел' ")

a,b = input().split()

a = a.lower()
b = b.lower()

print ("Место в алфавите : ", ord(a) % 96)

print ("Место в алфавите : ", ord(b) % 96)


print("Количество знаком между ними: ", abs(ord(a) - ord(b)) - 1)
