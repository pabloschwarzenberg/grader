# completa el código de la función
def amigos(a,b):
    lista = []
    for i in range(1, a):
        if a % i == 0:
            lista.append(i)
    suma = sum(lista)
    if suma == b:
        return True
    else:
        return False