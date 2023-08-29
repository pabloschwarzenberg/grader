def suma_divisores(nro):
    suma = 0
    for i in range(1, nro):
        if nro % i == 0:
            suma += i
    
    primo = suma == 1
    
    return suma, primo