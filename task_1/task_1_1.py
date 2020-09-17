a = 5
b = 6

print("{} = {}".format(a, bin(a)))
print("{} = {}".format(b, bin(b)))

print("Операция 'И': {} & {} = {} ({})".format(a,b,bin(a&b),a&b))
print("Операция 'исключающее ИЛИ':{} ^ {} = {} ({})".format(a,b,bin(a^b),a^b))
print("Операция 'ИЛИ': {} | {} = {} ({})".format(a,b,bin(a|b),a|b))
print("Побитовый сдвиг влево: {} << {} = {} ({})".format(a,2,bin(a<<2),a<<2))
print("Побитовый сдвиг вправо: {} >> {} = {} ({})".format(a,2,bin(a>>2),a>>2))
