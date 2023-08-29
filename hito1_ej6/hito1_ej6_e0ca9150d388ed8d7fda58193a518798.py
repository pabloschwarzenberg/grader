lista = []
for x in range(3):
    lista.append(input("Ingrese un valor: "))

for x in range(1, len(lista)):
    for i in range(len(lista) - x):
        if(lista[i] > lista[i+1]):
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
print(lista[0] + "," + lista[1] + "," + lista[2])