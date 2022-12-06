#naprogramuj funkciu, ktorá vráti počet všetkych párnych čísel od 1-N

n = int(input('zadaj n: '))
a = 0

for i in range(1,n):
    if i%2 == 0:
        a = a+1
print('pocet všetkých párnych čísiel od 1 do N je:', a)