#Factores Primos
def es_primo(numero):
    lista1 = []
    lista2 = []
    for x in range(1, numero):
        if numero % x == 0:
            lista1.append(x)

    for x in range(2, numero):
        if numero > 1:
            if (numero % x) == 0:
                lista2.append(x)
    return lista2

