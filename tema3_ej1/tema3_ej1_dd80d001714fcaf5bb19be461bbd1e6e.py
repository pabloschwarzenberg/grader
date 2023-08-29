# completa el código de la función
def suma_divisores(a):
    divisores = [1]
    for i in range(2,a+1):
        if a % i == 0:
            divisores.append(i)
    suma = sum(divisores) - a

    if suma == 1:
        return suma,True    
    elif suma == 2:
        return suma,False
    else:
        for i in range(2, suma):
            if suma % i == 0:
                return suma,True
        return suma,False 