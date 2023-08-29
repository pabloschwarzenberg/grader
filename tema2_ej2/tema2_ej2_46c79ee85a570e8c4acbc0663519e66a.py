# completa el código de la función
def amigos(a, b):
    lista= []
    for n in range(1, a):
        if a% n== 0:
            lista.append(n)
    suma_lista= 0
    for i in lista:
        suma_lista= suma_lista+ i
    if suma_lista== b:
        return True
    else:
        return False
