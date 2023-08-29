#Suma de los divisores de un número
def suma_divisores(a):
    i = 1
    divisores = []
    while i<a:
        if a%i == 0:
            divisores.append(i)
        i = i + 1
    suma = 0
    for j in divisores:
        suma = suma + j
    if suma == 1:
        return suma,True
    else:
        return suma,False         