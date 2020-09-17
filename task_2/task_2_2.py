print("Введите число")
a = int(input())
even = odd = 0

while a > 0:
	if a%2 == 0:
		even += 1
	else:
		odd += 1
	a = a // 10
print ("четных: {}; нечетных: {}".format(even, odd))

