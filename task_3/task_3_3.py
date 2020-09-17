from random import random
n = 15
arr = [0]*n
for i in range(n):
    arr[i] = int(random()*100)
    print(arr[i],end=' ')
print()
 
a = 0
b = 0
for i in range(n):
    if arr[i] < arr[a]:
        a = i
    elif arr[i] > arr[b]:
    	b = i
print('arr[%d]=%d arr[%d]=%d' % (a+1, arr[a], b+1, arr[b]))
b = arr[a]
arr[a] = arr[b]
arr[b] = b
 
for i in range(15):
    print(arr[i],end=' ')
print()