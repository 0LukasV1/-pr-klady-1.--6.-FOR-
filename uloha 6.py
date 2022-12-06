#Naprogramuj funkciu, ktorá v intervale od  <začiatok,  koniec>  zistí počet čísel, ktoré sú deliteľné ôsmimi

z = int(input('zadaj zaciatok intervalu: '))
k = int(input('zadaj koniec intervalu: '))
a = 0

for i in range(z,k):
    if i%8 == 0:
        a = a+1
print('pocet čísiel delitelnych 8 v intervale je:', a)