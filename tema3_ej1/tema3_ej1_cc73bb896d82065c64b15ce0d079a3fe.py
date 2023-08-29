# completa el código de la función
def suma_divisores(a):
    suma = 0
    lista = []
    for i in range (1,a):
        lista.append(i)
    for k in lista:
        if a % k == 0:
            suma += k

    if suma == 1:
        tof = True
    else:
        tof = False

    return suma,tof