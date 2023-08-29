# Numeros Amigos
def amigos(numero,numero2):
    lista_1= []
    lista_2 = []
    suma_1 = 0
    suma_2 = 0
    for x in range(1, numero):
        if numero % x == 0:
            lista_1.append(x)
    for x in lista_1:
        suma_1 += x
    for x in range(1, numero2):
        if numero2 % x == 0:
            lista_2.append(x)
    for x in lista_2:
        suma_2 += x
    if suma_1 == numero2 and suma_2 == numero:
        return True
    else:
        return False