# Vypočítaj súčet  všetkých  párnych čísiel od 1 do N

n = int(input('zadaj n: '))
a = 0

for i in range(1,n):
    if i%2 == 0:
        a = a+i
print('súčet  všetkých  párnych čísiel od 1 do N je:', a)
