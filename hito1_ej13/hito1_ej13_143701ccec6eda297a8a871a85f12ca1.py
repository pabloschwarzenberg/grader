#Factores Primos
def descomponer(lista_primos, numero):
    lista_factores = []
    contador = 0
    while contador < len(lista_primos):
        if numero % lista_primos[contador] == 0:
            lista_factores.append(lista_primos[contador])
            numero = numero / lista_primos[contador]
        else:
            contador += 1
    return lista_factores