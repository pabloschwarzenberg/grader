decimal = int(input("Ingrese un número: "))

aux = decimal
lista = []
while(True):
    lista.append(aux%2)
    aux = int(aux / 2)
    if(aux == 0):
        break

lista.reverse()

binario = 0
for x in range(len(lista)):
    binario = binario + lista[x]*pow(10,(len(lista)-x-1))

print("resultado=%i"% binario)