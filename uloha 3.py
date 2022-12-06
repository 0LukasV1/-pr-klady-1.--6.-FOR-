#Naprogramuj funkciu, ktorá zistí počet všetkých čísel od , ktoré sú deliteľné siedmymi a štyrmi.

n = int(input('zadaj n: '))
a = 0

for i in range(1,n):
    if i%4 == 0 and i%7 == 0:
        a = a+1

print('počet všetkých čísel od , ktoré sú deliteľné siedmymi a štyrmi je:', a)
