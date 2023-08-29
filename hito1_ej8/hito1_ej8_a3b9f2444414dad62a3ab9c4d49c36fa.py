#Descomponer un número
import sys

lista = []
Numero = input('Ingrese un numero de 1 a 4 digitos: ')


while len(Numero)>4:
    Numero = input('Ingrese un numero de 1 a 4 digitos: ')


for i in reversed(Numero):
    lista.append(i)

lista_final = []
contador = 0
for y in lista:
    if contador == 0:
        lista_final.append(y+'U')
    elif contador == 1:
        lista_final.append(y+'D +')
    elif contador == 2:
        lista_final.append(y+'C +')
    elif contador == 3:
        lista_final.append(y+'M +')

    contador = contador + 1

for z in reversed(lista_final):
    sys.stdout.write(z+' ')
