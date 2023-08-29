# completa el código de la función
def suma_divisores(a):
    lista=[]
    suma=0
    for n in range(1,a):
        if a%n == 0:
            lista.append(n)
    for j in lista:
        suma+=j
    if a > 1:
        for n in range(2,a):
            if a%n == 0:
                return suma,False
        return suma,True
    else:
        return suma,False

