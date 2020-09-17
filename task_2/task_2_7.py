print("Введите число")
a = int(input())
c = 0
b = 0

for i in range(a):
    c += (i+1)
b = (a*(a+1))/2
    
print(c)
print(int(b))
print(c == int(b))
    