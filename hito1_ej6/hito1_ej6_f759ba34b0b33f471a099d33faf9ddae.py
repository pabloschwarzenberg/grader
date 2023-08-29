#Ordenar tres números
lista = []
i = 1

while i <= 3:
    codigo = input("Introduzca codigo número {}: ".format(i))
    if codigo.isdigit():
        lista.append(int(codigo))
        i += 1
    else:
        print("No es un código válido. Intente nuevamente.")

lista.sort()

print("Números ordenados: {}, {}, {}".format(lista[0], lista[1], lista[2]))