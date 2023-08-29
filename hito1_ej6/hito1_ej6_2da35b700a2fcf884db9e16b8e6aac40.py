#Ordenar tres números
numero1 = int(input("Ingrese numero entero 1"))
numero2 = int(input("Ingrese numero entero 2"))
numero3 = int(input("Ingrese numero entero 3"))

lista = [numero1,numero2,numero3]
listaOrdenada = []
while len(lista) > 0:
    numero = lista[0]
    if len(lista) == 1:
        listaOrdenada.append(numero)
    else:
        for item in lista:
            for item2 in lista:
                if item < item2:
                    if item < numero:
                        numero = item
                        break
        listaOrdenada.append(numero)
    lista.remove(numero)
print(listaOrdenada)