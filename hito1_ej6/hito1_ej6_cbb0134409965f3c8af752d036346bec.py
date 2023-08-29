lista =[]
for i in range(3):
    agregar = int(input("Ingresar un numero: "))
    lista.append(agregar)

def ordenar(x):
    x.sort()
    return lista

ordenar(lista)
print(lista)