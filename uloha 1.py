#Naprogramuj funkciu, ktorá vypíše všetky čísla od 1-N, ktoré sú deliteľné troma.

n = int(input('zadaj n:' ))

for i in range(1,n):
    if i%3 == 0:
        print(i,end =' ')