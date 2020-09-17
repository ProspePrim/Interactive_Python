print("Введите число")
a = int(input())
b = 1
c = 0
for i in range(a):
    c += b
    b /= -2
print(c)