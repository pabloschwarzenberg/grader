# completa el código de la función
def suma_divisores(a):
    divisores = []
    for i in range(1,a):
        if a % i == 0:
            divisores.append(i)
    suma = sum(divisores)
    primo = a % 2
    if primo == 1 and a != 1:
        return suma,True
    elif primo == 0 :
        return suma,False
    else:
        return suma,False