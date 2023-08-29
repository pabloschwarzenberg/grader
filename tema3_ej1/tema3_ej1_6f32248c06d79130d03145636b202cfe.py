# completa el código de la función
def suma_divisores(a):
    lista = []
    for i in range(1, a):
        if a % i == 0:
            lista.append(i)
    suma = sum(lista)
    x = suma % 2
    if a == 1:
        return suma,False 
    if suma == 1:
        return suma,True 
    if x == 1 and suma != 1:
        return suma,False
    if x == 0 and suma != 1 :
        return suma,True