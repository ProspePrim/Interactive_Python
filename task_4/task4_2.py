#Вывод все простые числа в диапазоне от 0 до N

N = 20

def other(n):
    arr = []
    for i in range(2, n):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            arr.append(i)
    return arr

def eratosthenes(n):
    sieve = list(range(0, n + 1))
    for i in range(0, n+1):
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
        else:
            sieve[1] = 0
    sieve.sort()
    while 0 in sieve:
            sieve.remove(0)
    return sieve    
    
print(eratosthenes(N))
print(other(N))