#Naprogramuj funkciu , ktorá sčíta dokopy čísla od 1 do N. (N -parameter funkcie)

n = int(input('zadaj n: '))
a = 0

for i in range(1,n):
        a = a+i

print('súčet  všetkých  čísiel od 1 do N je:', a)
