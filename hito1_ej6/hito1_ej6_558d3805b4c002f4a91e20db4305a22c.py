#Ordenar tres números
from os import system
system('cls')

n1 = int(input(''))
n2 = int(input(''))
n3 = int(input(''))

nMayor = 0
nMedio = 0
nMenor = 0

if n1 >= n2 and n1 >= n3:
    nMayor = n1
    if n2 >= n3:
        nMedio = n2
        nMenor = n3
    elif n3 >= n2:
        nMedio = n3
        nMenor = n2
elif n2 >= n1 and n2 >= n3:
    nMayor = n2
    if n1 >= n3:
        nMedio = n1
        nMenor = n3
    elif n3 >= n1:
        nMedio = n3
        nMenor = n1
elif n3 >= n1 and n3 >= n2:
    nMayor = n3
    if n1 >= n2:
        nMedio = n1
        nMenor = n2
    elif n2 >= n1:
        nMedio = n2
        nMenor = n1


numbers = [nMenor,nMedio,nMayor]
print(numbers)
